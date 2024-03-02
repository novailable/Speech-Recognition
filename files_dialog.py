from tkinter import Tk
from tkinter.filedialog import askopenfilenames
import os


class File_Open():
    def __init__(self):
        self.file_path_dicts = []
        self.root = Tk()
        self.root.withdraw()

    def file_list(self):

        file_paths = askopenfilenames(title="Open File")

        # Convert the result into a list of file paths
        file_paths = self.root.tk.splitlist(file_paths)
        __select_txt = "You have selected: "
        if len(file_paths) < 1:
            __select_txt += "nothing!"
        print(__select_txt)
        # Iterate over the selected file paths
        for file_path in file_paths:
            print(f"\t{file_path}")
            file_name = os.path.basename(file_path)
            file_no_ext, file_ext = os.path.splitext(file_name)
            file_size = os.path.getsize(file_path) / 1024
            # Create a dictionary for each file path and its corresponding parts
            file_dict = {
                "Path": file_path,
                "Name": file_name,
                "Ext": file_ext,
                "NoExt": file_no_ext,
                "Size": file_size
            }

            # Append the dictionary to the file_path_dicts
            self.file_path_dicts.append(file_dict)

        return self.file_path_dicts


if __name__ == '__main__':
    fileopen = File_Open()
    files = fileopen.file_list()
    print(files)
    for file_path in files:
        print(file_path["Path"])
