from applyu_services.Models import data_mods,conn

UserAccount = data_mods.UserAccount
AccountActivation = data_mods.AccountActivation

session = conn.session()

# Delete user of AccountActivation
def delete_user_AccountActivation(username):
    session.query(AccountActivation)\
    .filter(AccountActivation.user_name == username)\
    .delete()

    session.commit()

# Delete user of UserAccount
def delete_user_UserAccount(username):
    session.query(UserAccount)\
    .filter(UserAccount.user_name == username)\
    .delete()






