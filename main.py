from fastapi import FastAPI
from models import Grave
import data_service

app = FastAPI()


@app.get("/")
async def root():
    return {"title": "Cemetry Service"}


# create grave
@app.post("/graves")
async def create_grave(grave: Grave):
    data_service.create_grave(grave)
    return {"message": "Grave created"}


# fetch all graves
@app.get("/graves/all")
async def get_all_graves():
    return data_service.get_all_graves()


# fetch grave by id
@app.get("/graves/{grave_id}")
async def get_grave(grave_id: int):
    return data_service.search_grave_by_id(grave_id)


# fetch grave by name
@app.get("/graves")
async def get_grave_by_name(name: str):
    return data_service.search_grave_by_name(name)


# update grave
@app.put("/graves/{grave_id}")
async def update_grave(grave_id: int):
    return data_service.update_grave(grave_id)


# delete grave
@app.delete("/graves/{grave_id}")
async def delete_grave(grave_id: int):
    return data_service.delete_grave(grave_id)
