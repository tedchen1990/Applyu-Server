from applyu_services.Models import data_mods,conn

UserAccount = data_mods.UserAccount
AccountActivation = data_mods.AccountActivation

session = conn.session()

# Ger users
def get_all_user(get_username,get_real_password):
    users = session.query(UserAccount)\
        .join(AccountActivation,UserAccount.user_name == AccountActivation.user_name)\
        .filter(UserAccount.user_name == get_username,UserAccount == get_real_password)\
        .all()
    return users





