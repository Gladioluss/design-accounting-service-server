class TokenError(Exception):
    pass

class BadCredentials(TokenError):
    pass

class TokenExpiredSignatureError(TokenError):
    pass

class TokenDecodeError(TokenError):
    pass

class TokenMissingRequiredClaimError(TokenError):
    pass

class WrongVerifyToken(TokenError):
    pass
