import React, { useState } from 'react';
import axios from 'axios';

function ProductInsight() {
  const [productId, setProductId] = useState("");
  const [htmlResult, setHtmlResult] = useState("");

  const getInsights = async () => {
    try {
      const res = await axios.post('http://localhost:8000/product/insight', { product_id: productId }, {
        headers: {
          'Content-Type': 'application/json',
        },
        responseType: 'text', // ensure raw HTML is returned
      });
      setHtmlResult(res.data);
    } catch (err) {
      console.error("Error fetching insights:", err);
      setHtmlResult("<p style='color:red;'>Error fetching insights</p>");
    }
  };

  return (
    <div style={{ padding: '1rem' }}>
      <h2>Product Insight</h2>
      <input
        value={productId}
        onChange={(e) => setProductId(e.target.value)}
        placeholder="Enter Product ID"
        style={{ padding: '0.5rem', marginRight: '1rem' }}
      />
      <button onClick={getInsights} style={{ padding: '0.5rem 1rem' }}>
        Get Insight
      </button>

      {htmlResult && (
        <div
          style={{ marginTop: '2rem', border: '1px solid #ccc', padding: '1rem', borderRadius: '8px' }}
          dangerouslySetInnerHTML={{ __html: htmlResult }}
        />
      )}
    </div>
  );
}

export default ProductInsight;
