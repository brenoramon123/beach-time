SUCCESS_STATUSES = frozenset([200, 201])
ERROR_STATUSES = frozenset([400, 404, 500])
NO_CONTENT_STATUSES = frozenset([204])
OTP_TTL_SECONDS = 300
OTP_DIGITS = 6
OTP_MAX_ATTEMPTS = 5
RESEND_COOLDOWN = 60
TEMP_TOKEN_TTL = 600
MASK_USER_ENUMERATION = True
DEFAULT_REGION = "BR"