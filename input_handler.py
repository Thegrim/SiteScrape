# input_handler.py
import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validate_url(url):
    """
    Validates the given URL to ensure it is in a correct format.
    
    Args:
    url (str): The URL to validate.
    
    Returns:
    tuple: A tuple containing a boolean indicating if the URL is valid and an error message if it's not.
    """
    logging.info(f"Validating URL: {url}")
    # Regular expression pattern for validating URLs
    pattern = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    # Check if the URL matches the pattern
    match = re.match(pattern, url)
    if match:
        logging.info("URL is valid.")
        return True, ""
    else:
        error_message = "Invalid URL format."
        logging.error(f"URL validation failed: {error_message}")
        return False, error_message