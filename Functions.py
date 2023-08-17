import csv
import pygame
import random
from gtts import gTTS
import tempfile
import time
import os

def read_csv(file_name):
    with open(file_name, newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        # Skip the header row
        next(reader, None)
        # Create a list of questions
        all_questions = [(row[0], row[1], row[2]) for row in reader]
        random.shuffle(all_questions)
    return all_questions

def playaudio(audio,language):
    tts = gTTS(text=audio, lang=language)
    # Save the audio to a temporary file
    filename = tempfile.NamedTemporaryFile(suffix=".mp3", delete=False).name
    tts.save(filename)

    pygame.mixer.init()
    pygame.mixer.music.load(filename)

    # Play the audio
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(0.01)

    pygame.mixer.stop()
    pygame.mixer.quit()

    # Delete the temporary file after playing the audio
    os.remove(filename)
