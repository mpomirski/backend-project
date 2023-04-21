from pydantic import BaseModel


class MaxRateDifference(BaseModel):
    max: float
