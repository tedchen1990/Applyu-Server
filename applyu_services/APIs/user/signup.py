from fastapi import APIRouter
from applyu_services.Service.user_service.signup import new_user_register
from pydantic import BaseModel

router = APIRouter()

# API-----User Sign Up----------------- http(s)://8.218.238.147/api/user-service/signup
class signup_info (BaseModel):
        user_name: str
        password:str
        account_type_id:int
        reg_mode_id:int
        country_code:str
        email:str
        phone:str

@router.post("/signup")
async def signup(signup_info:signup_info):
        user,signup_status = new_user_register(signup_info)
        return user,signup_status





