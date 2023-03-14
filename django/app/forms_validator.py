from typing import Optional

from pydantic import BaseModel


class GetAtivosForm(BaseModel):
    name: Optional[str]
    code: Optional[str]
    table: Optional[str]
    order_by: Optional[str]
    limit: Optional[int]


class GetAtivoByCodeForm(BaseModel):
    order_by: Optional[str]
    limit: Optional[int]


class GetAtivoByTableForm(BaseModel):
    order_by: Optional[str]
    limit: Optional[int]
