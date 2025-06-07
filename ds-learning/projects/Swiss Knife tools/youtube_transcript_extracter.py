import re
from youtube_transcript_api import YouTubeTranscriptApi

youtube_url = "https://www.youtube.com/watch?v=mMrkbszl9Xo&t=190s&ab_channel=MoonDev"

# extract video ID with regex
video_id_regex = r'(?:v=|\/)([0-9A-Za-z_-]{11}).*'
match = re.search(video_id_regex, youtube_url)

if match:
    video_id = match.group(1)
else:
    None

transcript = YouTubeTranscriptApi.get_transcript(video_id)
# print(transcript)

# extract transcript
text_list = [transcript[i]['text'] for i in range(len(transcript))]
transcript_text = '\n'.join(text_list)
# print(transcript_text)
text_file = open("/Users/pulin05/ds-learn-git-hub/ds-learn-hub/ds-learning/Python Output/Output.txt", "w")
text_file.write(transcript_text)
text_file.close()