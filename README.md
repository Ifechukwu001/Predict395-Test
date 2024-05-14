# Predict395 Test

## Setup
To run the program you must have `Python` installed on your computer.
- Clone the repository and change directory
    ```bash
        git clone https://github.com/Ifechukwu001/Predict395-Test.git ifechukwu001
        cd ifechukwu001
    ```

- Create a Virtual environment (optional)
    ```bash
        python -m venv venv
        source venv/bin/activate
    ```

- Install all dependencies
    ```bash
        pip install -U pip
        pip install -r requirements.txt
    ```

- Apply all migrations
    ```bash
        python src/manage.py migrate
    ```

- Start the Development Server
    ```bash
        python src/manage.py runserver 8888
    ```

The server is now available at http://localhost:8888
    