from fastapi import APIRouter, HTTPException
import httpx
from config import ALPHA_VANTAGE_API_KEY, ALPHA_VANTAGE_BASE_URL
from typing import Literal

router = APIRouter()


@router.get("/{symbol}")
async def get_stock_data_from_symbol(
    symbol: Literal["IBM"], interval: Literal["1", "5", "15", "30", "60"]
):
    """
    Fetch intraday stock data for the given symbol from Alpha Vantage.

    Args:
        symbol (str): Stock ticker symbol (e.g., IBM).
        interval (str): Interval for intraday data (default is "5min"), supported interval are [1min, 5min, 15min, 30min, 60min].

    Returns:
        JSON response with stock data.
    """
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": f"{interval}min",
        "apikey": ALPHA_VANTAGE_API_KEY,
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(ALPHA_VANTAGE_BASE_URL, params=params)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.json()
            print(params)

        # Check if Alpha Vantage returns an error
        if "Error Message" in data or "Note" in data:
            raise HTTPException(
                status_code=400, detail=data.get("Error Message", "API Limit Reached")
            )

        return data

    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail=f"HTTP error occurred: {e}")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
