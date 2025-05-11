import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()


def get_text_from_audio_file(file):
	try:
		audio_ex = speech_recognition.AudioFile(file)
		with audio_ex as source:
		    audiodata = recognizer.record(audio_ex)
		my_text = recognizer.recognize_google(audiodata,language='pt-BR')
		return my_text
	except speech_recognition.RequestError as e:
		print("could not request results: {0}".format(e))
		
	except speech_recognition.UnknownValueError as e:
		print("unknown error")

def output_text(text):
	f = open("output.txt","a")
	f.write(text)
	f.write("\n")
	return False
