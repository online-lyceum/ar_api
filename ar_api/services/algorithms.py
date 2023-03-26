from math import sqrt
from ar_api import schemas


def get_path(
    start_coord: tuple[float, float], 
    stop_coord: tuple[float, float]
#) -> list[schemas.path.Coords]:
):
    start_coord = [round(start_coord[0]), round(start_coord[1])]
    stop_coord = [round(stop_coord[0]), round(stop_coord[1])]
    diff_x, diff_y = 1, 1

    path = []
    while start_coord != stop_coord:
        if start_coord[0] < stop_coord[0]:
            start_coord[0] += 1
        if start_coord[0] > stop_coord[0]:
            start_coord[0] -= 1
        if start_coord[1] < stop_coord[1]:
            start_coord[1] += 1
        if start_coord[1] > stop_coord[1]:
            start_coord[1] -= 1

        #path.append(tuple(start_coord))
        path.append(schemas.path.Coords(x=start_coord[0], y=start_coord[1]))

    return path

