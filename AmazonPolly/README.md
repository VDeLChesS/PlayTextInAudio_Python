B) Text-to-Speech Converter Using Microsoft Azure Speech Services

This project demonstrates how to convert text to speech using Microsoft Azure's Speech Services. It supports various input formats (text, PDF, Word, ODT) and allows users to preview and select from multiple Azure voices. The program also provides a GUI where users can play, pause, and resume the speech.

1) Overview

This version of the project leverages Microsoft Azure's Speech Services for high-quality, lifelike text-to-speech synthesis. It supports various input formats (text, PDF, Word, ODT) and allows users to preview and select from multiple Azure voices. The program also provides a GUI where users can play, pause, and resume the speech.

2) Features

- Supports input in the form of plain text, PDF, Word (docx), or ODT files.
- Integrates with Microsoft Azure's Speech Service to provide realistic, human-like voices.
- Allows users to choose from a list of available Azure voices.
- Offers play, pause, and resume functionality for the synthesized speech.

3) Prerequisites

To use Azure Speech Services, you'll need:

- An Azure account.
- A Speech Service resource created in the Azure portal.
- Your Azure Speech API Key and Region.

4) Installing Dependencies

The following Python libraries are required:

- azure-cognitiveservices-speech
- PyPDF2
- python-docx
- odfpy
- tkinter

You can install all dependencies using:

![image](https://github.com/user-attachments/assets/ea305f84-7bb7-407b-b9a5-800f4506ae19)


5) Configuration

Update the following variables in the Python script with your Azure credentials:

![image](https://github.com/user-attachments/assets/9c0788d8-729a-4dfe-a3ea-e21f71ca6573)


6) Usage

- Run the script.
- Select the input format (Text, PDF, Word, or ODT).
- Either enter the text directly or upload the selected file type.
- Preview and select from Azure’s available voices.
- The program will synthesize the text to speech and play it, with pause and resume functionality.

7) How to Run

![image](https://github.com/user-attachments/assets/4f819143-71bf-4351-b5e2-898c0654a82c)
