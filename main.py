import uvicorn
from fastapi import FastAPI

import src.api.view.user_api as user_api

app = FastAPI()
app.include_router(user_api.router)


@app.get('/')
def home():
    return {
        "message": "we are in home page"
    }


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='127.0.0.1',
        port=8000,
        reload=False,
    )
