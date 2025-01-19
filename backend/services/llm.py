import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("huggin-face-api-token to be added here")
API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

def get_selectors_from_model(prompt):
    data = json.dumps({"inputs": prompt})
    response = requests.post(API_URL, headers=headers, data=data)

    if response.status_code == 200:
        result = response.json()
        return result
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

async def identify_css_selectors(html_content: str) -> dict:
    prompt = (
        "Extract CSS selectors for the following elements in this HTML:\n"
        "- Title of the review\n"
        "- Body of the review\n"
        "- Rating\n"
        "- Reviewer's name\n\n"
        f"HTML:\n{html_content}"
    )
    selectors = get_selectors_from_model(prompt)
    if selectors:
        return selectors
    else:
        print("Failed to generate CSS selectors. Using default selectors.")
        return {
            "review": ".review",
            "title": ".review-title",
            "body": ".review-body",
            "rating": ".review-rating",
            "reviewer": ".reviewer-name"
        }
