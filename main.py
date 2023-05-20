import config
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from bardapi import Bard

def audio_to_text(filename):
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
    try:
        return r.recognize_google(audio_data)
    except r.recognize_google(audio_data):
        print("Error handling audio_to_text(filename)")


def generate_bard_response(prompt):
    try:
        return Bard(token=config.BARD_TOKEN).get_answer(prompt)['content']
    except Bard(token=config.BARD_TOKEN).get_answer(prompt)['content']:
        print("Error generating response")


def speak_text(text):
    speech = gTTS(text=text, lang='en')
    speech.save('output.mp3')
    playsound('output.mp3')


def main():
    while True:
        print("Say Jarvis to trigger")
        with sr.Microphone() as source:
            r = sr.Recognizer()
            audio = r.listen(source)
            try:
                initiator = r.recognize_google(audio)
                if "jarvis" in initiator.lower():
                    if initiator:
                        print(f"You said: {initiator}")
                        response = generate_bard_response(config.PRE_PROMPT + initiator)
                        print(f"Jarvis said: {response}")
                        speak_text(response.replace('**JARVIS:**', ''))
            except Exception as e:
                print(f"An Error has occurred: {e}")


main()
