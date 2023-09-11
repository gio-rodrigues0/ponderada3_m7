from pydantic import BaseModel, Field

class DataSchema(BaseModel):
    age: int = Field(default=None)
    annual_income: int = Field(default=None)
    gender: int = Field(default=None)

    class Config:
        schema_extra = {
            "data" : {
                "age": 35,
                "annual_income": 30,
                "gender": 1
            }
        }