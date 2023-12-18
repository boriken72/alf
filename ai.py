import pyttsx3
import speech_recognition as sr

# run pip install google-cloud-speech
GOOGLE_CLOUD_SPEECH_CREDENTIALS = "google-credentials.json"

class AI():
    __name = ""
    __skill = []
    
    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)
        name = voices[0].name
        print(name)
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
        
        if name is not None:
            self.__name = name
        
        print("Listening")
        with self.m as source:
            self.r.adjust_for_ambient_noise(source, duration = 5)
            # self.r.pause_threshold = 2
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        sentence = "Hello, my name is" + self.__name
        self.__name = value
        self.engine.say(sentence)
        self.engine.runAndWait()
    
    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()
        
    def listen(self):
        print('Say Something')
        with self.m as source:
            audio = self.r.listen(source)
        print("Got it")
        
        try:
            phrase = self.r.recognize_google_cloud(audio, language='en-US', credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
            sentence = "Got it, you said" + phrase
            self.engine.say(sentence)
            self.engine.runAndWait()
            
        except Exception as error:
            print(f"Sorry didn't catch that", error)
            self.engine.say("Sorry I didn't catch that")
            self.engine.runAndWait()
        
        print(f"You said {phrase}")
        return phrase
                        
