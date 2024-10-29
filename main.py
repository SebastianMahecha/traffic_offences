from fastapi import FastAPI
import config.db as db
import routes.user as user_routes
import uvicorn

app = FastAPI()

app.include_router(user_routes.router)

# Create the database tables
@app.on_event("startup")
def on_startup():
    db.init_db()

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
