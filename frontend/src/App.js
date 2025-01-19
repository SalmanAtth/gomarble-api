import React, { useState } from "react";
import "./App.css";

function App() {
  const [url, setUrl] = useState("");
  const [reviews, setReviews] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const fetchReviews = async () => {
    setLoading(true);
    setError("");
    try {
      const response = await fetch(
        `http://127.0.0.1:8000/api/reviews?url=${encodeURIComponent(url)}`
      );
      if (!response.ok) {
        throw new Error(`Error: ${response.status} - ${response.statusText}`);
      }
      const data = await response.json();
      setReviews(data.reviews);
    } catch (error) {
      setError("Failed to fetch reviews. Please check the URL and try again.");
      console.error(error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>Product Review Extractor</h1>
      <div>
        <input
          type="text"
          placeholder="Enter product page URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
        />
        <button onClick={fetchReviews} disabled={loading}>
          {loading ? "Loading..." : "Extract Reviews"}
        </button>
      </div>
      {error && <p style={{ color: "red" }}>{error}</p>}
      <div>
        <h2>Reviews</h2>
        {reviews.length > 0 ? (
          <ul>
            {reviews.map((review, index) => (
              <li key={index}>
                <h3>{review.title}</h3>
                <p>{review.body}</p>
                <p>Rating: {review.rating}</p>
                <p>Reviewer: {review.reviewer}</p>
              </li>
            ))}
          </ul>
        ) : (
          <p>No reviews found.</p>
        )}
      </div>
    </div>
  );
}

export default App;