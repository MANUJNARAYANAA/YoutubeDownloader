from tkinter import *
from tkinter import ttk 
from tkinter import filedialog
from pytube import YouTube

foldername=""

def openDirectory():
    global foldername
    foldername=filedialog.askdirectory()
    if(len(foldername)>1):
     saveentryerr.config(text=foldername,fg="blue")
    else:
     saveentryerr.config(text="Please choose a folder to continue",fg="red")

def ytdwn():
    choice=qualitycombo.get()
    video=ytentry.get()
    if(len(video)>1):
     ytentryerr.config(text="")
     print(video,"is at",foldername)
     yt=YouTube(video)
     print("Video name is:\n\n",yt.title)

     if(choice==dwnchoice[0]):
       print("Video of mp4_720p is being downloaded...")
       loadlbl.config(text="Video of mp4_720 is being downloaded")
       selection=yt.streams.filter(progressive=True).first()
     elif(choice==dwnchoice[1]):
       print("Video of mp4_144p is being downloaded...")
       loadlbl.config(text="Video of mp4_144 is being downloaded")
       selection=yt.streams.filter(progressive=True,file_extension="mp4").last()
     elif(choice==dwnchoice[2]):
       print("mp3 file is being downloaded...")
       loadlbl.config(text="mp3 file is being downloaded")
       selection=yt.streams.filter(only_audio=True).first()

     selection.download(foldername)
     complete()  
    else:
     ytentryerr.config(text="Please enter an URL to continue",fg="red")
         

def complete():
    loadlbl.config(text="Download Completed")
     
root=Tk()
root.title('YTDownloader')
root.grid_columnconfigure(0,weight=1)
ytlinklabel=Label(root,text="Enter YouTube URL:")
ytlinklabel.grid()

ytentryvar=StringVar()
ytentry=Entry(root,width=50,textvariable=ytentryvar)
ytentry.grid(padx=(20,20),pady=(20,20))

ytentryerr=Label(root,text="")
ytentryerr.grid(pady=(0,20))


loclabel=Label(root,text=("Enter download location"))
loclabel.grid(pady=(0,20))


saveentry=Button(root,text=("Choose Folder"),command=openDirectory)
saveentry.grid(pady=(10,20))

saveentryerr=Label(root,text="")
saveentryerr.grid(pady=(0,10))

qualitychoice=Label(root,text="Choose the file quality")
qualitychoice.grid(pady=(0,20))

dwnchoice=["mp4_720p","mp4_144p","mp3"]

qualitycombo=ttk.Combobox(root,values=dwnchoice)
qualitycombo.grid(pady=(0,20))

dwnbtn=Button(root,text="Download",command=ytdwn)
dwnbtn.grid(pady=(10,20))

loadlbl=ttk.Label(root,text="-Developed by Manuj-")
loadlbl.grid(pady=(0,20))

root.mainloop()
