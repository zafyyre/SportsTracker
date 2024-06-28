# Sports Tracking App

This repository contains the backend for the Sports Tracking App. Follow the instructions below to set up and run the backend on your local machine.

# Backend Setup

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Setup Instructions

### 1. Clone the Repository

First, clone this repository to your local machine:

\`\`\`bash
git clone https://github.com/zafyyre/SportsTracker.git
cd SportsTracker/backend
\`\`\`

### 2. Set Up Python Virtual Environment

Create and activate a Python virtual environment:

\`\`\`bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
\`\`\`

### 3. Install Required Packages

Install the required Python packages using \`requirements.txt\`:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 4. Set Up Environment Variables

Create a \`.env\` file in the \`backend\` directory and add the necessary environment variables. You will need to set the \`SPORTSDB_KEY\`:

\`\`\`
SPORTSDB_KEY=your_sportsdb_api_key_here
\`\`\`

### 5. Run the Flask Application

Ensure your virtual environment is activated, then run the Flask application:

\`\`\`bash
flask run
\`\`\`

The backend server should now be running, and you can access it at \`http://127.0.0.1:5000\`.

## Directory Structure

\`\`\`
backend/
│
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│
├── venv/
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│
├── .env
├── requirements.txt
├── run.py
├── sports.db
\`\`\`

## Additional Notes

- Ensure your \`SPORTSDB_KEY\` is correctly set in the \`.env\` file.
- The database file \`sports.db\` will be created in the root of the \`backend\` directory when the application is run for the first time.

## Troubleshooting

If you encounter any issues, ensure you have followed all the setup steps correctly and that your environment variables are set up properly.
"""
