import speech_recognition as sr

def detect_wake_word_and_command():
    r = sr.Recognizer()
    wake_words = ["hey", "hello", "hi"]  # Define your wake words here

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        print("Listening...")

        while True:
            audio = r.listen(source)
            try:
                speech_text = r.recognize_google(audio).lower()
                for wake_word in wake_words:
                    if wake_word in speech_text:
                        print(f"Wake word detected. Full command: {speech_text}")
                        # Remove the wake word and return the rest of the command
                        command = speech_text.replace(wake_word, "").strip()
                        return command
            except sr.UnknownValueError:
                print("No speech recognized. Continuing to listen...")
            except sr.RequestError as e:
                print(f"Error: {e}")

    return "no_command"
