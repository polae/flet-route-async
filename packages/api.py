import httpx
from httpx import RequestError, HTTPError, ConnectTimeout
from pydantic import ValidationError
import os
import json

from packages.config import BASE_URL, HEADERS, QUERYSTRING
from packages.schemas import Quotation
from packages.logger import logger


async def GetQuote():
    async with httpx.AsyncClient() as client:
        try:
            r = await client.get(f"{BASE_URL}", headers=HEADERS, params=QUERYSTRING)
            r.raise_for_status()
            logger.info(f"Status code: {r.status_code}")
        except HTTPError as exc:
            logger.info(
                f"HTTP error occurred: {exc.response.status_code}\n{exc}"  # Reason: {exc.response.reason}
            )
        except ConnectTimeout as exc:
            logger.info(f"Connection to the server timed out!{str(exc)}")
        except RequestError as exc:
            logger.warn(
                f"Request URL:\n{exc.request.url}, method: {exc.request.method}\n\nRequestError:\n{str(exc)}"
            )

        r_json = r.json()
        # logger.info(json.dumps(r_json, indent=2))
        try:
            quote = Quotation(**r_json[0])
            logger.info(f"Quote:\n{quote}\n")
            return quote
        except ValidationError as e:
            print(e.errors())
            return

    # preset = Preset(**preset)
    # logger.info(f"GetPreset({preset_id}):\n{preset}\n")
