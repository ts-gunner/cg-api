from pydantic import BaseModel, Field, field_validator
import datetime


class TaskWorkerRecord(BaseModel):
    user_id: str = Field(...)
    nickname: str = Field(...)
    remark: str = Field(...)
    task_id: str = Field(...)
    content: str = Field(...)
    create_time: str = Field(...)
    status: str = Field(...)
    category: str = Field(...)

    @field_validator("create_time", mode="before")
    @classmethod
    def switch_datetime_to_str(cls, v):
        if isinstance(v, datetime.datetime):
            return v.strftime("%Y-%m-%d %H:%M:%S")
        return v

    class Config:
        from_atrributes = True
