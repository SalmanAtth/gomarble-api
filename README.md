GoMarble Assignment: Product Review Extractor
This project is an API server that extracts reviews from any given product page using Playwright for web scraping and Hugging Face's Falcon-7B model for dynamic CSS selector identification. The API is built with FastAPI, and the frontend is a simple React application.

Table of Contents
Features

Project Structure

Setup

Running the Backend

Running the Frontend

API Usage

Example Pages

Contributing

License

Features
Dynamic CSS Selector Identification: Uses Hugging Face's Falcon-7B model to dynamically identify CSS selectors for reviews.

Web Scraping: Uses Playwright to scrape reviews from product pages.

Pagination Handling: Automatically handles pagination to extract all reviews.

Frontend UI: A simple React frontend to interact with the API.

Project Structure
Copy
gomarble-api/
├── backend/
│   ├── main.py
│   ├── api/
│   │   ├── endpoints.py
│   ├── services/
│   │   ├── scraper.py
│   │   ├── llm.py
│   ├── models/
│   │   ├── schemas.py
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── App.jsx
│   │   ├── index.js
│   ├── package.json
│   ├── package-lock.json
│   ├── .env
├── requirements.txt
├── README.md
├── .gitignore
├── .env
Setup
1. Clone the Repository
bash
Copy
git clone https://github.com/your-username/gomarble-api.git
cd gomarble-api
2. Install Backend Dependencies
Create a virtual environment:

bash
Copy
python -m venv venv
Activate the virtual environment:

On Windows:

bash
Copy
.\venv\Scripts\activate
On macOS/Linux:

bash
Copy
source venv/bin/activate
Install the required Python packages:

bash
Copy
pip install -r requirements.txt
Install Playwright browsers:

bash
Copy
playwright install
3. Install Frontend Dependencies
Navigate to the frontend directory:

bash
Copy
cd frontend
Install the required Node.js packages:

bash
Copy
npm install
Running the Backend
Navigate to the backend directory:

bash
Copy
cd backend
Start the FastAPI server:

bash
Copy
uvicorn main:app --reload
The API will be available at:

Copy
http://127.0.0.1:8000
Running the Frontend
Navigate to the frontend directory:

bash
Copy
cd frontend
Start the React development server:

bash
Copy
npm start
The frontend will be available at:

Copy
http://localhost:3000
API Usage
Endpoint: /api/reviews
Method: GET

Query Parameter:

url: The URL of the product page.

Response:

json
Copy
{
  "reviews_count": 100,
  "reviews": [
    {
      "title": "Review Title",
      "body": "Review body text",
      "rating": 5,
      "reviewer": "Reviewer Name"
    },
    ...
  ]
}
Example Request
bash
Copy
curl "http://localhost:8000/api/reviews?url=https://2717recovery.com/products/recovery-cream"
Example Pages
Here are some example product pages you can use to test the API:

2717 Recovery Cream

Bhumi Flannelette Sheet Set

LyfeFuel Essentials Nutrition Shake

Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.

Create a new branch:

bash
Copy
git checkout -b feature/your-feature-name
Commit your changes:

bash
Copy
git commit -m "Add your feature"
Push to the branch:

bash
Copy
git push origin feature/your-feature-name
Open a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Let me know if you need further assistance! 🚀
