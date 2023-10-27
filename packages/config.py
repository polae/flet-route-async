import os

# API SETTINGS
api_key = os.getenv("QUOTATION_API_KEY")


BASE_URL = "https://andruxnet-random-famous-quotes.p.rapidapi.com/"
QUERYSTRING = {"cat": "famous", "count": "1"}
HEADERS = {
    "X-RapidAPI-Key": api_key,
    "X-RapidAPI-Host": "andruxnet-random-famous-quotes.p.rapidapi.com",
}
