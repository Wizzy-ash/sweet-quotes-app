from kivy.app import App
from kivy.uix.label import Label
import random

quotes = [
    "Life is short. Smile while you still have teeth! 😁",
    "Happiness is a choice, choose wisely! 💖",
    "Love yourself first! 💕",
    "Make today amazing! 🌟",
]

class SweetQuotesApp(App):
    def build(self):
        return Label(text=random.choice(quotes), font_size='24sp')

if __name__ == "__main__":
    SweetQuotesApp().run()
