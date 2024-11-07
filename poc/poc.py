from pydantic import BaseModel, Field

class Category(BaseModel):
    cg_name: str = Field(alias="df_name")

if __name__ == '__main__':
    c = Category(df_name="ssa")
