# TechCrunch bot

## Description 

This is the repository of the TechCrunch WhatsApp bot made for my [Spanish YouTube channel](https://youtu.be/f6ZsXNlmeyw) if you want to know more about the development of this project I encourage you to visit that video.

### About the project

This project is a Flask app that exposes one API route with the path `/bot` which allows a POST request. When a POST request is made to that route with a `to_number` field in the JSON body, the function route uses the helper functions to:

- Scrape 10 news from [techcrunch.com](https://techcrunch.com/).
- Summarize those news using the OpenAI's GPT 4-o mini model.
- Send those summaries to the WhatsApp number took from the `to_number` field using the Twilio client,

## Pre-requirements

- Python, better if the version is higher than 3.8.x
- A Twilio account to get the Twilio account SID and auth roken.
- A OpenAI account to get a secret key.

## Installation

1. Clone the repository by using the command `git clone https://github.com/Danii2020/techcrunch-bot.git`

2. Go to the project directory by using the command `cd techcrunch-bot`

3. Create a Python virtual environment by using the following command based on your OS:

        - Windows: python -m venv venv
        - MacOS: python3 -m venv venv

4. Activate the virtual environment by using the following command based on your OS:

        - Windows: .\venv\Scripts\activate
        - MacOS: source venv/bin/activate

5. Install the required Python packages by using the command `pip install -r requirements.txt`

6. Remember to create a `.env` file with your keys, see the [.env.example](.env.example) file.

7. Go to the [app.py](app.py) file and uncomment the entry point:
```python
# if __name__ == '__main__':
#     app.run(port=4000, debug=True)
```

8. Run the app by using the command `python app.py`.

9. Copy the URL in the terminal and use a client like [Postman](https://www.postman.com/) to test the API.


## Contribution

Feel free to clone or fork this repository, test it and modify it as you want. You can open a pull request if you want to contribute with useful changes to make this project even better.