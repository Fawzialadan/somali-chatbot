# Somali Chatbot

A simple rule-based chatbot written in Python. It understands Somali greetings and common questions and replies in Somali.

## Features

- Asks for the user's name and remembers it during the chat
- Replies in Somali to greetings, food, tea, Somalia, and more
- Type `caawin` to see what you can ask
- Type `nabadgelyo` to exit
- Friendly fallback message when it does not understand

## How to run

1. Install [Python 3](https://www.python.org/downloads/)
2. Download `chatbot.py`
3. Open a terminal in the folder and run:

```
python chatbot.py
```

On Windows you can also use:

```
py chatbot.py
```

## Example

```
Somali Bot: Soo dhawoow! Magacaa yaa la yidhaa?
Adiga: Fawzia
Somali Bot: Waan ku faraxsanahay inaan ku arko, Fawzia!
Fawzia: salaan
Somali Bot: Salaan! Sideed tahay?
Fawzia: magacaa
Somali Bot: Magacaygu waa Somali Bot.
Fawzia: nabadgelyo
Somali Bot: Nabadgelyo, Fawzia! Maalin wanaagsan.
```

## How it works

The chatbot stores questions and answers in a Python dictionary. It reads the user's message, searches for a matching keyword, and prints the matching reply inside a `while` loop.

## Future improvements

- Add more Somali questions and answers
- Handle spelling variations
- Add more topics

## Author

Fawzia Hassan Mohamoud
