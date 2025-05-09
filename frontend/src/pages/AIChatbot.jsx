import React, { useState } from 'react';

const AIChatbot = () => {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setResponse('');

    try {
      const res = await fetch('http://localhost:8000/chat/query', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query }),
      });

      const html = await res.text();
      console.log(html)// now response is actual HTML string
      setResponse(html);
    } catch (error) {
      console.error('Error:', error);
      setResponse('<p style="color:red;">An error occurred while contacting the chatbot.</p>');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: '2rem' }}>
      <h2>AI Chatbot</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask something..."
          style={{ width: '70%', padding: '0.5rem' }}
        />
        <button type="submit" style={{ padding: '0.5rem 1rem', marginLeft: '1rem' }}>
          Submit
        </button>
      </form>

      {loading && <p style={{ marginTop: '1rem' }}>Loading...</p>}

      {response && (
        <div
          style={{
            marginTop: '2rem',
            background: '#f4f4f4',
            padding: '1rem',
            borderRadius: '8px',
            overflowX: 'auto',
          }}
          dangerouslySetInnerHTML={{ __html: response }}
        />
      )}
    </div>
  );
};

export default AIChatbot;
