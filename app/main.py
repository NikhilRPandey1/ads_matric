from fastapi import FastAPI, Request
import uvicorn
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from app.api.accounts.matrics_routes import router as user_router
from app.db.session import engine
from app.db.base import Base

app = FastAPI(
    title="Ad Metrics",
    description="Service for advertising metrics",
)

# Include routers
app.include_router(user_router, prefix="/api/v1")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_messages = [
        {
            "type": error["type"],
            "field": error["loc"][-1],
            "message": error["msg"],
        }
        for error in exc.errors()
    ]
    return JSONResponse(
        status_code=422,
        content=error_messages,
    )


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# if __name__ == "__main__":
#     uvicorn.run(reload=True)
