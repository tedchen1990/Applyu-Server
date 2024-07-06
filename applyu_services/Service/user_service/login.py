from applyu_services.DAO.user_dao import read,update,create,delete

# Login by username and password
def user_login(login_info):
    user = None
    login_auth = False
    uep = login_info.uep 
    pw = login_info.password
    
    user = read.get_user_by_U_password(uep,pw)
    if user != None:
        login_auth = True
    else:
        user = read.get_user_by_E_password(uep,pw)
        if user != None:
            login_auth = True
        else:
            user = read.get_user_by_U_password(uep,pw)
            if user != None:
                login_auth = True

    return login_auth,user


