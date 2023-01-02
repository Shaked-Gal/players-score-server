import uvicorn
from fastapi import FastAPI

import src.api.view.user_api as user_api
import src.api.view.score_api as score_api

app = FastAPI()
app.include_router(user_api.user_router)
app.include_router(score_api.score_router)


@app.get('/')
def home():
    return {
        "message": "we are in home page"
    }


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        reload=True
    )
