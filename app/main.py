from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.api.v1.router import api_router
from app.core.exceptions import ConflictError, NotFoundError, ValidationError

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")


@app.exception_handler(NotFoundError)
async def not_found_handler(request: Request, exc: NotFoundError) -> JSONResponse:
    return JSONResponse(status_code=404, content={"detail": exc.message})


@app.exception_handler(ConflictError)
async def conflict_handler(request: Request, exc: ConflictError) -> JSONResponse:
    return JSONResponse(status_code=409, content={"detail": exc.message})


@app.exception_handler(ValidationError)
async def validation_handler(request: Request, exc: ValidationError) -> JSONResponse:
    return JSONResponse(status_code=422, content={"detail": exc.message})