/**
 * Checks the Firebase sign-in the app sends (an ID token in the
 * Authorization header), the same way firebase-admin's verifyIdToken does:
 * Google's signature, this project as audience and issuer, not expired.
 *
 * https://firebase.google.com/docs/auth/admin/verify-id-tokens#verify_id_tokens_using_a_third-party_jwt_library
 */
import { createRemoteJWKSet, jwtVerify, type JWTVerifyGetKey } from "jose";

export interface Caller {
  uid: string;
  email?: string;
  emailVerified?: boolean;
}

const GOOGLE_KEYS = new URL(
  "https://www.googleapis.com/service_accounts/v1/jwk/securetoken@system.gserviceaccount.com",
);

/** Google's keys, fetched once per Worker instance and cached by jose. */
let googleKeys: JWTVerifyGetKey | undefined;

export type TokenVerifier = (token: string) => Promise<Caller>;

export class Unauthenticated extends Error {}

export function firebaseVerifier(projectId: string, keys?: JWTVerifyGetKey): TokenVerifier {
  return async (token) => {
    const getKey = keys ?? (googleKeys ??= createRemoteJWKSet(GOOGLE_KEYS));
    let payload;
    try {
      ({ payload } = await jwtVerify(token, getKey, {
        algorithms: ["RS256"],
        audience: projectId,
        issuer: `https://securetoken.google.com/${projectId}`,
      }));
    } catch {
      throw new Unauthenticated("invalid sign-in token");
    }
    const authTime = payload.auth_time;
    if (typeof payload.sub !== "string" || !payload.sub || (typeof authTime === "number" && authTime * 1000 > Date.now() + 60_000)) {
      throw new Unauthenticated("invalid sign-in token");
    }
    return {
      uid: payload.sub,
      email: typeof payload.email === "string" ? payload.email : undefined,
      emailVerified: payload.email_verified === true,
    };
  };
}

/** The token from "Authorization: Bearer <token>". */
export function bearerToken(header: string | null): string {
  const match = /^Bearer (\S+)$/.exec(header ?? "");
  if (!match) throw new Unauthenticated("sign in first");
  return match[1];
}
