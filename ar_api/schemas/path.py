from pydantic import BaseModel


class Coords(BaseModel):
    x: float
    y: float


class StartEndPathCoords(BaseModel):
    start_coords: Coords
    end_coords: Coords


class Path(BaseModel):
    points: list[Coords]
