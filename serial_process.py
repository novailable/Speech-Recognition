import speech_recognition as sr
import time
from files_dialog import File_Open
from mp3_wav_conversion import MP3toWAVConverter


def speech_recog(audio_file_path):
    s_time = time.time()
    r = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        print(f"\tProcessing...")
        audio = r.record(source)

    try:
        print("\tRecognizing...")

        # Use Google Speech Recognition to convert speech to text
        txt = r.recognize_google(audio)
        print(f"\tTranscript: {txt}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand audio.")
    except sr.RequestError:
        print("Sorry, my speech recognition service is currently unavailable.")
    d_time = time.time()
    print(f"\nProcessing time : {d_time - s_time} seconds")


def main():
    files = File_Open().file_list()
    correct_files = []
    for audio_dict in files:
        audio_ext = audio_dict["Ext"]
        audio_path = audio_dict["Path"]
        audio_name = audio_dict["Name"]
        if audio_ext not in (".wav", ".flac"):
            audio_path = MP3toWAVConverter(audio_path, audio_ext, audio_name).convert()
        if audio_path:
            correct_files.append((audio_path, audio_name))

    s_time = time.time()
    for c_file in correct_files:
        print(f"\nTranscription for \"{c_file[1]}\"")
        speech_recog(c_file[0])
    print(f"\nTotal processing time: {time.time() - s_time} second")


if __name__ == '__main__':
    main()
