import logging
from bs4 import BeautifulSoup
from error_handler import handle_generic_error

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_text(html_content):
    """
    Extracts and structures text from given HTML content using BeautifulSoup.

    Args:
    html_content (str): HTML content of the webpage.

    Returns:
    dict: A dictionary containing structured text with HTML tags as keys and corresponding text as values.
    """
    try:
        logging.info("Starting text extraction process.")
        soup = BeautifulSoup(html_content, 'html.parser')

        # Remove script and style elements
        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()

        structured_text = {}

        # Extract and structure text based on tags
        for tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li']:
            elements = soup.find_all(tag)
            structured_text[tag] = [element.get_text(separator=" ", strip=True) for element in elements]

        logging.info("Text extraction process completed successfully.")
        return structured_text
    except Exception as e:
        logging.error("An error occurred during the text extraction process.", exc_info=True)
        return handle_generic_error(e)