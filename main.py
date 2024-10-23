import pyttsx3
import pyglet
import os
from gtts import gTTS
from tkinter import Tk, filedialog, StringVar, Label, OptionMenu, Button, messagebox, Text, Scrollbar, END
import PyPDF2
import docx
from odf import text, teletype
from odf.opendocument import load

# Initialize TTS engine
engine = pyttsx3.init()

is_paused = False

# Get available voices (from pyttsx3)
voices = engine.getProperty('voices')

# Function to play audio using pyglet
def play_audio(file):
    music = pyglet.media.load(file, streaming=False)
    music.play()
    pyglet.app.run()

# Function to extract text from PDF
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
    return text

# Function to extract text from Word docx
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return '\n'.join([para.text for para in doc.paragraphs])

# Function to extract text from ODT file
def extract_text_from_odt(file_path):
    doc = load(file_path)
    all_paragraphs = doc.getElementsByType(text.P)
    return '\n'.join([teletype.extractText(paragraph) for paragraph in all_paragraphs])

# Function to convert text to speech using pyttsx3 (offline)
def play_with_pyttsx3(text, voice_id):
    engine.setProperty('voice', voice_id)
    engine.say(text)
    engine.runAndWait()

# Function to convert text to speech using gTTS (online)
def play_with_gtts(text):
    tts = gTTS(text)
    tts.save('temp_audio.mp3')
    play_audio('temp_audio.mp3')
    os.remove('temp_audio.mp3')

def play_with_pyttsx3(text, voice_id):
    global is_paused
    engine.setProperty('voice', voice_id)
    
    def on_word(name, location, length):
        if is_paused:
            engine.pause()
    
    engine.connect('started-word', on_word)  # Trigger for each word spoken
    engine.say(text)
    engine.runAndWait()

# Function to pause/resume TTS playback
def pause_resume_pyttsx3():
    global is_paused
    if is_paused:
        engine.resume()
        is_paused = False
    else:
        is_paused = True

# GUI to choose the format and input text
def choose_input_format():
    root = Tk()
    root.title("Text-to-Speech Converter")
    
    # Variable to store user-selected format
    file_format = StringVar(root)
    file_format.set("Select Format")

    def submit_input_format():
        selected_format = file_format.get()
        if selected_format == "Text":
            text_input_ui(root)
        elif selected_format in ["PDF", "Word", "ODT"]:
            file_input_ui(root, selected_format)
        else:
            messagebox.showerror("Error", "Please select a valid format")

    # Dropdown for file format selection
    Label(root, text="Select Input Format:").pack()
    format_menu = OptionMenu(root, file_format, "Text", "PDF", "Word", "ODT")
    format_menu.pack()

    # Submit button
    Button(root, text="Next", command=submit_input_format).pack()

    root.mainloop()

# Text input window
def text_input_ui(previous_window):
    previous_window.destroy()  # Close previous window
    
    input_window = Tk()
    input_window.title("Enter Text")

    Label(input_window, text="Enter or Paste your text:").pack()

    # Text area
    text_area = Text(input_window, height=20, width=50)
    text_area.pack()

    # Scroll bar
    scroll_bar = Scrollbar(input_window)
    scroll_bar.pack(side="right", fill="y")
    text_area.config(yscrollcommand=scroll_bar.set)
    scroll_bar.config(command=text_area.yview)

    def submit_text():
        user_text = text_area.get("1.0", END)
        if user_text.strip():
            voice_selection_ui(input_window, user_text)
        else:
            messagebox.showerror("Error", "Please enter some text.")

    # Submit button
    Button(input_window, text="Next", command=submit_text).pack()

    input_window.mainloop()

# File input window
def file_input_ui(previous_window, file_type):
    previous_window.destroy()  # Close previous window
    
    file_window = Tk()
    file_window.title("Upload File")

    def upload_file():
        file_path = filedialog.askopenfilename()
        if file_path:
            if file_type == "PDF":
                text = extract_text_from_pdf(file_path)
            elif file_type == "Word":
                text = extract_text_from_docx(file_path)
            elif file_type == "ODT":
                text = extract_text_from_odt(file_path)
            voice_selection_ui(file_window, text)
    
    Label(file_window, text=f"Upload your {file_type} file").pack()

    # Upload button
    Button(file_window, text="Upload", command=upload_file).pack()

    file_window.mainloop()

# Voice selection window
def voice_selection_ui(previous_window, input_text):
    previous_window.destroy()  # Close previous window
    
    voice_window = Tk()
    voice_window.title("Select Voice")

    # Voice selection
    selected_voice = StringVar(voice_window)
    selected_voice.set(voices[0].id)  # Default voice

    Label(voice_window, text="Select a Voice:").pack()
    voice_menu = OptionMenu(voice_window, selected_voice, *[voice.id for voice in voices])
    voice_menu.pack()

    # Preview voices with a sample text
    def preview_voice():
        play_with_pyttsx3("The greatest glory in living lies not in never falling, but in rising every time we fall.", selected_voice.get())

    Button(voice_window, text="Preview Voice", command=preview_voice).pack()

    # Convert and play the full text
    def convert_and_play():
        # Offline TTS (pyttsx3)
        play_with_pyttsx3(input_text, selected_voice.get())

    def pause_play():
        pause_resume_pyttsx3()

    Button(voice_window, text="Play Text", command=convert_and_play).pack()
    Button(voice_window, text="Pause/Resume", command=pause_play).pack()

    voice_window.mainloop()

if __name__ == "__main__":
    choose_input_format()
