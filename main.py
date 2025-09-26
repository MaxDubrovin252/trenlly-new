from fastapi import FastAPI
from api.user import router as auth_router
from api.profiles import router as profile_router

import uvicorn


app = FastAPI()

app.include_router(router=auth_router)
app.include_router(router=profile_router)


if __name__=="__main__":
    uvicorn.run("main:app",reload=True)