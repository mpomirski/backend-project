from pydantic import BaseModel


class MinmaxRates(BaseModel):
    min: float
    max: float
