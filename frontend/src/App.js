import React from 'react';
import './App.css';
import UrlInputForm from './components/UrlInputForm';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import ResultsPage from './components/ResultsPage';

function App() {
  const handleUrlSubmit = async (url) => {
    console.log("URL submitted:", url);
    // Placeholder for actual submission logic to be implemented in the next task.
  };

  return (
    <BrowserRouter>
      <div className="App">
        <header className="App-header">
          <p>SiteScrape</p>
          <Routes>
            <Route path="/" element={<UrlInputForm onSubmit={handleUrlSubmit} />} />
            <Route path="/results" element={<ResultsPage />} />
          </Routes>
        </header>
      </div>
    </BrowserRouter>
  );
}

export default App;