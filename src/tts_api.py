import requests
import urllib.parse
import json

# TTS_IP = "192.168.1.8"
TTS_IP = "127.0.0.1"
TTS_PORT = "7851"

url = f"http://{TTS_IP}:{TTS_PORT}/api/tts-generate"

headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

def generatePodcastAudio(script, numberOfSpeakers, speaker1Gender, speaker2Gender="Male"):

    encoded_script = urllib.parse.quote(script)
    payload = f'text_input={encoded_script}'
    
    if(speaker1Gender == "Male"):
        payload += f"&character_voice_gen=male_01.wav"
    elif (speaker1Gender == "Female"):
        payload += f"&character_voice_gen=female_01.wav"
    else:
        #error
        print("Error: wrong speaker 1 gender")
    
    if (numberOfSpeakers == 1):
        payload += f"&narrator_enabled=false"
    elif(numberOfSpeakers == 2):
        payload += f"&narrator_enabled=true"

        if (speaker2Gender == "Male"):
            payload += f"&narrator_voice_gen=male_02.wav"
        elif (speaker2Gender == "Female"):
            payload += f"&narrator_voice_gen=female_02.wav"
        else:
            #error
            print("Error: wrong Speaker 2 gender")
    

    response = requests.request("POST", url, headers=headers, data=payload)
    response_json = json.loads(response.text)
    result = {
        "status": response_json["status"],
        "output_file_url": response_json["output_file_url"]
    }
    
    return result