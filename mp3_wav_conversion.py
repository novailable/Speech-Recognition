from pydub import AudioSegment
import os


class MP3toWAVConverter:
    def __init__(self, mp3_path=None, ext=None, name=None):
        self.__mp3_path = mp3_path
        self.__ext = ext
        self.__name = name
        self.o_folder_name = None

    def convert(self):
        wav_path = None
        try:
            audio = AudioSegment.from_file(self.__mp3_path)
            print(f"\nConverting \"{self.__name}\" to wav...")
            wav_path = self.__mp3_path[:-len(self.__name)] + "output"
            # Create the output folder if it doesn't exist
            if not os.path.exists(wav_path):
                os.makedirs(wav_path)
            wav_path += "/" + self.__name[:-len(self.__ext)] + ".wav"  # Generate the output WAV file path
            audio.export(wav_path, format="wav")
            #file_size = os.path.getsize(wav_path) / 1024

        except Exception as e:
            print(f"\nThe selected file: {self.__mp3_path} is not audio file!")

        return wav_path
