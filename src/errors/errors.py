def format_error(message, status_code):
  return (dict(error=dict(reason=message)), status_code)

SERVER_ERROR_500 = format_error("An unexpected error has occurred.", 500)
INVALID_LOGIN_PARAMS = format_error("Invalid email or password.", 400)
USER_NOT_FOUND = format_error("User not found.", 400)
