import httpx
from httpx import RequestError, HTTPError, ConnectTimeout
import os
import json

from packages.schemas import Quotation
from packages.logger import logger

# API SETTINGS
api_key = os.getenv("QUOTATION_API_KEY")

url = "https://andruxnet-random-famous-quotes.p.rapidapi.com/"
querystring = {"cat": "famous", "count": "1"}
headers = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "andruxnet-random-famous-quotes.p.rapidapi.com",
}


async def GetQuote():
    async with httpx.AsyncClient() as client:
        try:
            r = await client.get(f"{url}", headers=headers, params=querystring)
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
        quote = Quotation(**r_json[0])
        logger.info(f"Quote:\n{quote}\n")

    # preset = Preset(**preset)
    # logger.info(f"GetPreset({preset_id}):\n{preset}\n")

    return quote
