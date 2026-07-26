# codealpha_task4# Simple Python Chatbot

A minimal command-line chatbot written in Python. It responds to a few basic
keywords typed by the user and keeps the conversation going until the user
decides to end it.

## Features

- Case-insensitive matching (`hello`, `HELLO`, `Hello` all work the same)
- Recognizes simple greetings and questions:
  - `hello` → greets you back
  - `how are you` → shares how it's doing
  - `bye` → says goodbye and ends the conversation
- Falls back to a default response for anything it doesn't understand

## Requirements

- Python 3.x (no external libraries needed)

## Usage

1. Save the script as `chatbot.py` (or keep the provided filename).
2. Run it from your terminal:

   ```bash
   python chatbot.py
   ```

3. Start chatting! Example session:

   ```
   Hello , I am a chatbot ! (type 'bye' to exit)
   You : hello
   Bot : hi !
   You : how are you
   Bot : I'm doing well, thank you !
   You : what's the weather like?
   Bot : Sorry, I didn't understand.
   You : bye
   Bot : Goodbye !
   ```

## How It Works

The chatbot runs an infinite loop that:

1. Prompts the user for input and converts it to lowercase.
2. Checks the message for known keywords (`hello`, `bye`, `how are you`).
3. Prints a matching response, or a default fallback message if no keyword
   is found.
4. Exits the loop when the user types a message containing `bye`.

## Possible Improvements

- Add more keywords and responses
- Use regular expressions for more flexible matching
- Handle multiple keywords in a single message more gracefully
- Add unit tests
- Turn it into a simple GUI or web app

## License

Feel free to use, modify, and share this project for learning purposes.
