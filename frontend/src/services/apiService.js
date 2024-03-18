import axios from 'axios';

// Function to perform a POST request to the backend
export const fetchExtractedText = async (url) => {
    try {
        // Use environment variable for the backend base URL
        const BASE_URL = process.env.REACT_APP_BACKEND_URL || 'http://localhost:8000';
        const response = await axios.post(`${BASE_URL}/extract-text/`, { url });
        console.log("Extracted text fetched successfully.");
        return response.data; // Return the response data from the server
    } catch (error) {
        if (error.response) {
            // The request was made and the server responded with a status code
            // that falls out of the range of 2xx
            console.error("Error data:", error.response.data);
            console.error("Error status:", error.response.status);
            throw new Error(`Server responded with an error: ${error.response.data.detail}`);
        } else if (error.request) {
            // The request was made but no response was received
            console.error("Error request:", error.request);
            throw new Error('No response from the server. Please try again later.');
        } else {
            // Something happened in setting up the request that triggered an Error
            console.error('Error message:', error.message);
            throw new Error('Error in setting up the request.');
        }
    }
};