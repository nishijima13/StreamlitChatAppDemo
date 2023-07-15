import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import const
from modules.database import database


def get_authenticator(
    db_path: str = const.DATABSE_PATH,
    cookie_name: str = const.COOKIE_NAME,
    cookie_key: str = const.COOKIE_KEY,
    cookie_expiry_days: int = const.COOKIE_EXPIRY_DAYS,
    preauthorized: bool = const.PREAUTHORIZED,
) -> stauth.authenticate.Authenticate:
    # Get authenticator
    db = database.Database(db_path)
    user_infos = db.get_all_user_infos()
    init_user_names = [uinfo["username"] for uinfo in const.USER_SETTINGS]
    all_user_names = [uinfo[0] for uinfo in user_infos]
    for uinfo in const.USER_SETTINGS:
        # Insert admin user info
        if uinfo["username"] not in all_user_names:
            db.insert_user_info(
                uinfo["username"],
                uinfo["email"],
                uinfo["name"],
                stauth.Hasher([uinfo["password"]]).generate()[0],
                uinfo["image_path"],
            )
    user_infos = db.get_all_user_infos()
    # Convert user_infos to credentials
    credentials = {"usernames": {}}
    for uinfo in user_infos:
        credentials["usernames"][uinfo[0]] = {
            "email": uinfo[1],
            "name": uinfo[2],
            "password": uinfo[3],
        }
    authenticator = stauth.Authenticate(
        credentials,
        cookie_name,
        cookie_key,
        cookie_expiry_days,
        preauthorized,
    )
    return authenticator
