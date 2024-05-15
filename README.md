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

## Demo

![image](https://github.com/Ifechukwu001/Predict395-Test/assets/66724426/143aad96-9f6e-4ac1-b1ae-4641df7dd57a)
![image](https://github.com/Ifechukwu001/Predict395-Test/assets/66724426/1692b5cb-5250-4731-92aa-3b1fe460c2a1)
![image](https://github.com/Ifechukwu001/Predict395-Test/assets/66724426/beb0bcfd-e790-463d-978b-11472e1566fa)
![image](https://github.com/Ifechukwu001/Predict395-Test/assets/66724426/0a005681-30dc-4102-8164-a68bebe623c6)
![image](https://github.com/Ifechukwu001/Predict395-Test/assets/66724426/03ef11bb-efc8-4dec-b846-be3911a18429)
![image](https://github.com/Ifechukwu001/Predict395-Test/assets/66724426/9d59bb91-a3b5-418f-9fab-e0c8fe6c07cd)
![image](https://github.com/Ifechukwu001/Predict395-Test/assets/66724426/3595a57c-2f88-4f9c-bb9d-1b4897e083de)
![image](https://github.com/Ifechukwu001/Predict395-Test/assets/66724426/1619a11b-3c0b-4ca9-8575-a6762cbf64a0)

## Tests

To test the application, run the following command from the root of the repository after the [setup](#setup)
```bash
    python src/manage.py test
```

## Admin Interface

To access the admin interface, you need to first create a superuser.
```bash
    python src/manage.py createsuperuser
```
Then navigate to the admin root url http://localhost:8888/admin and login with the superuser credentials.


---
Developed by ifechukwu T. Ogidi ([Ifechukwu001](https://github.com/ifechukwu001))





