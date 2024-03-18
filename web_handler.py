# Module for handling web requests.

import requests
from bs4 import BeautifulSoup
import logging
import asyncio
from pyppeteer import launch
from error_handler import handle_network_error, handle_generic_error

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_javascript_rendered_page(url):
    """
    A simple check to guess if the page might be using JavaScript to render content.
    This function can be enhanced based on requirements.
    """
    try:
        response = requests.get(url)
        if "application/json" in response.headers.get("Content-Type", ""):
            logging.info("Page seems to be JSON/API driven.")
            return True
        if len(response.content) < 15000:  # Arbitrary limit for simplicity
            logging.info("Page content size suggests dynamic JavaScript rendering might be involved.")
            return True
        return False
    except Exception as e:
        logging.error(f"Error checking if page is JavaScript rendered: {e}", exc_info=True)
        return False

async def fetch_content_with_pyppeteer(url):
    """
    Fetch webpage content for JavaScript-heavy pages using pyppeteer.
    """
    try:
        browser = await launch()
        page = await browser.newPage()
        await page.goto(url)
        content = await page.content()
        await browser.close()
        return content
    except Exception as e:
        logging.error(f"Error fetching webpage content with pyppeteer: {e}", exc_info=True)
        return handle_generic_error(e)

def fetch_webpage_content(url):
    """
    Fetches the webpage content, handling both simple and JavaScript-heavy pages.
    """
    logging.info(f"Fetching content for: {url}")
    if is_javascript_rendered_page(url):
        logging.info("Detected JavaScript-heavy page, using pyppeteer.")
        # Pyppeteer is async, so run it in an event loop
        content = asyncio.get_event_loop().run_until_complete(fetch_content_with_pyppeteer(url))
    else:
        try:
            response = requests.get(url, allow_redirects=True)
            response.raise_for_status()  # Will raise an HTTPError for bad responses
            content = response.text
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching webpage content with requests: {e}", exc_info=True)
            return handle_network_error(e)
        except Exception as e:
            logging.error(f"Unexpected error fetching webpage content: {e}", exc_info=True)
            return handle_generic_error(e)

    if content:
        logging.info("Successfully fetched webpage content.")
    else:
        logging.warning("Failed to fetch webpage content.")
    return content