from fastapi import APIRouter
from applyu_services.APIs.user import signup
from applyu_services.APIs.user import login

router = APIRouter(
    prefix = "/user-service",
    tags = ["user-service"],
    responses = {404:{"decription":"Not found"}}
)

router.include_router(signup.router)
router.include_router(login.router)

@router.get("/")
async def root():
    return { "Here is the user-service APIs !" } 