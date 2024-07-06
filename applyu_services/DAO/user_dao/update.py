from applyu_services.Models import data_mods,conn

AccountActivation = data_mods.AccountActivation
UserProfile = data_mods.UserProfile

session = conn.session()

# Activate User
def activate_user(username):
    user = session.query(AccountActivation).get(username) # find the user
    user.activate_status = True # update here
    session.commit() #sumbit

# Update User Profile
def update_user_profile(profile):
    username = profile.username
    user = session.query(UserProfile).get(username)

    user.first_name = profile.fisrt_name # update here
    user.last_name = profile.last_name   #
    user.gender = profile.gender         #
    user.birth = profile.birth           #
    user.avatar_path = profile.path      #

    session.commit() #sumbit

    



