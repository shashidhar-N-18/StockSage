import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import ProductInsight from './pages/ProductInsight';
import AIChatbot from './pages/AIChatbot';
// import ThirdPage from './pages/ThirdPage'; // Uncomment when you have the 3rd page

function App() {
  return (
    <Router>
      <div style={{ padding: "50px%", fontFamily: "Arial" }}>
        <nav style={{ marginBottom: "20px" }}>
          <Link to="/" style={{ marginRight: "15px" }}>Product Insight</Link>
          <Link to="/chatbot" style={{ marginRight: "15px" }}>AI Chatbot</Link>
          {/* <Link to="/third">Third Page</Link> */}
        </nav>

        <Routes>
          <Route path="/" element={<ProductInsight />} />
          <Route path="/chatbot" element={<AIChatbot />} />
          {/* <Route path="/third" element={<ThirdPage />} /> */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
