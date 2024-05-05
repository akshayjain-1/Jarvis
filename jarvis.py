"""
Jarvis AI
"""
import os
import webbrowser
import speech_recognition as sr
import wikipedia as wk
import openai as oa
import pyaudio


def speak(text: str):
    """
    This function speaks a message using the system's text-to-speech engine.

    Parameters:
    text (str): Text to be spoken

    Returns:
    None
    """
    # The "espeak" module is for Linux OS. For MAC OS, use "say" or "ptts" for Windows OS
    os.system(f'espeak "{text}"')


def speech_input():
    """
    This function listens to the user's voice and returns the text that was heard.

    Parameters:
    None

    Returns:
    text (str): Text that was heard
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 2  # Seconds of non-speaking before a phrase is considered complete
        speak("What can I do for you today?")
        audio = r.listen(source)  # Listen for the user's input

    try:
        text = r.recognize_google(audio, language="en-in")  # Convert speech to text
        print(text)
        return text
    except sr.UnknownValueError:
        speak("Sorry, I could not understand your speech.")
    except sr.RequestError:
        speak("Could not request results from Google Speech Recognition service")


def open_website(website: str):
    """
    Opens a website based on the input string.

    Parameters:
    website (str): The name of the website to open.

    Returns:
    None
    """
    if "youtube" in website:
        speak("Opening Youtube")
        webbrowser.open("https://youtube.com")
    elif "google" in website:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "wikipedia" in website:
        speak("Searching Wikipedia...")
        search_ip = website.replace("wikipedia", "")
        results = wk.summary(search_ip, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)
    else:
        speak("Sorry, I could not find the website you are looking for.")

if __name__ == "__main__":
    speak("I am Jarvis!")
    while True:
        user_ip = speech_input()
        if "open" in user_ip:
            open_website(user_ip)


#  To-do integrate openai
