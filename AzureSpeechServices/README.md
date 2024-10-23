C) Text-to-Speech Converter Using Amazon Polly

1) Overview

This version of the project integrates with Amazon Polly, a cloud-based service that offers a wide variety of lifelike voices for text-to-speech synthesis. Users can select the input format (text, PDF, Word, ODT), choose a voice from Amazon Polly, and play the converted speech. The program provides a GUI where users can also pause and resume the speech playback.

2) Features

- Supports input in the form of plain text, PDF, Word (docx), or ODT files.
- Integrates with Amazon Polly for realistic, high-quality speech synthesis.
- Allows users to select from multiple Polly voices.
- Supports play, pause, and resume functionality for the speech playback.

6) Prerequisites

To use Amazon Polly, you'll need:

- An AWS account.
- IAM user credentials (Access Key ID and Secret Access Key) with permissions to use Amazon Polly.
- Installing Dependencies

The following Python libraries are required:

- boto3
- pygame
- PyPDF2
- python-docx
- odfpy
- tkinter

7) You can install all dependencies using:

![alt text](image.png)

8) Configuration

Update the following variables in the Python script with your AWS credentials:

![alt text](image-1.png)

9) Usage

- Run the script.
- Select the input format (Text, PDF, Word, or ODT).
- Either enter the text directly or upload the selected file type.
- Preview and select from Amazon Polly's available voices.
- The program will synthesize the text to speech and play it, with pause and resume functionality.

10) How to Run

![alt text](image-2.png)