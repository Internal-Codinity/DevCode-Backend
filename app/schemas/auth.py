from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
# pip install pydantic-extra-types phonenumbers


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class RegisterRequest(BaseModel):
    name: str
    email: EmailStr
    number: 

# auth schemas, login request, token response, register request, user response, forgot password request, reset password request, change password request, 
# verify email request, resend verification email request, revoke tokens request, refresh token request, social login request, otp login request,
# magic link login request, biometric login request, passwordless login request, sso login request, 2fa login request, mfa login request, totp login request, 
# hotp login request, sms otp login request, email otp login request, push notification otp login request