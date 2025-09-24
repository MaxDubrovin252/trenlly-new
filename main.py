from fastapi import FastAPI
from api.user import router as auth_router
import uvicorn


app = FastAPI()

app.include_router(router=auth_router)

if __name__=="__main__":
    uvicorn.run("main:app",reload=True)