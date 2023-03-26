from math import sqrt
from ar_api import schemas


def get_path(
    start_coord: tuple[float, float], 
    stop_coord: tuple[float, float]
) -> list[schemas.path.Coords]:

    start_coord = [round(start_coord[0]), round(start_coord[1])]
    end_coord = [round(stop_coord[0]), round(stop_coord[1])]
    diff_x, diff_y = 1, 1

    path = []
    while diff_x != 0 and diff_y != 0:
        diff_x = start_coord[0] - stop_coord[0]
        diff_y = start_coord[1] - stop_coord[1]

        if diff_x < 0:
            start_coord[0] += 1
        if diff_x > 0:
            start_coord[0] -= 1
        if diff_y < 0:
            start_coord[1] += 1
        if diff_x > 0:
            start_coord[1] -= 1

        path.append(schemas.path.Coords(x=start_coord[0], y=start_coord[1]))

    return path

