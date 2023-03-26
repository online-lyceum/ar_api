import logging

from fastapi import APIRouter, Depends, Query

from ar_api import schemas
from ar_api.services.algorithms import get_path


logger = logging.getLogger(__name__)
router = APIRouter(
    prefix='/api/path',
    tags=["Path finding"],
)


@router.get('', response_model=schemas.path.Path)
async def find_path(start_x: float = Query(None), start_y: float = Query(None),
                    end_x: float = Query(None), end_y: float = Query(None)):
    print(schemas.path.Path(points=get_path(
        (start_x, start_y), 
        (end_x, end_y))
    ))

    return schemas.path.Path(points=get_path(
        (start_x, start_y), 
        (end_x, end_y))
    )

