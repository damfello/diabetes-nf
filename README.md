# Diabetes Challenge Machine Learning Project

This project implements an end-to-end machine learning pipeline to predict diabetes outcomes using data extracted from a PostgreSQL database.

## Project Structure

```
diabetesproject/
│
├── solutions/
│   └── 1_diabetes_challenge.ipynb   # Main Jupyter Notebook containing the workflow
├── data/                            # Directory for local data storage
├── .env                             # Local database configuration (ignored by Git)
├── .env.example                     # Template for environment variables
├── pyproject.toml                   # Project dependencies and configuration
└── README.md                        # Project documentation
```

## Setup & Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd diabetesproject
   ```

2. Ensure you have your dependencies installed via your preferred environment manager (e.g., using `uv` or `pip`):
   ```bash
   pip install -e .
   ```

3. Create a `.env` file in the root directory based on your database credentials to securely connect to the SQL playground:
   ```env
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=your_db_host
   DB_PORT=5432
   DB_NAME=postgres
   ```

## Usage

Open the Jupyter notebook inside the `solutions` folder:
```bash
jupyter notebook solutions/1_diabetes_challenge.ipynb
```
