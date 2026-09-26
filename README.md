# AI YouTube Video Analyzer

An AI-powered YouTube video analyzer built using **Agno**, **Groq**, **YouTube Tools**, and **Streamlit**.

The application analyzes YouTube videos and provides a structured overview of the video content, important topics, learning points, and timestamps when reliable timestamp information is available.

## Features

- AI-powered YouTube video analysis
- Video overview and content analysis
- Topic and theme identification
- Meaningful timestamps when available
- Key learning points
- Content organization
- Identification of important demonstrations and references
- Prevents fake timestamps and unsupported information  
- Streamlit-based web interface
- Built using Agno and Groq
  
## Architecture

```text
                    YouTube Video URL
                           |
                           v
                 +-------------------+
                 |  Streamlit UI     |
                 +---------+---------+
                           |
                           v
                 +-------------------+
                 |  YouTube Agent    |
                 +---------+---------+
                           |
                           v
                    YouTube Tools
                           |
                           v
                      Groq AI Model
                           |
                           v
                  Video Analysis
                           |
                           v
              +-----------------------+
              | Overview              |
              | Topics & Themes       |
              | Timestamps            |
              | Learning Points       |
              +-----------------------+
```

## Technologies Used

-Python
-Agno
-Groq
-YouTube Tools
-YouTube Transcript API
-Streamlit
-python-dotenv

## Project Structure
```text
youtube-analyzer/
|
├── youtube_analyzer.py
├── app.py
├── requirements.txt
├── .gitignore
└── .env
```

## Installation

Clone the repository:
```bash
git clone https://github.com/arishak10/youtube-analyzer.git
cd youtube-analyzer
```
Create a virtual environment:
```bash
python -m venv .venv
```
Activate the virtual environment on Windows:
```bash
.venv\Scripts\activate
```
Install the required packages:
```bash
pip install -r requirements.txt
```

## Environment Setup

Create a .env file in the project folder:
```bash
GROQ_API_KEY=your_groq_api_key
```
Replace your_groq_api_key with your own Groq API key.
Never upload your .env file or expose your API key publicly.

## Run the Project

Start the Streamlit application:
```bash
streamlit run app.py
```
The application will open in your browser.

## Example

Enter a YouTube video URL such as:

https://www.youtube.com/watch?v=...

## The AI agent analyzes the video and provides:

Video overview
Main topics
Content structure
Important learning points
Relevant timestamps when available
Practical demonstrations and references

## Purpose

This project demonstrates how an AI agent can use YouTube tools and a large language model to analyze video content and organize useful information into a structured response.

## Author

Arisha Khan

Computer Science Student | AI/ML Enthusiast
