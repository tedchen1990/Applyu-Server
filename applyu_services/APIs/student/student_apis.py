from fastapi import APIRouter

router = APIRouter(
    prefix = "/student-service",
    tags = ["student-service"],
    responses = {404:{"decription":"Not found"}}
)

#router.include_router()

@router.get("/")
async def root():
    return { "Here is the student-service APIs !" } 