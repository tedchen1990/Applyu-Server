from fastapi import APIRouter

router = APIRouter(
    prefix = "/career-service",
    tags = ["career-service"],
    responses = {404:{"decription":"Not found"}}
)

#router.include_router()

@router.get("/")
async def root():
    return { "Here is the career-service APIs !" } 