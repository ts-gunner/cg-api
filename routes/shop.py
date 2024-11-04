from fastapi import APIRouter, Form, UploadFile, Depends

shop_router = APIRouter(
    tags=["shop"],
    include_in_schema=True
)

