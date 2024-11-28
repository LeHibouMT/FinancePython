from fastapi import APIRouter, HTTPException
from config import ALPHA_VANTAGE_API_KEY, QUANDL_BASE_URL
from typing import Literal

router = APIRouter()
