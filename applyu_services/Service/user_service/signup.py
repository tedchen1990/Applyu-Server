from applyu_services.DAO.user_dao import create,delete,update,read
from applyu_services.Service.user_service import pw_encrypted

def new_user_register(signup_info):
    user = None
    #need_encrypted_password = pw_encrypted.encryption(signup_info.password)
    #signup_info.password = need_encrypted_password 

    add_OK = create.create_user(signup_info) # excute insert new user
    if add_OK == True: # if add up success then review the new user status
        user = read.get_user_activate_status(signup_info.user_name)
    else:
        add_OK = False

    return add_OK,user
        
        
            
