import os
import webbrowser

def handle_task(command):
    """Process the user's command and execute the appropriate task."""
    if "open browser" in command:
        webbrowser.open("https://www.google.com")
        return "Opening the browser."
    elif "play music" in command:
        music_directory = "path_to_your_music_directory"
        songs = os.listdir(music_directory)
        os.startfile(os.path.join(music_directory, songs[0]))
        return "Playing music."
    elif "what is your name" in command:
        return "I am Jarvis, your personal assistant."
    elif "time" in command:
        from datetime import datetime
        now = datetime.now()
        return f"The current time is {now.strftime('%H:%M:%S')}."
    else:
        return "Sorry, I can't perform that task yet."