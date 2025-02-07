class AuthError(Exception):
    pass

class UserAlreadyExists(AuthError):
    pass

class UserValidateError(AuthError):
    pass