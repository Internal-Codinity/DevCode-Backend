class AppError(Exception):
    pass

class NotFoundError(AppError):
    pass

class AuthenticationError(AppError):
    pass




# application exceptions, not found error, authentication error, authorization error, validation error, database error, external service error, internal server error, custom application error 