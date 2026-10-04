import secrets
from hashlib import sha256
from typing import Optional


def hash_password(password: str) -> str:
    return sha256(password.encode("utf-8")).hexdigest()


def verify_password(password: str, hashed_password: str) -> bool:
    return hash_password(password) == hashed_password


def create_access_token(subject: str) -> str:
    return secrets.token_urlsafe(32)


def get_token_from_header(authorization: str) -> Optional[str]:
    if not authorization:
        return None
    parts = authorization.split()
    if len(parts) != 2:
        return None
    return parts[1]



# security utilities, hash password, verify password, create access token, get token from header, verify token, revoke token, refresh token, generate otp, verify otp, send otp, generate magic link, verify magic link, generate biometric challenge, verify biometric response, generate sso token, verify sso token, generate 2fa token, verify 2