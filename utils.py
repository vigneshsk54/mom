import speech_recognition as sr;
from pydub import AudioSegment;

from utils.constants import mom_prompt


def split_file_by_lines(file_path, lines_per_chunk):
    question = mom_prompt;
    with open(file_path, 'r') as file:
        chunk = []
        if(question != None):
            chunk.append((question))
            question = None;
        for i, line in enumerate(file, start=1):
            chunk.append(line)
            if i % lines_per_chunk == 0:
                yield chunk
                chunk = []
        if chunk:
            yield chunk  # For the remaining lines

def write_to_file(response, file_name):
    """Write chunks of data to a specified file."""
    with open(file_name, 'w') as file:
        file.write(response+"\n")


def convert_m4a_to_wav(m4a_file, wav_file):
    """Convert M4A file to WAV format."""
    audio = AudioSegment.from_file(m4a_file, format="m4a")
    audio.export(wav_file, format="wav")


def transcribe_audio(wav_file):
    """Transcribe audio from a WAV file to text."""
    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_file) as source:
        audio_data = recognizer.record(source)  # Read the entire audio file
        try:
            text = recognizer.recognize_google(audio_data)  # Use Google Web Speech API
            return text
        except sr.UnknownValueError:
            return "Google Speech Recognition could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results from Google Speech Recognition service; {e}"


# from pydub import AudioSegment
# import speech_recognition as sr
#
# def transcribe_audio(wav_file, chunk_length_ms=10000):
#     """
#     Transcribes audio from a WAV file to text, splitting it into chunks.
#
#     Args:
#         wav_file: Path to the WAV file.
#         chunk_length_ms: Length of each audio chunk in milliseconds.
#
#     Returns:
#         A list of transcribed text chunks.
#     """
#
#     audio = AudioSegment.from_wav(wav_file)
#     chunks = []
#     for i in range(0, len(audio), chunk_length_ms):
#         chunk = audio[i:i+chunk_length_ms]
#         chunks.append(chunk)
#
#     transcriptions = []
#     recognizer = sr.Recognizer()
#     for i, chunk in enumerate(chunks):
#         chunk.export(f"chunk_{i}.wav", format="wav")
#         with sr.AudioFile(f"chunk_{i}.wav") as source:
#             audio_data = recognizer.record(source)
#             try:
#                 text = recognizer.recognize_google(audio_data)
#                 transcriptions.append(text)
#             except sr.UnknownValueError:
#                 transcriptions.append(f"Could not understand audio chunk {i}")
#             except sr.RequestError as e:
#                 transcriptions.append(f"Error processing audio chunk {i}: {e}")
#
#     return transcriptions