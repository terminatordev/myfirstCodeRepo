from model.user import UserModel
from werkzeug.security import safe_str_cmp

# userdb=[User(1,'DevD','asw123'),
#         User(2,'infoblox','welcome123')]
#
# username_mapping={u.name:u for u in userdb}
# userid_mapping={u.id:u for u in userdb}

def authenticate(uname,pwd):
    # fetch_user=username_mapping.get(uname,None)
    fetch_user=UserModel.find_by_username(uname)
    if fetch_user and safe_str_cmp(fetch_user.password,pwd):
        return fetch_user

def identity(payload):
    user_id=payload['identity']
    # return userid_mapping.get(user_id,None)
    return UserModel.find_by_userid(user_id)
