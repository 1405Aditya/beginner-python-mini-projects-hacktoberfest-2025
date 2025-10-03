# Hangman (Beginner-Friendly)

A simple command-line Hangman game written in Python. Guess the secret word one letter at a time before you run out of mistakes.

## Features

- Category-based random words (animals, fruits, colors)
- ASCII gallows graphics
- Clean, readable code with small functions

## Requirements

- Python 3.8+
- No external dependencies

## How to Run

```bash
# From the repository root
python src/zenitsu0509-hangman/main.py
```

Optional arguments:

```bash
python src/zenitsu0509-hangman/main.py --word fruits       # pick a category
python src/zenitsu0509-hangman/main.py --max-mistakes 8    # change difficulty
```

## Project Structure

```text
src/zenitsu0509-hangman/
  ├── main.py      # game logic + CLI
  └── README.md    # this file
```

## Contributing / Learning

- Read through `main.py` — it’s organized for clarity.
- Good beginner exercises:
  - Add a hint feature (reveal one random letter)
  - Track and display remaining letters not yet guessed
  - Add more categories or load words from a file

Enjoy playing and hacking on it! 🎉
