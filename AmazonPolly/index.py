import boto3
import os
from pygame import mixer  # For playing audio
from tkinter import Tk, filedialog, StringVar, Label, OptionMenu, Button, messagebox, Text, Scrollbar, END

# AWS Credentials (replace with your credentials)
AWS_ACCESS_KEY = 'YOUR_AWS_ACCESS_KEY'
AWS_SECRET_KEY = 'YOUR_AWS_SECRET_KEY'
AWS_REGION = 'YOUR_AWS_REGION'

# Initialize AWS Polly Client
polly_client = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
).client('polly')

# Function to convert text to speech using Amazon Polly
def play_with_polly_tts(text, voice_id):
    response = polly_client.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId=voice_id
    )

    # Save the audio stream returned by Amazon Polly as an mp3 file
    file_name = 'polly_output.mp3'
    with open(file_name, 'wb') as file:
        file.write(response['AudioStream'].read())

    # Play the mp3 using pygame
    mixer.init()
    mixer.music.load(file_name)
    mixer.music.play()

    while mixer.music.get_busy():  # Wait for the audio to finish
        continue

    os.remove(file_name)  # Remove the file after playing

# Voice selection window for Amazon Polly
def voice_selection_ui_polly(previous_window, input_text):
    previous_window.destroy()  # Close previous window
    
    voice_window = Tk()
    voice_window.title("Select Polly Voice")

    # List of Polly voices (You can expand this list from Amazon Polly docs)
    polly_voices = [
        "Joanna", "Matthew", "Ivy", "Justin", "Kendra", "Kimberly",
        "Salli", "Amy", "Emma", "Brian", "Nicole", "Russell"
    ]

    selected_voice = StringVar(voice_window)
    selected_voice.set(polly_voices[0])  # Default voice

    Label(voice_window, text="Select a Voice (Polly):").pack()
    voice_menu = OptionMenu(voice_window, selected_voice, *polly_voices)
    voice_menu.pack()

    # Preview voices with a sample text
    def preview_voice_polly():
        play_with_polly_tts("The greatest glory in living lies not in never falling, but in rising every time we fall.", selected_voice.get())

    Button(voice_window, text="Preview Voice", command=preview_voice_polly).pack()

    # Convert and play the full text
    def convert_and_play_polly():
        play_with_polly_tts(input_text, selected_voice.get())

    Button(voice_window, text="Play Text", command=convert_and_play_polly).pack()

    voice_window.mainloop()

if __name__ == "__main__":
    # Assume you have a main function that gathers user input and displays the Polly voice selection
    text = "This is a sample text to be read."
    voice_selection_ui_polly(None, text)
