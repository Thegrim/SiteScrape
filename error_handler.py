# error_handler.py
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def handle_network_error(e):
    logging.error(f"Network error occurred: {e}", exc_info=True)
    return {"error": "Network error occurred, please try again later."}, 503

def handle_access_denied_error(e):
    logging.error(f"Access denied error occurred: {e}", exc_info=True)
    return {"error": "Access denied. You might not have the permission to access this page."}, 403

def handle_page_not_found_error(e):
    logging.error(f"Page not found error occurred: {e}", exc_info=True)
    return {"error": "The requested page does not exist."}, 404

def handle_generic_error(e):
    logging.error(f"An unexpected error occurred: {e}", exc_info=True)
    return {"error": "An unexpected error occurred, please try again later."}, 500