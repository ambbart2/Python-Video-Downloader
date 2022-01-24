from pytube import YouTube
from pytube import exceptions
from pathlib import Path
from tkinter import *
import tkinter as tk

# Where to save file
SAVE_PATH = str(Path.home()) + "/Downloads"

# Create UI to enter url for download
ui = tk.Tk()
ui.geometry('600x400')
ui.resizable()
ui.title("YouTube Video Downloader")
Label(ui, text='Youtube Video Downloader', font='arial 22 bold').pack()

# Create field to enter link
link = StringVar()
lbl_instruction = Label(ui, text='Enter video url:', font='arial 16 bold')
lbl_instruction.pack(pady=35)
link_enter = Entry(ui, width=60, textvariable=link)
link_enter.pack()

# Create status label
lbl_status = Label(ui, text='Status: ', font='arial 15')
lbl_status.pack(pady=20)

# Create menu for right click
m = Menu(ui, tearoff=0)
m.add_command(label="Cut")
m.add_command(label="Copy")
m.add_command(label="Paste")
m.add_separator()


# function to handle right click
def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()


link_enter.bind("<Button-2>", do_popup)


# function to download pasted url
def download_video():
    lbl_status.config(text='Status: DOWNLOADING..')

    try:
        url = YouTube(str(link.get()))
        print("Found Video: {}".format(url.title))
        # ys = url.streams.get_highest_resolution()
        ys = url.streams.first()
        ys.download(SAVE_PATH)
        lbl_status.config(text='Status: DOWNLOAD COMPLETE')
    except exceptions.RegexMatchError:
        print('The Regex pattern did not return any matches for the video: {}'.format(link.get()))
        lbl_status.config(text='Status: Regex Error')

    except exceptions.ExtractError:
        print('An extraction error occurred for the video: {}'.format(link.get()))
        lbl_status.config(text='Status: Extraction Error')

    except exceptions.VideoUnavailable:
        print('The following video is unavailable: {}'.format(link.get()))
        lbl_status.config(text='Status: Video Unavailable')


# function to display info for video from url
def show_info():
    url = YouTube(str(link.get()))
    print("Title: {}".format(url.title))


# function to stream audio from video
def stream_audio():
    url = YouTube(str(link.get()))


frame = tk.Frame(width=250, height=40, master=ui, relief=tk.RAISED, borderwidth=0)

# Create download button and video info button
btn_download = tk.Button(master=frame, text='DOWNLOAD', font='arial 15 bold', bg='pale violet red', padx=2,
                         command=download_video)
btn_info = tk.Button(master=frame, text='Get Video Info', font='arial 15 bold', bg='pale violet red', padx=2,
                     command=show_info)
btn_stream = tk.Button(master=frame, text='Stream Audio', font='arial 15 bold', bg='pale violet red', padx=2,
                       command=stream_audio)
btn_download.pack(padx=5, side="left")
btn_info.pack(side="left")
btn_stream.pack(padx=5, side="left")
frame.pack(side="top")

ui.mainloop()
