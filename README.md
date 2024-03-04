# Design & Implementation
## Development Tools
Programming Language: Python is a popular choice for its simplicity, readability, and large community support. It offers cross-platform compatibility and has extensive libraries available, making it versatile for various purposes (TechVidvan Team, 2019).
Integrated Development Environment (IDE): PyCharm is a widely used IDE for Python development. It provides Python-specific features, has a user-friendly interface, and offers extensibility through a plugin ecosystem. It includes intelligent refactoring capabilities and integrates well with version control systems. Strong community support and student license availability make it a favorable choice (alexandre, 2023).

Choices of package

  - PyDub: PyDub is a package used for audio file handling, format conversion, and sound segmentation. By installing this package, I gain access to functionality that allows me to manage audio files, such as segmentation and conversion of different audio formats (Robert, 2021). 
  - SpeechRecognition: This package provides multiple APIs for speech recognition tasks. It offers easy input methods and error handling features, making speech recognition easy to incorporate. It allows me to access various APIs from simple coding instead of diving in, as well as language module defaulting to English (Zhang, 2023).
  - Multiprocessing: I used this built-in module for parallel execution, task separation, and efficient CPU utilization. It enables tasks to leverage multiple CPU cores for concurrent processing, potentially improving performance. In my program, this is applied to checking the file whether it is in readable format as well as transcription (Python, n.d.).
  - OS: The built-in OS module in Python provides functions for file and directory operations as well as path manipulation. This module handles input from the file, directory manipulation, and creating new file paths for output audio files (Python, 2019).
  - Tkinter: The standard Python library for creating graphical user interfaces (GUIs). In this program, I used it for features such as file dialogs and directory selection, to emphasize user interaction for audio inputs (Python, n.d.). 
  - Time: The built-in time module in Python allows you to capture execution time, measure performance, or introduce delays in your program. It offers functions to work with time-related operations and can be handy for various timing-related tasks (Programiz, n.d.).

## Flow Charts

To effectively design and implement the coding structure that can be used as the backbone of the program, a flowchart is a must.

![serial drawio](https://github.com/novailable/Speech-Recognition/assets/97833342/8b01fd55-f3cc-4a9f-93db-f5c047f94d74)

Upon starting the program, the user is prompted to input files. At this stage, the user can select a single or multiple files. Check whether the file has the correct audio extension. If it does not, it will transform into the ".wav" extension which is needed for speech transcription. If the conversion process fails, the system will show the selected item is not audio. If it succeeds, the program generates a file with the extension of ".wav" inside the output folder which will be created under the same directory of user selected file path. Following that, the audio will be converted into text. The result will be printed out in the IDE console as text. Finally, the whole process will be looped depending on the number of files selected. From the above explanation, this is a very typical serial computing process.

![parallel drawio](https://github.com/novailable/Speech-Recognition/assets/97833342/2436c1ba-1b1e-4f14-aed6-4d60c6ede6c3)

The files list encounters the file checking process first, followed by the conversion of the audio files into the correct format. However, in the process of converting non-transcript able files, they will return as null value types due to multiprocessing. Before moving on to scripting, I filter out those items. During the scripting step, all audio files will be integrated with Google API at the same time. After that the results will be sorted based on the size and complexity of the file. The smallest one will be the first to be printed. Unlike the serial process, all the processes like file validation, audio conversion, transcription undergo multiple processing. This means there is no additional looping except for the audio conversion where I must filter out the null item from the list.

## Evaluation

There are many ways to evaluate speech recognition programs' performance. Measurements include accuracy, processing time, resource utilization, language support, error handling, and robustness. Also, parallel computing performance is determined by speedup, scalability, efficiency, load balancing, etc. For parallel computing, I will use speed up to measure its performance in this case. However, since the program uses the Google API inside the SpeechRecognition package, I must consider network connectivity, audio file size as well as API limits.

Hardware Configuration
```
Dell Inspiron 5567
  - OS: Windows 10 Pro 64-bit
  - CPU: Intel® Core™ i7, 7500U @ 2.70 GHz
  - Logical Processor: 
  - Cores: 2
  - Memory: 8 GB 
```
```
MacBook Air
  - OS: macOS Ventura version 13.4
  - CPU: Apple M2 chip @ 3.49 GHz
  - Efficiency Core: 4
  - Performance Core: 4
  - Memory: 8 GB
```

There is no question that the MacBook Air has higher performance than the Dell because it has 8 CPUs while the Dell has 4 CPUs

### Test Data

<img width="700" alt="image" src="https://github.com/novailable/Speech-Recognition/assets/97833342/7f78a934-c999-40a4-be78-7b4e1f60c36f">

In above table, you will find the details of audio files containing speeches in various formats, durations, and file sizes.

<img width="600" alt="image" src="https://github.com/novailable/Speech-Recognition/assets/97833342/50733577-151c-4990-923f-d9b926d2adc1">

The second table describes which audio I chose to test, and the file size inside the table is the size after “.wav” conversion. The main reason I chose 3, 5, 7 files with different sizes and durations is to show the time difference and process performed based on the number of files.

### Result

<img width="600" alt="image" src="https://github.com/novailable/Speech-Recognition/assets/97833342/db946014-ebae-4aeb-904e-fe4bca154bfc">

Table 3 shows the average execution time I got from running serial and parallel processes of the program. Number of times to get the average time is 3.

<img width="600" alt="image" src="https://github.com/novailable/Speech-Recognition/assets/97833342/dd36cf20-94e7-4a0c-9521-33447eccc4b5">

<img width="600" alt="image" src="https://github.com/novailable/Speech-Recognition/assets/97833342/ae3caf45-ddb5-440a-80ea-eeb6ad7eddb7">

These are the test result of serial & parallel computing on Dell Inspiron 5567 and MacBook. The X-axis is for the number of files examined while the Y-axis is the average execution time of the program in seconds. These indicate that testing 3 files produced a minor difference, but things appear to be different in 5 files. Finally, the results of testing 7 files clearly show that parallel computing has a higher potential for larger files. As a result of the different CPU counts, all MacBook testing times are shorter than Dell testing times. Additionally, the execution time for Dell and MacBook serialize 7 files differently.



