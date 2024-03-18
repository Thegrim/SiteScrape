import logging
from urllib.robotparser import RobotFileParser
from ratelimit import limits, sleep_and_retry
from requests.exceptions import HTTPError
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ComplianceManager:
    def __init__(self, rate_limit_calls, rate_limit_period):
        self.rate_limit_calls = rate_limit_calls
        self.rate_limit_period = rate_limit_period

    def check_robots_txt(self, target_url):
        """
        Checks if the crawler is allowed to access the target URL based on the site's robots.txt.
        Args:
        - target_url (str): The URL of the target website.
        
        Returns:
        - bool: True if allowed, False otherwise.
        """
        try:
            parsed_url = requests.utils.urlparse(target_url)
            base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
            robots_txt_url = f"{base_url}/robots.txt"
            rp = RobotFileParser()
            rp.set_url(robots_txt_url)
            rp.read()
            can_fetch = rp.can_fetch("*", target_url)
            if not can_fetch:
                logging.warning(f"Access to {target_url} is disallowed by robots.txt")
            return can_fetch
        except HTTPError as e:
            logging.error(f"Failed to fetch robots.txt for {target_url}: {e}")
            return False
        except Exception as e:
            logging.error(f"An error occurred while checking robots.txt for {target_url}: {e}", exc_info=True)
            return False

    @sleep_and_retry
    @limits(calls=lambda self: self.rate_limit_calls, period=lambda self: self.rate_limit_period)
    def rate_limited_request(self, url):
        """
        Performs a rate-limited HTTP GET request to the specified URL.
        Args:
        - url (str): The URL to fetch.
        
        Returns:
        - Response: The response object from requests.get() if successful, None otherwise.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response
        except Exception as e:
            logging.error(f"Error making rate-limited request to {url}: {e}", exc_info=True)
            return None