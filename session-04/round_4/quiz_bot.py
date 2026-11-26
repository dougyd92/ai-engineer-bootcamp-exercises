"""Quiz bot: ask the practice API five questions and print the answers.

Run it from the top folder of the repository:
    python session-04/round_4/quiz_bot.py
"""

import logging
from time import sleep

from practice_api import ask, PracticeAPIError

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

QUESTIONS = [
    "What is a token?",
    "What is a context window?",
    "What does temperature change?",
    "What is a system prompt?",
    "What is a stack trace?",
]

for question in QUESTIONS:
    print(f"\nQ: {question}")
    try:
        answer = ask(question)
        print(f"A: {answer}")
        

    except PracticeAPIError as error:
        logging.warning("API request failed: question=%r error=%s", question, error)
        # print(f"Something went wrong. Try again in a bit.")

    except Exception as error:
        logging.exception("Unexpected error: question=%r error=%s", question, error)
        # print(f"Something went wrong: {error}")
        raise