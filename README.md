# Review Shelf

Review Shelf is a book review and rating community platform built with Django.

## Installation

### Prerequisites

- Python 3.9+

### Installation Steps

```bash
# Clone the Repository
git clone https://github.com/yourusername/review-shelf.git
cd review-shelf

# Create and Activate Virtual Environment
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

# Install Dependencies
pip install -r requirements.txt

# Create .env File 
Copy the contents from .env.example and add your credentials

# Apply Migrations
python manage.py migrate

# Run the Development Server
python manage.py runserver
