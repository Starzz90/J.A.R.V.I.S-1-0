import speech_recognition as sr
import pyttsx3
from jarvis_tasks import handle_task

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Capture audio from the user and convert to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand that.")
            return None
        except sr.RequestError:
            speak("Sorry, there seems to be an issue with the speech recognition service.")
            return None

if __name__ == "__main__":
    speak("Hello, I am Jarvis. How can I assist you today?")
    while True:
        command = listen()
        if command:
            if "exit" in command or "quit" in command:
                speak("Goodbye!")
                break
            else:
                response = handle_task(command)
                speak(response)