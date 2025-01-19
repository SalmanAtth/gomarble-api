from playwright.async_api import async_playwright
from ..services.llm import identify_css_selectors

async def extract_reviews(url: str) -> list:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        html_content = await page.content()
        css_selectors = await identify_css_selectors(html_content)
        reviews = []
        review_elements = await page.query_selector_all(css_selectors.get("review", ".review"))
        for element in review_elements:
            title = await element.query_selector(css_selectors.get("title", ".review-title"))
            body = await element.query_selector(css_selectors.get("body", ".review-body"))
            rating = await element.query_selector(css_selectors.get("rating", ".review-rating"))
            reviewer = await element.query_selector(css_selectors.get("reviewer", ".reviewer-name"))
            if body:
                reviews.append({
                    "title": await title.inner_text() if title else "N/A",
                    "body": await body.inner_text(),
                    "rating": await rating.inner_text() if rating else "N/A",
                    "reviewer": await reviewer.inner_text() if reviewer else "N/A"
                })
        await browser.close()
        return reviews