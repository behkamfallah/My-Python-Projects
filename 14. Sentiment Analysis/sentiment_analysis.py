from textblob import TextBlob
from dataclasses import dataclass


@dataclass
class Mood:
    feeling: str
    sentiment: float


def get_mood(input_text: str, *, sensitivity: float) -> Mood:
    polarity: float = TextBlob(input_text).sentiment.polarity

    friendly_treshold: float = sensitivity
    hostile_treshold: float = -sensitivity

    if polarity >= friendly_treshold:
        return Mood('Happy', polarity)
    elif polarity < hostile_treshold:
        return Mood('Angry', polarity)
    else:
        return Mood('Neutral', polarity)


def run_bot():
    print('Enter a word or sentence to get the sentiment analysis.')
    while True:
        user_input: str = input('You: ')
        mood: Mood = get_mood(user_input, sensitivity=0.3)
        print(f'Bot: {mood.feeling} ({mood.sentiment})')


if __name__ == "__main__":
    run_bot()
