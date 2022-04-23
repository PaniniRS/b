import json

API = "https://api.gettr.com"
WEBSITE = "https://gettr.com"

LOGIN_URL = WEBSITE + '/login'
AUTHORIZE_URL = API + '/s/auth_up'

FOLLOW_URL = API + '/u/user/{}/follows/{}'
UNFOLLOW_URL = API + '/u/user/{}/unfollows/{}'
FOLLOWINGS_URL = API + '/u/user/{}/followings'
SUGGESTIONS_URL = API + '/s/usertag/suggest'

MAX_FOLLOWS_PER_DAY = 600
TOKEN = None

def get_headers_from_dict(headers):
    return {k: json.dumps(v) if isinstance(v, dict) else v for k, v in headers.items()}
