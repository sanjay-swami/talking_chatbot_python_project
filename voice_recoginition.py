import speech_recognition as sr

def recognize_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening !!!!")

        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print(text)
            return text
        except sr.UnknownValueError:
            print("could not understand your voice")
        except Exception as e:
            print(e) 