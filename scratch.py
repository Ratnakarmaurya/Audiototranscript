from docx import Document
import os.path
import os
import speech_recognition as sr
import math
from tkinter import *
from tkinter import filedialog
from pydub import AudioSegment
filepath= os.path.join(os.path.expanduser('~'),'Documents')
app = Tk()
class BrowseButton:
    def __init__(self,master):
        self.frame = Frame(master)
        self.frame.pack()

        self.browseButton = Button(self.frame,text="Browse",command=self.browseFile)
        self.browseButton.pack()

        self.enterName=Label(self.frame,text="What Do you Want the name to Be?")
        self.enterName.pack()

        self.textBox=Entry(self.frame,text=("Enter the name here"))
        self.textBox.pack()

        self.convertButton = Button(self.frame, text="Convert", command=self.conversion)
        self.convertButton.pack()

        self.openFileLocation=Button(self.frame,text ="Open Location",command=self.openLocation)
        self.openFileLocation.pack()











    def browseFile(self): #used to get destination of desired file

        self.filename=filedialog.askopenfilename \
            (initialdir = "/",title = "Select file",
             filetypes = [("Wav files", "*.wav"),("Mp3 files","*.mp3"),("Aac files","*.aac"),("all files","*.*")])

    # def transcript(self):
    #     pass
    #     with open ("hey.docx", "r")as self.trans:
    #         self.contents=self.trans.read()
    #         print(self.contents)

    def openLocation(self):

        # print(self.completeName)
        # print(self.autoOpenName)
        pass
        print("path" + self.incompleteName + self.getname)
        self.location=filedialog.askopenfile(initialdir=self.incompleteName,filetypes=[("Document","*.docx")])
        # open(self.location,"r")
        os.startfile(self.completeName)
        print(self.incompleteName + self.getname)
        print(self.location)




    def conversion(self):
        self.rawfile = self.filename
        self.wavfile = "tempo.wav"
        if self.rawfile[-3:] == "mp3":
            # converting mp3 to wac now
            self.sound = AudioSegment.from_file(self.rawfile, format="mp3")
        elif self.rawfile[-3:] == 'wav':
            self.sound = AudioSegment.from_file(self.rawfile, format="wav")
        elif self.rawfile[-3:] == "aac":
            self.sound = AudioSegment.from_file(self.rawfile, format="aac")
        self.sound.export(self.wavfile, format="wav")
        self.getname = self.textBox.get()
        self.finalname = self.getname + ".docx"
        self.incompleteName = os.path.join(os.path.expanduser('~') )

        # if not os.path.exists(self.incompleteName):
        #     os.makedirs(self.incompleteName)
        # else:
        #     pass

        self.completeName = os.path.join(os.path.expanduser('~'), self.finalname)
        self.autoOpenName=os.path.normcase(self.completeName)


        # dur = duration pydub counts the duration in millisecond so dividing it by 100
        self.dur = len(self.sound) / 1000
        # seg aka segments distritutes or in simple words splits the audio in several segments
        self.seg = self.dur / 60
        # modf method seprates decimal we will use this later
        self.modfofdur = math.modf(self.dur)
        self.modfofseg = math.modf(self.seg)

        self.li = []  # making list
        if len(self.sound) > 60000:
            range(int(self.modfofseg[1]))
            for i in range(int(self.modfofseg[1])):
                if i == int(self.modfofseg[1] - 1):
                    round(self.modfofdur[0], 2)
                    self.seconds = 60 + (self.modfofdur[0] * 100)  # this will add remaining seconds to the last element of li list (will always be 60+)
                    self.li.append(self.seconds)
                else:
                    self.li.append(60)
        elif len(self.sound) <= 60000:
            self.li.append(self.modfofdur[1])

        self.r = sr.Recognizer()
        if self.rawfile[-1] != "v":
            self.sampleaudio = sr.AudioFile(self.wavfile)
        else:
            self.sampleaudio = sr.AudioFile(self.rawfile)
        self.document = Document()
        self.document.save(self.completeName)
        with self.sampleaudio as self.source:
            for self.sec in self.li:
                self.audio = self.r.record(self.source, offset=0, duration=self.sec)
                self.r.recognize_google(self.audio)
                with open(self.completeName, 'a') as self.appenddocx:
                    self.document.add_paragraph(self.r.recognize_google(self.audio), style='Intense Quote')
                    #             document.add_page_break()
                    self.document.save(self.completeName)









b=BrowseButton(app)


app.mainloop()




