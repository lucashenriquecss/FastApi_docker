from fastapi import FastAPI
# import models
# from config import engine

# models.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello "}
