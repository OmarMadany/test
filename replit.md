# Text-to-Speech Converter

## Overview
This is a simple Python console application that converts text to speech using Google Text-to-Speech (gTTS). The application prompts the user to enter text, converts it to speech, and saves it as an MP3 file.

## Project Structure
- `gg.py` - Main Python script that handles text-to-speech conversion
- `.gitignore` - Ignores Python cache files, virtual environments, and generated MP3 files
- `pyproject.toml` - Python project configuration managed by uv
- `.pythonlibs/` - Virtual environment directory (auto-generated, ignored by git)

## Recent Changes (November 4, 2025)
- Imported from GitHub repository
- Configured for Replit environment:
  - Installed Python 3.11 and gTTS library using uv package manager
  - Removed Windows-specific `os.system("start speech.mp3")` command
  - Added user-friendly console messages indicating successful MP3 creation
  - Configured workflow to run the Python script in console mode
  - Created .gitignore for Python best practices

## How It Works
1. The script prompts the user to enter text
2. Uses Google's Text-to-Speech API to convert the text to audio
3. Saves the audio as `speech.mp3` in the project directory
4. Displays a success message with instructions to download the file

## How to Use
1. Click the "Run" button or restart the workflow
2. When prompted, type the text you want to convert to speech
3. Press Enter
4. The MP3 file will be created in the file browser
5. Download and play the `speech.mp3` file

## Dependencies
- **Python 3.11** - Programming language
- **gTTS (Google Text-to-Speech)** - Text-to-speech conversion library
- Additional dependencies: certifi, charset-normalizer, click, idna, requests, urllib3

## Technical Notes
- This is a console application (no web interface)
- Each run creates a new `speech.mp3` file, overwriting the previous one
- The application uses the default English language for speech synthesis
- MP3 files are excluded from git to keep the repository clean
