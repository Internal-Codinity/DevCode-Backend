from fastapi import APIRouter, HTTPException, status

from app.schemas.auth import LoginRequest, TokenResponse
from app.services.auth_service import AuthService

route = APIRouter()
service = AuthService()

@route.post("/", response_model=TokenResponse)
def login(payload: LoginRequest):
    token = service.authenticate_user(payload.email, payload.password)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    return TokenResponse(access_token=token)






































# login route, login with different providers, login with email and password, login with otp, login with magic link, login with social media, login with google,
# login with facebook, login with twitter, login with github, login with linkedin, login with apple, login with microsoft, login with amazon, login with custom provider,
# login with jwt, login with oauth2, login with openid connect, login with saml, login with ldap, login with active directory, login with radius, login with kerberos, 
# login with sso, login with 2fa, login with mfa, login with totp, login with hotp, login with sms otp, login with email otp, login with biometric authentication, 
# login with passwordless authentication, login with webauthn, login with fido2, login with u2f, login with passkeys, login with security keys, login with yubi key, 
# login with google authenticator,login with push notification otp 