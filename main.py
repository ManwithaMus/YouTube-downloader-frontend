import pytube
import tkinter

#  Used to test if the videos could be downloaded
#  URL = input("What is the Youtube URL of the video you wish to download!").strip()
def convert(URL):
    try:
        youtube = pytube.YouTube(URL)
        video = youtube.streams.first()
        video.download()
        print("Video is downloading...")
        print("It may take a while depending on the size")
        print()
    except Exception as e:
        print("___________________________")
        print(e)
        print("Video could not be loaded")
        print("Try using a different valid URL")
        print("___________________________")
        print()
def getText(self):
    URL = text.get("1.0", 'end-1c').strip()
    convert(URL)
    text.delete("1.0", 'end-1c')

window = tkinter.Tk()
#  window.geometry("1000x100")
window.iconbitmap('YuhFinal.ico')
window.title("YouTube to Mp4")
label_instruct = tkinter.Label(window, text="Enter a YouTube URL to download video!")
label = tkinter.Label(window, text="URL:")
text = tkinter.Text(window, width=100, height=1)
#  text = tkinter.Entry(window)
#  window.bind('<Return>')
label.grid(column=0, row=1)
text.grid(column=1, row=1)
label_instruct.grid(column=1, row=0)
window.bind('<Return>', getText)
window.mainloop()
