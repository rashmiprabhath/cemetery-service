from pydantic import BaseModel


class Grave(BaseModel):
    id: int
    name: str
    slots: str | None = None
    garden: str | None = None
    section: str | None = None
    lot: str | None = None
    block: str | None = None
    space: str | None = None