#Step1a: Setup Text to Speech TTS model with gTTS 
import os
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language="en"

    audioobj= gTTS(
        text=input_text,
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

input_text=" Hi! This is a medical chatbot."
#text_to_speech_with_gtts_old(input_text=input_text, output_filepath= "gtts_testing.mp3")

#Step1b: Setup Text to Speech TTS model with ElevenLabs


import os
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs import play

# Load environment variables
load_dotenv()
ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")

# Initialize the ElevenLabs client
client = ElevenLabs(api_key=ELEVEN_LABS_API_KEY)

def text_to_speech_with_elevenlabs_old(input_text, output_filepath=None):
    audio_generator = client.text_to_speech.convert(
        text=input_text,
        voice_id="9BWtsMINqrJLrRacOk9x",  # Replace with your own
        model_id="eleven_turbo_v2",
        output_format="mp3_44100_128"
    )

    if output_filepath:
        with open(output_filepath, "wb") as f:
            for chunk in audio_generator:
                if isinstance(chunk, bytes):
                    f.write(chunk)
    else:
        play(audio_generator)

# Example usage
#input_text = "Hello, how can I assist you today?"
#text_to_speech_with_elevenlabs_old(input_text, output_filepath="eleven_labs_testing.mp3")


#Step2: Use model for text output to Voice 

import os
import platform
import subprocess
from gtts import gTTS
from pydub import AudioSegment
from dotenv import load_dotenv

def text_to_speech_with_gtts(input_text, output_filepath_mp3):
    language = "en"
    tts = gTTS(text=input_text, lang=language, slow=False)
    tts.save(output_filepath_mp3)

    # Convert to WAV for Windows SoundPlayer compatibility
    wav_path = output_filepath_mp3.replace(".mp3", ".wav")
    sound = AudioSegment.from_mp3(output_filepath_mp3)
    sound.export(wav_path, format="wav")

    # Cross-platform playback
    os_name = platform.system()
    try:
        if os_name == "Darwin":
            subprocess.run(["afplay", wav_path])
        elif os_name == "Windows":
            subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_path}").PlaySync();'])
        elif os_name == "Linux":
            subprocess.run(["aplay", wav_path])
        else:
            raise OSError("Unsupported OS")
    except Exception as e:
        print(f"Playback error: {e}")

text_to_speech_with_gtts("Testing WAV conversion!", "gtts_testing_autoplay.mp3")


# Load your ElevenLabs API key
load_dotenv()
ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")
client = ElevenLabs(api_key=ELEVEN_LABS_API_KEY)

def text_to_speech_with_elevenlabs(input_text, output_filepath_mp3=None):
    audio_generator = client.text_to_speech.convert(
        text=input_text,
        voice_id="9BWtsMINqrJLrRacOk9x",  # Replace with your own
        model_id="eleven_turbo_v2",
        output_format="mp3_44100_128"
    )

    if output_filepath_mp3:
        # Save MP3
        with open(output_filepath_mp3, "wb") as f:
            for chunk in audio_generator:
                if isinstance(chunk, bytes):
                    f.write(chunk)

        # Convert MP3 to WAV
        wav_path = output_filepath_mp3.replace(".mp3", ".wav")
        try:
            sound = AudioSegment.from_mp3(output_filepath_mp3)
            sound.export(wav_path, format="wav")

            # Play the WAV file
            os_name = platform.system()
            if os_name == "Windows":
                subprocess.run(['powershell', '-c', f'(New-Object Media.SoundPlayer "{wav_path}").PlaySync();'])
            elif os_name == "Darwin":
                subprocess.run(['afplay', wav_path])
            elif os_name == "Linux":
                subprocess.run(['aplay', wav_path])
        except Exception as e:
            print(f"Error during conversion or playback: {e}")
    else:
        # Just stream and play
        play(audio_generator)
text_to_speech_with_elevenlabs("Hello! This is ElevenLabs speaking.", output_filepath_mp3="eleven_labs_test.mp3")
