# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users might need to use `pip3` instead of `pip`.

import os
from dotenv import load_dotenv
import assemblyai as aai

load_dotenv()
ASSEMBLY_API_KEY = os.getenv("ASSEMBLY_API_KEY")

# Replace with your API key
aai.settings.api_key = ASSEMBLY_API_KEY

transcriber = aai.Transcriber()

audio_url = (
    "https://storage.googleapis.com/aai-web-samples/5_common_sports_injuries.mp3"
)

transcript = transcriber.transcribe(audio_url)

prompt = "Provide a brief summary of the transcript."

result = transcript.lemur.task(prompt)

print(result.response)
"""
 The transcript describes common sports injuries to the knee, ankle, shoulder, and ACL. It provides definitions, causes, 
and symptoms for runner's knee, sprained ankle, meniscus tear, rotator cuff tear, and ACL tear. The transcript seems to be narrating sports footage and explaining the injuries as they occur to the athletes. Overall, it provides an overview of several common sports-related injuries.
"""
