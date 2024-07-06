from fastapi import APIRouter
from applyu_services.Service.user_service.login import user_login
from pydantic import BaseModel

router = APIRouter()
# API-----User Login-----------------
class login_info (BaseModel):
        uep:str
        password:str

@router.post("/login")
async def login(login_info:login_info):
        login_status,user = user_login(login_info)
        return login_status,user
