import speech_recognition as sr
import pyttsx3
import json
import openai

openai.api_key = #input your openAI api Key here

r = sr.Recognizer()
 
def SpeakText(command):
     
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
     
     
while(1):   
    print("activated")
    try:
         
        with sr.Microphone() as source2:
             
            r.adjust_for_ambient_noise(source2, duration=0.2)
             
            audio2 = r.listen(source2)
             
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("input: " + MyText)

    
            response = openai.Completion.create(
                model=#openAI language model type here,
                prompt=str(MyText),
                temperature=2,
                max_tokens=200,
                top_p=0.5,
                frequency_penalty=0,
                presence_penalty=0.6,
                stop=[" Human:", " AI:"]
            )

            json_object = json.loads(str(response))
            a = json_object['choices'][0]['text']
 
            print("Response: ", a)
            SpeakText(a)
             
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
         
    except sr.UnknownValueError:
        print("unknown error occurred")
