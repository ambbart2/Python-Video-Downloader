from pytube import YouTube
from pytube import exceptions
from pathlib import Path
from tkinter import *

# Where to save file
SAVE_PATH = str(Path.home()) + "/Downloads"

# Create UI to enter url for download
ui = Tk()
ui.geometry('600x400')
ui.resizable()
ui.title("YouTube Video Downloader")
Label(ui, text='Youtube Video Downloader', font='arial 22 bold').pack()

# Create field to enter link
link = StringVar()
instruction = Label(ui, text='Enter video url:', font='arial 16 bold')
instruction.pack(pady=35)
link_enter = Entry(ui, width=60, textvariable=link)
link_enter.pack()

# Create status label
status_label = Label(ui, text='Status: ', font='arial 15')
status_label.pack(pady=20)


# function to download pasted url
def download_video():
    status_label.config(text='Status: DOWNLOADING..')

    try:
        url = YouTube(str(link.get()))
        print("Found Video: {}".format(url.title))
        # ys = url.streams.get_highest_resolution()
        ys = url.streams.first()
        ys.download(SAVE_PATH)
        status_label.config(text='Status: DOWNLOAD COMPLETE')
    except exceptions.RegexMatchError:
        print('The Regex pattern did not return any matches for the video: {}'.format(link.get()))
        status_label.config(text='Status: Regex Error')

    except exceptions.ExtractError:
        print('An extraction error occurred for the video: {}'.format(link.get()))
        status_label.config(text='Status: Extraction Error')

    except exceptions.VideoUnavailable:
        print('The following video is unavailable: {}'.format(link.get()))
        status_label.config(text='Status: Video Unavailable')


# Create download button
download_button = Button(ui, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2,
                         command=download_video)
download_button.pack(pady=30)

ui.mainloop()
