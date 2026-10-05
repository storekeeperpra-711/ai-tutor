"""Cloudflare KV storage for Mithu's recordings, through Cloudflare's API.

The AI server (worker/) reads the same storage (binding VOICE) and hands
the recordings to the app. Needs CLOUDFLARE_API_TOKEN and
CLOUDFLARE_ACCOUNT_ID (the GitHub secrets the deploy workflow already
uses; the "Edit Cloudflare Workers" token template includes KV).

    # The storage's id (made the first time), for wrangler.toml:
    python tools/voice/kv.py namespace-id
"""

from __future__ import annotations

import base64
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request

# One storage for both servers: the recordings are the same for dev and prod.
NAMESPACE_TITLE = "ai-tutor-voice"
API = "https://api.cloudflare.com/client/v4"


class KV:
    def __init__(self, token: str, account: str, namespace: str | None = None):
        self._token = token
        self._base = f"{API}/accounts/{account}/storage/kv/namespaces"
        self.namespace = namespace

    @classmethod
    def from_env(cls) -> "KV":
        token = os.environ.get("CLOUDFLARE_API_TOKEN")
        account = os.environ.get("CLOUDFLARE_ACCOUNT_ID")
        if not token or not account:
            raise SystemExit("CLOUDFLARE_API_TOKEN and CLOUDFLARE_ACCOUNT_ID are needed "
                             "(GitHub secrets, docs/setup/ai-setup.md).")
        return cls(token, account)

    def _call(self, method: str, url: str, body=None, raw: bool = False):
        data = None if body is None else json.dumps(body).encode()
        req = urllib.request.Request(url, data=data, method=method, headers={
            "Authorization": f"Bearer {self._token}",
            "Content-Type": "application/json",
        })
        try:
            with urllib.request.urlopen(req, timeout=60) as res:
                payload = res.read()
        except urllib.error.HTTPError as e:
            if raw and e.code == 404:
                return None
            raise RuntimeError(f"Cloudflare said {e.code}: "
                               f"{e.read().decode(errors='replace')[:300]}") from None
        if raw:
            return payload
        answer = json.loads(payload)
        if not answer.get("success", False):
            raise RuntimeError(f"Cloudflare said: {answer.get('errors')}")
        return answer

    def ensure_namespace(self, title: str = NAMESPACE_TITLE) -> str:
        """The storage's id; makes it the first time."""
        page = 1
        while True:
            answer = self._call("GET", f"{self._base}?per_page=100&page={page}")
            for ns in answer["result"]:
                if ns["title"] == title:
                    self.namespace = ns["id"]
                    return ns["id"]
            if len(answer["result"]) < 100:
                break
            page += 1
        self.namespace = self._call("POST", self._base, {"title": title})["result"]["id"]
        return self.namespace

    def get(self, key: str) -> bytes | None:
        url = f"{self._base}/{self.namespace}/values/{urllib.parse.quote(key, safe='')}"
        return self._call("GET", url, raw=True)

    def put_many(self, values: dict[str, bytes]) -> None:
        """Writes several keys in one request."""
        body = [{"key": k, "value": base64.b64encode(v).decode(), "base64": True}
                for k, v in values.items()]
        self._call("PUT", f"{self._base}/{self.namespace}/bulk", body)


def main(argv: list[str]) -> int:
    if argv != ["namespace-id"]:
        print(__doc__)
        return 1
    print(KV.from_env().ensure_namespace())
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
