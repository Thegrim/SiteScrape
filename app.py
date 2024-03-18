from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from input_handler import validate_url
from web_handler import fetch_webpage_content
from text_extractor import extract_text
from output_formatter import format_output
from fastapi.middleware.cors import CORSMiddleware
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = FastAPI(title="SiteScrape_", description="A web crawler RPA bot that extracts all textual content from webpages.")

# Configure CORS with specific settings for production
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with the actual origins of your frontend application
    allow_credentials=True,
    allow_methods=["GET", "POST"],  # Explicitly specify allowed methods
    allow_headers=["*"],
)

class URLInput(BaseModel):
    url: str

@app.post("/extract-text/")
async def extract_text_from_url(input: URLInput):
    logging.info("Received request to extract text from URL.")
    
    # Validate URL
    logging.info(f"Validating URL: {input.url}")
    is_valid, error = validate_url(input.url)
    if not is_valid:
        logging.error(f"URL validation failed: {error}")
        raise HTTPException(status_code=400, detail=error)
    logging.info("URL validation successful.")

    # Fetch webpage content
    logging.info(f"Fetching content for URL: {input.url}")
    webpage_content = fetch_webpage_content(input.url)
    if isinstance(webpage_content, tuple) and 'error' in webpage_content[0]:
        # If the error is returned from fetch_webpage_content
        error_response = webpage_content
        logging.error(f"Error fetching webpage content: {error_response[0]['error']}")
        raise HTTPException(status_code=error_response[1], detail=error_response[0]['error'])
    logging.info("Webpage content fetched successfully.")

    # Extract text
    logging.info("Extracting text from webpage content.")
    extracted_text = extract_text(webpage_content)
    if 'error' in extracted_text:
        # If the error is returned from extract_text
        logging.error(f"Error during text extraction: {extracted_text['error']}", exc_info=True)
        status_code = extracted_text.get('status', 500)
        raise HTTPException(status_code=status_code, detail=extracted_text['error'])
    logging.info("Text extraction successful.")

    # Format output
    logging.info("Formatting extracted text to JSON.")
    output = format_output(extracted_text)
    if 'error' in output:
        # If the error is returned from format_output
        logging.error(f"Error formatting output: {output['error']}", exc_info=True)
        status_code = output.get('status', 500)
        raise HTTPException(status_code=status_code, detail=output['error'])
    logging.info("Output formatted successfully.")

    return {"extracted_text": output}