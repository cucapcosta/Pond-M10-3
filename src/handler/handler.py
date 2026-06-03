from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from domain.entities.figurinha import Figurinha
from service.figurinhaServ import FigurinhaService

app = FastAPI()


@app.exception_handler(RequestValidationError)
def on_validation_error(request: Request, exc: RequestValidationError):
    return JSONResponse(status_code=400, content={"detail": exc.errors()})


@app.post("/figurinha", response_model=Figurinha, status_code=201)
def createFig(fig:Figurinha):
    return FigurinhaService.addFig(fig)

@app.get("/figurinhas")
def getAllFigs():
    return FigurinhaService.getAllFigs()

@app.get("/figurinha/{id}", response_model=Figurinha)
def getFigs(id: int):
    fig = FigurinhaService.getFigs(id)
    if fig is None:
        raise HTTPException(status_code=404, detail="Figurinha não encontrada")
    return fig

@app.put("/figurinha/{id}", response_model=Figurinha)
def updateFig(id: int, fig: Figurinha):
    updated = FigurinhaService.updateFig(id, fig)
    if updated is None:
        raise HTTPException(status_code=404, detail="Figurinha não encontrada")
    return updated

@app.delete("/figurinha/{id}")
def deleteFig(id: int):
    deleted = FigurinhaService.deleteFig(id)
    if deleted is None:
        raise HTTPException(status_code=404, detail="Figurinha não encontrada")
    return {"deleted": id}

