import os
import azure.cognitiveservices.speech as speechsdk
from tkinter import Tk, filedialog, StringVar, Label, OptionMenu, Button, messagebox, Text, Scrollbar, END

# Azure Speech Key and Region (replace with your own)
AZURE_SPEECH_KEY = 'YOUR_AZURE_SPEECH_API_KEY'
AZURE_REGION = 'YOUR_REGION'

# Function to convert text to speech using Azure Speech Services
def play_with_azure_tts(text, voice_name):
    speech_config = speechsdk.SpeechConfig(subscription=AZURE_SPEECH_KEY, region=AZURE_REGION)
    speech_config.speech_synthesis_voice_name = voice_name
    
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
    synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

    # Synthesize and play the speech
    result = synthesizer.speak_text_async(text).get()

    # Error handling
    if result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print(f"Speech synthesis canceled: {cancellation_details.reason}")
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print(f"Error details: {cancellation_details.error_details}")

# Voice selection window for Azure
def voice_selection_ui_azure(previous_window, input_text):
    previous_window.destroy()  # Close previous window
    
    voice_window = Tk()
    voice_window.title("Select Azure Voice")

    # List of Azure voices (You can expand this list from Azure docs)
    azure_voices = [
        "en-US-JennyNeural", "en-US-GuyNeural", "en-GB-LibbyNeural",
        "es-ES-ElviraNeural", "es-ES-AlvaroNeural", "de-DE-ConradNeural"
    ]

    selected_voice = StringVar(voice_window)
    selected_voice.set(azure_voices[0])  # Default voice

    Label(voice_window, text="Select a Voice (Azure):").pack()
    voice_menu = OptionMenu(voice_window, selected_voice, *azure_voices)
    voice_menu.pack()

    # Preview voices with a sample text
    def preview_voice_azure():
        play_with_azure_tts("The greatest glory in living lies not in never falling, but in rising every time we fall.", selected_voice.get())

    Button(voice_window, text="Preview Voice", command=preview_voice_azure).pack()

    # Convert and play the full text
    def convert_and_play_azure():
        play_with_azure_tts(input_text, selected_voice.get())

    Button(voice_window, text="Play Text", command=convert_and_play_azure).pack()

    voice_window.mainloop()

if __name__ == "__main__":
    # Assume you have a main function that gathers user input and displays the Azure voice selection
    text = "This is a sample text to be read."
    voice_selection_ui_azure(None, text)
