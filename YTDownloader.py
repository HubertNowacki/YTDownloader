from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry("500x300")
root.resizable(0, 0)
root.title("Pobieracz z YouTuba bez zadnych reklam")
Label(root, text="YTDownloader", font='aerial 20 bold').pack()

link = StringVar()

Label(root, text="Tutaj wklejasz linkacza", font='aerial 15 bold').place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)


def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text="POBRANED WARIATUNCIO", font="arial 15").place(x=180, y=210)


Button(root, text="POBIERZ DZIADA!", font='arial 15 bold', bg='purple', padx=2, command=downloader).place(x=180, y=150)
root.mainloop()
