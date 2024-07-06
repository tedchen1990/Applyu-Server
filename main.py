import uvicorn
from fastapi import FastAPI
from applyu_services.APIs.base import base_apis
from applyu_services.APIs.career import career_apis
from applyu_services.APIs.student import student_apis
from applyu_services.APIs.user import user_apis

applyu = FastAPI(root_path="/api")

applyu.include_router(user_apis.router)
applyu.include_router(career_apis.router)
applyu.include_router(student_apis.router)
applyu.include_router(base_apis.router)

@applyu.get("/")
async def root():
    return {"Welcome to Applyu APIs !"}

#if __name__ == "__main":
#    uvicorn.run("main:applyu",host="0.0.0.0",port=8000,reload=True)
