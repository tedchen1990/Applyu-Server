from fastapi import APIRouter

router = APIRouter(
    prefix = "/base-service",
    tags = ["base-service"],
    responses = {404:{"decription":"Not found"}}
)

#router.include_router()

@router.get("/")
async def root():
    return { "Here is the base-service APIs !" } 