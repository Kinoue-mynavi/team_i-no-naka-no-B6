import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import "./root.css";
import LoginPage from './pages/LoginPage';
import HomePage from './pages/HomePage';

const App: React.FC = () => {
  return (
    <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="*" element={<h1>Not Found Page</h1>} />
        </Routes>
    </BrowserRouter>
  );
};

export default App
