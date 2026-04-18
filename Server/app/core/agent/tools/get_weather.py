import os
from dotenv import load_dotenv
from langchain.tools import tool
from requests import get
from typing import TypedDict
load_dotenv()

class weather(TypedDict):
    city:str
    key:str
    extensions:str


@tool
def get_weather(location:str)->str:
    """
    根据location获取指定天气
    """
    params:weather = {
        "city":location,
        "key":os.getenv("amap_key"),
        "extensions":"base"
    }
    url = 'https://restapi.amap.com/v3/weather/weatherInfo?parameters'
    weather_result = get(url,params).json()
    return  weather_result.get('lives')[0]["weather"]
