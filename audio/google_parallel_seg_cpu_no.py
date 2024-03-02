import speech_recognition as sr
import multiprocessing

# Function to process a segment of audio and return the transcribed text
def process_segment(segment, sample_rate):
    recognizer = sr.Recognizer()
    segment_audio = sr.AudioData(segment, sample_rate=sample_rate, sample_width=2)

    try:
        transcript = recognizer.recognize_google(segment_audio)  # Perform speech recognition
        return transcript
    except sr.UnknownValueError:
        return "Unable to transcribe segment"
    except sr.RequestError as e:
        return f"Error occurred during transcription: {str(e)}"

if __name__ == '__main__':
    audio_file = 'Windswept.wav'  # Replace with the path to your audio file

    # Read the audio file
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
        sample_rate = audio.sample_rate

    # Determine the number of CPU cores available
    num_cores = multiprocessing.cpu_count()

    # Calculate the segment size based on the number of CPU cores
    segment_samples = int(len(audio.frame_data) / num_cores)

    # Split the audio into segments
    segments = []
    for i in range(0, len(audio.frame_data), segment_samples):
        segment = audio.frame_data[i:i + segment_samples]
        segments.append(segment)

    # Process segments in parallel
    pool = multiprocessing.Pool()
    results = pool.starmap(process_segment, [(segment, sample_rate) for segment in segments])
    pool.close()
    pool.join()

    # Print the transcriptions
    for i, result in enumerate(results):
        print(f"Segment {i}: {result}")
