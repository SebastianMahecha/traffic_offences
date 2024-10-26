from fastapi import FastAPI
import config.db as db
import routes.user as user_routes

app = FastAPI()

app.include_router(user_routes.router)

# Create the database tables
@app.on_event("startup")
def on_startup():
    db.init_db()

@app.get("/")
async def root():
    return {"message": "Hello World"}


