import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def format_output(extracted_text):
    """
    Converts the extracted text into a JSON format.

    Args:
    extracted_text (dict): A dictionary containing structured text with HTML tags as keys.

    Returns:
    str: A JSON string representing the structured text content.
    """
    try:
        logging.info("Formatting output to JSON.")
        # Convert dictionary to JSON string
        json_output = json.dumps(extracted_text, indent=4, ensure_ascii=False)
        return json_output
    except Exception as e:
        logging.error(f"Error formatting output: {e}", exc_info=True)
        # In a real scenario, you might want to handle this more gracefully
        return json.dumps({"error": "Failed to format output."})