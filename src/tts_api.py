import requests
import urllib.parse
import json

# TTS_IP = "192.168.1.8"
TTS_IP = "127.0.0.1"
TTS_PORT = "9000"

url = f"http://{TTS_IP}:{TTS_PORT}/generate-podcast"

headers = {
  'Content-Type': 'application/json'
}

def generatePodcastAudio(script, numberOfSpeakers, speaker1Gender, speaker2Gender="Male"):


    if numberOfSpeakers not in [1, 2]:
        return {
            "status": "error",
            "message": "Invalid number of speakers. Only 1 or 2 speakers are supported."
        }
    
    encoded_script = urllib.parse.quote(script)

    payload = {
        "podcastScript": encoded_script,
        "numberOfSpeakers": numberOfSpeakers,
        "speaker1Gender": speaker1Gender
    }

    if numberOfSpeakers == 2:
        payload["speaker2Gender"] = speaker2Gender

    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    result = {
        "status": response_json["status"],
        "output_file_url": response_json["output_file_url"]
    }
    
    return result

x= generatePodcastAudio("Hey pal! what is up", 1, "female")
print(x)

    # encoded_script = urllib.parse.quote(script)
    # payload = f'text_input={encoded_script}'
    
    # if(speaker1Gender == "Male"):
    #     payload += f"&character_voice_gen=male_01.wav"
    # elif (speaker1Gender == "Female"):
    #     payload += f"&character_voice_gen=female_01.wav"
    # else:
    #     #error
    #     print("Error: wrong speaker 1 gender")
    
    # if (numberOfSpeakers == 1):
    #     payload += f"&narrator_enabled=false"
    # elif(numberOfSpeakers == 2):
    #     payload += f"&narrator_enabled=true"

    #     if (speaker2Gender == "Male"):
    #         payload += f"&narrator_voice_gen=male_02.wav"
    #     elif (speaker2Gender == "Female"):
    #         payload += f"&narrator_voice_gen=female_02.wav"
    #     else:
    #         #error
    #         print("Error: wrong Speaker 2 gender")
    

    # response = requests.request("POST", url, headers=headers, data=payload)
    # response_json = json.loads(response.text)
    # result = {
    #     "status": response_json["status"],
    #     "output_file_url": response_json["output_file_url"]
    # }
    
    # return result