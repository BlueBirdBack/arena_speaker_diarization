# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.

import os
from dotenv import load_dotenv
import assemblyai as aai

load_dotenv()
ASSEMBLY_API_KEY = os.getenv("ASSEMBLY_API_KEY")

# Replace with your API key
aai.settings.api_key = ASSEMBLY_API_KEY

# URL of the file to transcribe
FILE_URL = "https://github.com/AssemblyAI-Examples/audio-examples/raw/main/20230607_me_canadian_wildfires.mp3"

# You can also transcribe a local file by passing in a file path
# FILE_URL = './path/to/file.mp3'

config = aai.TranscriptionConfig(auto_highlights=True)

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(FILE_URL, config=config)

for result in transcript.auto_highlights.results:
    print(f"Highlight: {result.text}, Count: {result.count}, Rank: {result.rank}")

"""
Highlight: air quality alerts, Count: 1, Rank: 0.08
Highlight: wide ranging air quality consequences, Count: 1, Rank: 0.08
Highlight: systems change, Count: 1, Rank: 0.07
Highlight: more wildfires, Count: 1, Rank: 0.07
Highlight: air pollution, Count: 1, Rank: 0.07
Highlight: high levels, Count: 2, Rank: 0.06
Highlight: existing health conditions, Count: 1, Rank: 0.06
Highlight: climate change, Count: 3, Rank: 0.06
Highlight: New York City, Count: 1, Rank: 0.06
Highlight: respiratory conditions, Count: 1, Rank: 0.05
Highlight: New York, Count: 3, Rank: 0.05
Highlight: heart conditions, Count: 1, Rank: 0.05
Highlight: air quality warnings, Count: 1, Rank: 0.05
Highlight: Smoke, Count: 6, Rank: 0.05
Highlight: health problems, Count: 1, Rank: 0.05
"""
