
import uvicorn
from fastapi import FastAPI
import os
from routers import example_router

app = FastAPI()
app.include_router(example_router.router)




if __name__ == "__main__":
	uvicorn.run("main:app", host="0.0.0.0", port=9000, log_level="info", reload=True)
