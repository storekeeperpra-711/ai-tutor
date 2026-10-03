import assert from "node:assert/strict";
import { describe, it } from "node:test";

import { SignJWT, createLocalJWKSet, exportJWK, generateKeyPair } from "jose";

import { Unauthenticated, bearerToken, firebaseVerifier } from "../auth";

async function keys() {
  const { publicKey, privateKey } = await generateKeyPair("RS256");
  const jwk = { ...(await exportJWK(publicKey)), kid: "k1", alg: "RS256" };
  return { privateKey, jwks: createLocalJWKSet({ keys: [jwk] }) };
}

async function token(privateKey: CryptoKey, project: string, claims: Record<string, unknown> = {}) {
  const now = Math.floor(Date.now() / 1000);
  return new SignJWT({ email: "parent@example.com", email_verified: true, auth_time: now, ...claims })
    .setProtectedHeader({ alg: "RS256", kid: "k1" })
    .setIssuer(`https://securetoken.google.com/${project}`)
    .setAudience(project)
    .setSubject("u1")
    .setIssuedAt(now)
    .setExpirationTime(now + 3600)
    .sign(privateKey);
}

describe("Firebase sign-in check", () => {
  it("accepts a token for this project", async () => {
    const { privateKey, jwks } = await keys();
    const caller = await firebaseVerifier("demo", jwks)(await token(privateKey, "demo"));
    assert.deepEqual(caller, { uid: "u1", email: "parent@example.com", emailVerified: true });
  });

  it("refuses a token for another project, a forged one, or none", async () => {
    const { privateKey, jwks } = await keys();
    const other = await keys();
    const verify = firebaseVerifier("demo", jwks);
    await assert.rejects(verify(await token(privateKey, "someone-else")), Unauthenticated);
    await assert.rejects(verify(await token(other.privateKey, "demo")), Unauthenticated);
    await assert.rejects(verify("not-a-token"), Unauthenticated);
    assert.throws(() => bearerToken(null), Unauthenticated);
    assert.throws(() => bearerToken("Basic abc"), Unauthenticated);
    assert.equal(bearerToken("Bearer abc.def"), "abc.def");
  });
});
