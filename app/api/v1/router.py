from fastapi import APIRouter

from .user.route import user_router
from .code.route import code_router
from .questions.route import questions_router
from .profile.route import profile_router

api_router = APIRouter()

# create user, login user, logout user, refresh token, get user profile, update user profile, delete user profile, get all users, get user by id, get user by email, 
# get user by username, get user by phone number, get user by social media id, get user by social media username, get user by social media email, get user by social media phone number, 
# get user by social media token, get user by social media refresh token, get user by social media access token, get user by social media provider id, 
# get user by social media provider name, get user by social media provider type, get user by social media provider scope, get user by social media provider redirect uri,
#  get user by social media provider state, get user by social media provider code, get user by social media provider error, get user by social media provider error description
api_router.include_router(
    user_router,
    prefix="/user",
    tags=["User"]
)

# code submit, code run, code compile, code debug, code format, code lint, code test, code analyze, code optimize, code refactor, code document, code visualize, 
# code explain, code translate, code convert, code generate, code scaffold, code template, code snippet, code example, code sample, code demo, code tutorial, code guide,
# code walkthrough
api_router.include_router(
    code_router,
    prefix="/code",
    tags=["Code"]
)

# questions create, questions read, questions update, questions delete, questions list, questions search, questions filter, questions sort, questions paginate, questions tag, 
# questions category, questions difficulty, questions type, questions answer, questions explanation, questions hint, questions solution, questions test case, questions input,
# questions output, questions example, questions sample, questions demo, questions tutorial, questions guide, questions walkthrough
api_router.include_router(
    questions_router,
    prefix="/questions",
    tags=["Questions"]
)

# profile get, profile update, profile delete, profile list, profile search, profile filter, profile sort, profile paginate, profile tag, profile category, 
# profile difficulty, profile type, profile answer, profile explanation, profile hint, profile solution, profile test case, profile input, profile output, 
# profile example, profile sample, profile demo, profile tutorial, profile guide, profile walkthrough
api_router.include_router(
    profile_router,
    prefix="/profile",
    tags=["Profile"]
)


# api setup, setup infra, setup redis, setup db, setup logger, setup config, setup env variables, setup error handling, setup middlewares, setup routes, setup tests