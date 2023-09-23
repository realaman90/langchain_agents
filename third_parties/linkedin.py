import os
import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin(url: str):
    print(os.getenv("PROXYCURL_API_KEY"))
    """
    Scrapes a linkedin profile and returns the text
    """
    api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
    header_dict = {"Authorization": f"Bearer {os.getenv('PROXYCURL_API_KEY')}"}

    response = requests.get(api_endpoint, headers=header_dict, params={"url": url})
    data = response.json()
    data = {
        k: v
        for k, v in data.items()
        if v not in ([], "", "", None)
        and k
        not in [
            "people_also_viewed",
            "similarly_named_profiles",
            "education" "certifications",
            "volunteer_work",
            "experience",
            "skills",
            "accomplishments",
            "interests",
            "recommendations",
            "groups",
        ]
    }
    # print (data)

    if data.get("groups"):
        for group_dict in data.get("groups"):
            group_dict.pop("profile_pic_url")

    return data
