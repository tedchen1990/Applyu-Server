from applyu_services.Models import data_mods,conn

UserAccount = data_mods.UserAccount
AccountActivation = data_mods.AccountActivation

session = conn.session()

# Ger all users
def get_all_user():
    users = session.query(UserAccount)\
                    .order_by(UserAccount.user_name)\
                    .all()
    return users


# Get an user by username and password
def get_user_by_U_password(username,password):
    user = session.query(UserAccount)\
                    .filter(UserAccount.user_name == username,
                            UserAccount.password == password)\
                    .first()
    return user

# Get an user by email and password
def get_user_by_E_password(email,password):
    user = session.query(UserAccount)\
                    .filter(UserAccount.email == email,
                            UserAccount.password == password)\
                    .first()
    return user

# Get an user by phone and password
def get_user_by_P_password(phone,password):
    user = session.query(UserAccount)\
                    .filter(UserAccount.phone == phone,
                            UserAccount.password == password)\
                    .first()
    return user

# Get an user with activate status by username
def get_user_activate_status(username):
    user = session.query(AccountActivation)\
                    .filter(AccountActivation.user_name == username)\
                    .first()
    return user