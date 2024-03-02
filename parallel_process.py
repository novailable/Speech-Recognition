import speech_recognition as sr
import multiprocessing
import time
from files_dialog import File_Open
from mp3_wav_conversion import MP3toWAVConverter


# Function to process a segment of audio and return the transcribed text

def audio_to_segment(audio_path):
    audio_recog = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        print("\n\tProcessing audio...")
        audio = audio_recog.record(source)
        sample_rate = audio.sample_rate
        sample_width = audio.sample_width

    num_cores = multiprocessing.cpu_count()
    print(f"\tNumber of CPU cores: {num_cores}")

    # Calculate the segment size based on the number of CPU cores
    segment_samples = int(len(audio.frame_data) / num_cores)

    print("\tDividing audio into segments...")
    # Split the audio into segments
    segments = []
    for i in range(0, len(audio.frame_data), segment_samples):
        segment = audio.frame_data[i:i + segment_samples]
        segments.append(segment)

    return segments, sample_rate, sample_width


def tscript_segment(segment, sample_rate, sample_width):
    segment_recog = sr.Recognizer()
    audio_segment = sr.AudioData(segment, sample_rate=sample_rate, sample_width=sample_width)
    try:
        transcript = segment_recog.recognize_google(audio_segment)  # Perform speech recognition
        return transcript
    except sr.UnknownValueError:
        print("Sorry, I could not understand audio.")
    except sr.RequestError:
        print("Sorry, my speech recognition service is currently unavailable.")


def tscript_audio(audio_file_path, audio_name):
    s_time = time.time()
    audio_recog = sr.Recognizer()
    #txt = f"\n\tTranscript of \"{audio_name}\": "

    with sr.AudioFile(audio_file_path) as source:
        print(f"\tProcessing \"{audio_name}\"...\n")
        audio = audio_recog.record(source)

    try:
        # Use Google Speech Recognition to convert speech to text

        txt = audio_recog.recognize_google(audio)
        print(f"\tTranscript of \"{audio_name}\": {txt}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand audio.")
    except sr.RequestError:
        print("Sorry, my speech recognition service is currently unavailable.")
    d_time = time.time()
    print(f"Processing time : {d_time - s_time} seconds\n")

    #return txt

def mprocess_segment(audio_segments, sample_rate, sample_width):

    pool = multiprocessing.Pool()
    s_time = time.time()
    results = pool.starmap(tscript_segment, [(segment, sample_rate, sample_width) for segment in audio_segments])
    d_time = time.time()
    pool.close()
    pool.join()
    # Print the transcriptions
    print("\tTranscript:")
    for i, result in enumerate(results):
        print(f"\tSegment {i + 1}: {result}\n")

    print(f"\nProcessing time: {d_time - s_time} seconds")


def mprocess_audio(audio_list):

    pool = multiprocessing.Pool()
    s_time = time.time()
    results = pool.starmap(tscript_audio, audio_list)
    d_time = time.time()
    pool.close()
    pool.join()
    #for result in results:
        #print(result)
    print(f"\nTotal processing time: {d_time - s_time} seconds")


def main():
    files = File_Open().file_list()
    multi_files = []
    for audio_dict in files:
        audio_ext = audio_dict["Ext"]
        audio_path = audio_dict["Path"]
        audio_name = audio_dict["Name"]
        if audio_ext not in (".wav", ".flac"):
            audio_path = MP3toWAVConverter(audio_path, audio_ext, audio_name).convert()
        if audio_path is not None:
            if len(files) == 1:
                print(f"\nTranscription for \"{audio_name}\"")
                audio_segments, sample_rate, sample_width = audio_to_segment(audio_path)
                print("\tRecognition...")
                mprocess_segment(audio_segments, sample_rate, sample_width)
            else:
                multi_files.append((audio_path, audio_name))
    if multi_files:
        print()
        mprocess_audio(multi_files)


if __name__ == '__main__':
    main()
