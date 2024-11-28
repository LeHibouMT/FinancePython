from fastapi import APIRouter, HTTPException
from .alphaVantage import avs
from .quandl import qds
import httpx

router = APIRouter()

router.include_router(avs.router, prefix="/av")
router.include_router(qds.router, prefix="/ql")


@router.get("")
async def get_stock_data():
    """
    Fetch stock data.

    Args:
        None

    Returns:
        JSON response with stock data.
    """

    try:
        return {"data": True}

    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"HTTP error occurred: {e}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
