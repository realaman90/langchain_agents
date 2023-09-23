from langchain import SerpAPIWrapper

from dotenv import load_dotenv
import os

load_dotenv()
serp_api_key = os.getenv("SERP_API_KEY")


def get_profile_url(text: str) -> str:
    """Searches for linkedin profile"""

    search = SerpAPIWrapper(serpapi_api_key=serp_api_key)
    res = search.run(f"{text} ")

    return res
