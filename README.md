# bookrecommender
https://bookrecommenderr.onrender.com/
A Book Recommender System built using Python, Flask, and machine learning techniques to provide personalized book recommendations based on user input.

Features

Home Page: Displays popular books with their authors, ratings, and cover images.

Recommendation: Users can search for a book and get similar book recommendations.

Interactive UI: Simple web interface built with Flask templates.

Backend: Uses precomputed similarity scores for fast recommendations.

Technologies Used

Backend: Python, Flask

Data Processing: Pandas, NumPy

Machine Learning: Scikit-learn (similarity computation)

Frontend: HTML, CSS, Jinja2 templates

Data Storage: Pickle files for models and datasets

Dataset

popular.pkl – contains popular books data (titles, authors, ratings, images)

books.pkl – full dataset of books

pt.pkl – pivot table of books used for similarity calculations

similarity_scores.pkl – precomputed similarity scores between books

Note: The datasets are stored as pickle files due to their large size.

Installation

Clone the repository:

git clone https://github.com/kiran566/bookrecommender.git
cd bookrecommender


Create and activate a virtual environment:

python -m venv .venv
# Windows
.\.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate


Install dependencies:

pip install -r requirements.txt

Run Locally
python app.py


Open your browser at: http://127.0.0.1:5000/

Use the search bar to get book recommendations.

Deployment

This app can be deployed on Render, Heroku, or any Python web hosting service.

Render deployment: Use the main branch from GitHub, set build command as:

pip install -r requirements.txt


Set start command:

python app.py


Make sure to use a runtime.txt for Python version (e.g., python-3.11.8)

Large files may need to be hosted externally (Google Drive / AWS S3) for faster deployment.
