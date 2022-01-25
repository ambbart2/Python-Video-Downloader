from pytube import YouTube
from pytube import exceptions
from pathlib import Path
from tkinter import *
import tkinter as tk
import pyperclip

# Where to save file
SAVE_PATH = str(Path.home()) + "/Downloads"

# Create UI to enter url for download
ui = tk.Tk()
ui.geometry('600x400')
ui.resizable()
ui.title("YouTube Video Downloader")
Label(ui, text='Youtube Video Downloader', font='arial 22 bold').pack()

# Declare text variables
link = StringVar()
status = StringVar()
info = StringVar()

# Create field to enter link
lbl_instruction = Label(ui, text='Enter video url:', font='arial 16 bold')
lbl_instruction.pack(pady=35)
link_enter = Entry(ui, width=60, textvariable=link)
link_enter.pack()

# Create status label
lbl_status = Label(ui, textvariable=status, text='Status: ', font='arial 15')
lbl_status.pack(pady=20)


# function to handle right click
def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()


# function to download pasted url
def download_video():
    try:
        url = YouTube(str(link.get()))
        status.set("Downloading..")
        ui.update_idletasks()
        print("Found Video: {}".format(url.title))
        ys = url.streams.get_highest_resolution()
        ys.download(SAVE_PATH)
        status.set("Download Complete")
        print("Video Downloaded and saved to {}".format(SAVE_PATH))
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
    try:
        url = YouTube(str(link.get()))
        info.set("Title: {}\nViews: {}    Length: {}".format(url.title, url.views, url.length))
    except exceptions.RegexMatchError:
        print('The Regex pattern did not return any matches for the video: {}'.format(link.get()))
        lbl_status.config(text='Status: Regex Error')

    except exceptions.ExtractError:
        print('An extraction error occurred for the video: {}'.format(link.get()))
        lbl_status.config(text='Status: Extraction Error')

    except exceptions.VideoUnavailable:
        print('The following video is unavailable: {}'.format(link.get()))
        lbl_status.config(text='Status: Video Unavailable')


# function to stream audio from video
def stream_audio():
    url = YouTube(str(link.get()))


# function to cut text from link_enter field
def cut_link_enter():
    pyperclip.copy(str(link.get()))
    link.set('')


# function to copy text from link_enter field
def copy_link_enter():
    pyperclip.copy(str(link.get()))


# function to paste text into link_enter field
def paste_link_enter():
    link.set(link.get() + pyperclip.paste())


# Add right click function for mac and windows
link_enter.bind("<Button-2>", do_popup)
link_enter.bind("<Button-3>", do_popup)

# Create menu for right click
m = Menu(ui, tearoff=0)
m.add_command(label="Cut", command=cut_link_enter)
m.add_command(label="Copy", command=copy_link_enter)
m.add_command(label="Paste", command=paste_link_enter)

# Create frame that contains buttons
frame = tk.Frame(width=250, height=30, master=ui, relief=tk.RAISED, borderwidth=0)

# Create buttons
btn_download = tk.Button(master=frame, text='DOWNLOAD', font='arial 15 bold', bg='light green', padx=2,
                         command=download_video)
btn_info = tk.Button(master=frame, text='Get Video Info', font='arial 15 bold', bg='light green', padx=2,
                     command=show_info)
btn_stream = tk.Button(master=frame, text='Stream Audio', font='arial 15 bold', bg='light green', padx=2,
                       command=stream_audio)
btn_download.pack(padx=5, side="left")
btn_info.pack(side="left")
btn_stream.pack(padx=5, side="left")
frame.pack(side="top")

# Create field for video info
lbl_status = Label(ui, textvariable=info, font='arial 13')
lbl_status.pack(pady=25)

ui.mainloop()
