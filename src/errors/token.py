class TokenError(Exception):
    pass

class TokenExpiredSignatureError(TokenError):
    pass

class TokenDecodeError(TokenError):
    pass

class TokenMissingRequiredClaimError(TokenError):
    pass