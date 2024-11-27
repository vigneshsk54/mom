model_config = {
  "temperature": 1,
  "top_p": 0.99,
  "top_k": 0,
  "max_output_tokens": 4096,
}

# Paths for your files
m4a_file = "/Users/vigneshkumar/Documents/gen_ai/MOM/files/meet_audio.m4a"

wav_file = "/Users/vigneshkumar/Documents/gen_ai/MOM/files/meet_audio.wav"


mom_prompt = """
    1. You are the scrum master and you need to identify and send the details for the below questions
    2. Create minutes of the meeting based on the below context in a concise way?
    3. Create action items based on the below context before the next call?
    """