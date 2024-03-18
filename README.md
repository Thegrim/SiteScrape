# SiteScrape_

SiteScrape_ is a sophisticated web crawler RPA (Robotic Process Automation) bot designed to extract all textual content from webpages based on a given URL. It navigates through specified URLs, handles redirects, and extracts visible text while excluding HTML tags, scripts, and stylesheets, providing structured, readable content ideal for data processing or analysis.

## Overview

The project utilizes Python for backend operations, employing libraries such as BeautifulSoup and Pyppeteer for parsing HTML and handling JavaScript-heavy pages, respectively. The frontend is developed with JavaScript to offer a user-friendly interface for URL submissions. SiteScrape_ features a modular architecture with separate components for URL validation, webpage content fetching, text extraction, error handling, and output formatting, ensuring maintainability and scalability.

## Features

- **URL Input Handling:** Validates and processes single URL inputs through a web interface.
- **Webpage Crawling:** Navigates to URLs, handling redirects to fetch final webpage content.
- **Text Extraction:** Extracts and preserves the structure of visible text content, excluding unnecessary HTML elements.
- **Error Handling:** Implements robust error management for network issues, access restrictions, and more, ensuring graceful error handling.
- **Output Formatting:** Outputs extracted text in structured JSON format, categorized by HTML tags for ease of use.

## Getting started

### Requirements

- Python 3.11.4
- Libraries: BeautifulSoup, Pyppeteer
- Node.js and npm for the frontend application.

### Quickstart

1. Install Python 3.11.4 and pip.
2. Clone the project repository to your local machine.
3. Create a virtual environment within the project directory: `python -m venv env`.
4. Activate the virtual environment.
5. Install required dependencies: `pip install beautifulsoup4 pyppeteer`.
6. Navigate to the frontend directory and install dependencies: `npm install`.
7. Start the backend server: `python app.py`.
8. Start the frontend application: `npm start`.
9. Open a web browser and navigate to `http://localhost:3000` to use the application.

### License

Copyright (c) 2024.