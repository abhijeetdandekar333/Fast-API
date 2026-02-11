from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from pymongo import MongoClient


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")



conn = MongoClient("mongodb+srv://abhijeet_dandekar_db:abcd%401234@cluster0.npaoyco.mongodb.net")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "note": doc["note"]
        })
    return templates.TemplateResponse(
        "index.html", {"request": request, "newDocs": newDocs}
    )

@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item2(request: Request, id: str):
    return templates.TemplateResponse(
        request=request, name="item.html", context={"id": id}
    )