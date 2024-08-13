import string

SYMBOLS = string.ascii_letters + string.digits
SHORT_ID_LENGTH = 6
MAX_URL_LENGTH = 256
MAX_SHORT_ID_LENGTH = 16
LINK_REG = r'^[a-zA-Z\d]{1,16}$'
FIELD_NAMES = {'original': 'url', 'short': 'custom_id'}
