# Project Setup

### 1. Create a `.env` File

Create a file named `.env` in the root of your project directory and add the following line:

```env
# Database Configuration
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/db_name

# Google OAuth Credentials
GOOGLE_CLIENT_ID=client_id
GOOGLE_CLIENT_SECRET=client_secret
GOOGLE_REDIRECT_URI=server_url/callback

# Pipenv Configuration
PIPENV_VENV_IN_PROJECT=1
PIPENV_VERBOSITY=-1
```

Replace `username`, `password`, and `db_name` with your actual MySQL database credentials.

---

### 2. Project Setup Guide

This guide explains how to install the necessary dependencies for the project using the `Pipfile.lock` with `pipenv`.

#### Prerequisites

1. **Python**: Ensure Python is installed (preferably Python 3.7 or later).  
2. **pip**: Ensure `pip` (Python package manager) is installed.

---

#### Installation Steps

1. **Create a Virtual Environment**  
   First, create a virtual environment using the `venv` module that comes with Python:
   ```bash
   python -m venv .venv
   ```
   This will create a `.venv` directory in your project, which will hold the virtual environment.

2. **Activate the Virtual Environment**  
   After creating the virtual environment, you need to activate it:

   - **On Windows:**
     ```bash
     .\.venv\Scripts\activate
     ```
   - **On macOS/Linux:**
     ```bash
     source .venv/bin/activate
     ```

   After activation, you should see `(.venv)` in your terminal prompt, indicating that the virtual environment is active.

3. **Install `pipenv` from `requirements.txt`**  
   If `pipenv` is listed as a dependency in your `requirements.txt`, install it with the following command:
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Dependencies from `Pipfile.lock`**  
   Once `pipenv` is installed, you can use it to install the project dependencies:

   - To install both regular and development dependencies from `Pipfile.lock`, use:
     ```bash
     pipenv install --dev
     ```
   - If you only need the regular dependencies (without development dependencies), use:
     ```bash
     pipenv install
     ```

---

### 3. Start the Application

Once the setup is complete, you can start the application by running the following command from the root directory:

```bash
python main.py
```

This will initialize and start the application using the configurations defined in your `.env` file. Ensure your `.env` file is properly configured before running the command.
