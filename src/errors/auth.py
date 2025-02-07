class AuthError(Exception):
    pass

class UserAlreadyExists(AuthError):
    pass

class IncorrectLoginError(AuthError):
    message = "Incorrect email or password"

class UserValidateError(AuthError):
    pass