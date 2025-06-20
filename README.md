# AI Doctor with Vision and Voice 🩺🔍🎤

An intelligent multimodal AI doctor application that combines computer vision, speech recognition, and text-to-speech capabilities to provide medical consultations through voice and image analysis.

## 🌟 Features

- **Voice Input**: Record audio queries about medical concerns
- **Image Analysis**: Upload medical images for visual diagnosis
- **AI-Powered Diagnosis**: Professional medical analysis using advanced LLMs
- **Voice Response**: Natural speech output of medical recommendations
- **Interactive Web Interface**: User-friendly Gradio-based interface

## 🏗️ Project Structure

```
ai-doctor/
├── brain_of_the_doctor.py      # Core image analysis and LLM processing
├── voice_of_the_patient.py     # Audio recording and speech-to-text
├── voice_of_the_doctor.py      # Text-to-speech functionality
├── gradio_app.py               # Main application interface
├── .env                        # Environment variables (not included)
└── README.md                   # This file
```

## 🤖 AI Models & APIs Used

### Large Language Models (LLMs)
- **Meta LLaMA 4 Scout**: `meta-llama/llama-4-scout-17b-16e-instruct`
  - Used for multimodal image analysis and medical consultation
  - Provides professional medical insights and recommendations

### Speech Recognition
- **OpenAI Whisper Large V3**: `whisper-large-v3`
  - High-accuracy speech-to-text transcription
  - Processes patient voice queries

### Text-to-Speech Services
- **Google Text-to-Speech (gTTS)**: Natural voice synthesis
- **ElevenLabs**: Premium AI voice generation with realistic speech patterns

### API Providers
- **GROQ**: High-performance inference for LLaMA models and Whisper
- **ElevenLabs**: Advanced text-to-speech API

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- FFmpeg (for audio processing)
- PortAudio (for microphone access)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ai-doctor.git
   cd ai-doctor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install system dependencies**
   
   **For Windows:**
   ```bash
   # Install FFmpeg and add to PATH
   ```
   
   **For macOS:**
   ```bash
   brew install ffmpeg portaudio
   ```
   
   **For Ubuntu/Debian:**
   ```bash
   sudo apt update
   sudo apt install ffmpeg portaudio19-dev
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ELEVEN_LABS_API_KEY=your_elevenlabs_api_key_here
   ```

### Required Python Packages

```txt
gradio
groq
python-dotenv
gtts
elevenlabs
speech-recognition
pydub
pillow
base64
```

## 🖥️ Usage

1. **Start the application**
   ```bash
   python gradio_app.py
   ```

2. **Access the web interface**
   - Open your browser and navigate to `http://127.0.0.1:7860/`

3. **Using the AI Doctor**
   - **Record Audio**: Click the microphone button and describe your medical concern
   - **Upload Image**: Upload a medical image (skin condition, X-ray, etc.)
   - **Get Diagnosis**: The AI will analyze both inputs and provide medical insights
   - **Listen to Response**: The diagnosis will be read aloud using AI voice synthesis

## 🔧 Core Components

### 1. Brain of the Doctor (`brain_of_the_doctor.py`)
- **Image Encoding**: Converts images to base64 format for API processing
- **Multimodal Analysis**: Uses LLaMA 4 Scout for combined text and image understanding
- **Medical Reasoning**: Provides differential diagnoses and treatment suggestions

### 2. Voice of the Patient (`voice_of_the_patient.py`)
- **Audio Recording**: Captures microphone input with ambient noise adjustment
- **Speech Transcription**: Converts audio to text using Whisper Large V3
- **Audio Processing**: Handles MP3 conversion and file management

### 3. Voice of the Doctor (`voice_of_the_doctor.py`)
- **Text-to-Speech Options**: 
  - gTTS for basic voice synthesis
  - ElevenLabs for premium, natural-sounding speech
- **Cross-Platform Audio**: Supports Windows, macOS, and Linux playback
- **Audio Format Conversion**: MP3 to WAV conversion for compatibility

### 4. Gradio Interface (`gradio_app.py`)
- **User Interface**: Clean, intuitive web interface
- **Input Handling**: Processes both audio and image inputs simultaneously
- **Response Display**: Shows transcription, diagnosis, and plays audio response

## 🎯 System Prompt & Behavior

The AI doctor is configured with a specialized system prompt that:
- Acts as a professional medical consultant
- Provides concise, direct medical advice
- Focuses on differential diagnoses and remedies
- Maintains a professional, empathetic tone
- Avoids AI-like responses and formatting

## ⚠️ Important Disclaimers

- **Educational Purpose Only**: This application is designed for learning and demonstration purposes
- **Not a Replacement for Medical Care**: Always consult with qualified healthcare professionals for medical concerns
- **No Medical Liability**: The AI's responses should not be considered professional medical advice

## 🔒 Privacy & Security

- **Local Processing**: Audio recording and processing happen locally
- **API Security**: Uses secure API keys for external services
- **No Data Storage**: Patient data is not permanently stored

## 🛠️ Customization

### Changing AI Models
- Modify the `model` variable in `brain_of_the_doctor.py`
- Update the `stt_model` in `voice_of_the_patient.py`

### Voice Customization
- Change the `voice_id` in `voice_of_the_doctor.py` for different ElevenLabs voices
- Adjust language settings in gTTS configuration

### System Prompt Modification
- Edit the `system_prompt` variable in `gradio_app.py` to change AI behavior

## 🐛 Troubleshooting

### Common Issues

1. **Microphone Not Working**
   - Check microphone permissions
   - Ensure PortAudio is properly installed

2. **API Errors**
   - Verify API keys in `.env` file
   - Check API quotas and limits

3. **Audio Playback Issues**
   - Install required audio codecs
   - Check system audio settings

### Error Logs
The application includes comprehensive logging for debugging issues.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Meta AI** for LLaMA 4 Scout model
- **OpenAI** for Whisper speech recognition
- **GROQ** for high-performance inference
- **ElevenLabs** for advanced text-to-speech
- **Gradio** for the intuitive web interface

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the troubleshooting section
2. Review existing GitHub issues
3. Create a new issue with detailed information

---

**⚠️ Medical Disclaimer**: This AI tool is for educational and informational purposes only. It is not intended to diagnose, treat, cure, or prevent any disease. Always seek the advice of qualified health providers with any questions you may have regarding a medical condition.
