from pydantic import BaseModel


class MinmaxRateDifference(BaseModel):
    min: float
    max: float
