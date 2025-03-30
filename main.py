from fastapi import FastAPI
from database import init_db
import links
import auth
from projects import router as projects_router

init_db()

app = FastAPI()
app.include_router(links.router)
app.include_router(auth.router)
app.include_router(projects_router)


@app.get("/")
def read_root():
    return {"message": "URL Shortener Service"}
