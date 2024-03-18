import React from 'react';
import { useLocation, Link } from 'react-router-dom';
import './ResultsPage.css'; // Import the newly created CSS file

const ResultsPage = () => {
  const location = useLocation();
  const { extractedText } = location.state || {}; // Assuming `extractedText` is passed via state

  const renderContent = (data) => {
    if (typeof data === 'object') {
      return Object.entries(data).map(([key, value], index) => {
        if (Array.isArray(value)) {
          return (
            <div key={index}>
              <h2>{key}</h2>
              <ul>
                {value.map((item, itemIndex) => (
                  <li key={itemIndex}>{item}</li>
                ))}
              </ul>
            </div>
          );
        }
        return <p key={index}>{`${key}: ${value}`}</p>;
      });
    }
    return <p>{data}</p>;
  };

  return (
    <div>
      <h1 className="scraped-content">Scraped Content</h1> {/* Apply the CSS class */}
      <div className="extracted-text-container">
        {extractedText ? renderContent(extractedText) : <p>No data available. Please go back and submit a URL.</p>}
      </div>
      <Link to="/">Scrape another URL</Link>
    </div>
  );
};

export default ResultsPage;