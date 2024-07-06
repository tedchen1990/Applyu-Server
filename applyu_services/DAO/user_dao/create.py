from applyu_services.Models import data_mods,conn

UserAccount = data_mods.UserAccount

session = conn.session()

# insert new user in UserAccount table
def create_user(signup_info):
    add_OK = False

    add_user_name = signup_info.user_name
    add_password = signup_info.password
    add_account_type_id = signup_info.account_type_id
    add_reg_mode_id = signup_info.reg_mode_id
    add_country_code = signup_info.reg_mode_code
    add_email = signup_info.email
    add_phone = signup_info.phone
    
    new_user = UserAccount(user_name = add_user_name,
                           password = add_password,
                           account_type_id = add_account_type_id,
                           reg_mode_id = add_reg_mode_id,
                           country_code = add_country_code,
                           email = add_email,
                           phone = add_phone)

    session.add(new_user)
    
    try:
        session.commit()
        add_OK = True # succuess 
    except Exception:
        add_OK = False # something wrong
        
    return add_OK