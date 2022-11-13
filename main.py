from tkinter import *
import pathlib
from NewTape import NewTape
from Tapes import Tapes
import pygame


global pathing, open, i
open = True
i = -1

pathing = str(pathlib.Path(__file__).parent.absolute())+'\\'
# pathing = str(".\\lib\\")

app = Tk()
# titulo do app
app.title('Toca Fitas')
# tamanho da tela
app.geometry('510x510')


class App:
    def __init__(self, body):
        self.body = body
        self.mainFrame = Frame(self.body)
        self.mainFrame.pack( fill="both", expand=True)
        self.playing = False
        


        self.backgrounds = [
            PhotoImage(file = pathing+"img\\fita-girando.gif"),
            PhotoImage(file = pathing+"img\\tampa-aberta.png"),
            PhotoImage(file = pathing+"img\\toca-fitas-escuro.png"),
        ]
        self.bg = [
            PhotoImage(file = pathing+"img\\bg\\bg-blue.png"),
            PhotoImage(file = pathing+"img\\bg\\bg-brown.png"),
            PhotoImage(file = pathing+"img\\bg\\bg-red.png"),
            PhotoImage(file = pathing+"img\\bg\\bg-open.png")
        ]

        
        self.container = Label( self.mainFrame )
        self.tapes = Tapes(self.body, self.mainFrame, self.showTapeName)
        
        self.container.pack( pady=80)
        # self.container.config(image=self.bg[self.tapes.index])
        self.container.config(image=self.bg[3])

        self.clock = Label(
            self.container
        )
        self.clock.place(x=21, y=15)

        
        self.alicercebgBtn = PhotoImage(file = pathing+"img\\buttons\\alicerce-btn.png")
        self.btnBgPlay = PhotoImage(file = pathing+"img\\buttons\\btnPlay.png")
        self.btnBgPause = PhotoImage(file = pathing+"img\\buttons\\btn-pause.png")
        self.btnBgBack = PhotoImage(file = pathing+"img\\buttons\\btn-restart.png")
        self.btnBgAdvance = PhotoImage(file = pathing+"img\\buttons\\btn-add.png")
        self.btnBgEject = PhotoImage(file = pathing+"img\\buttons\\btn-eject.png")

        self.alicerce = Label(
            self.container,
            image=self.alicercebgBtn
        )
        self.alicerce.place(x=70, y=282)

        self.btnPlay = Button(
            self.alicerce, 
            image=self.btnBgPlay,
            borderwidth=0,
            command=self.play
        )
        self.btnPlay.pack(side=LEFT)

        # button pause
        self.btnPause = Button(
            self.alicerce, 
            image=self.btnBgPause,
            borderwidth=0,
            command=self.pause
        )
        self.btnPause.pack(side=LEFT)
         # button back
        self.btnBack = Button(
            self.alicerce, 
            image=self.btnBgBack,
            borderwidth=0,
            command=self.restart
        )
        self.btnBack.pack(side=LEFT)
        # button advace
        self.btnAddTape = Button(
            self.alicerce, 
            image=self.btnBgAdvance,
            borderwidth=0,
            command=self.addTape
        )
        self.btnAddTape.pack(side=LEFT)
        # button eject
        self.btnEject = Button(
            self.alicerce, 
            image=self.btnBgEject,
            borderwidth=0,
            command=self.showTapes
        )        
        self.btnEject.pack(side=LEFT)

        self.scotchTapeFrame = Frame(
            self.container,
            width=220
        )
        self.scotchTapeFrame.place(x=80,y=70)

        self.scotchTape = Label(
            self.scotchTapeFrame,
            text="",
            bg="#cce0f2",
            fg="black",    		
            justify=CENTER,
            font=("DS-Digital", 10)
        )
        self.scotchTape.pack()

    
        
    # functions
    def showButtons(self):
        self.alicerce.place(x=70, y=282)
        self.btnPlay.pack(side=LEFT)
        self.btnPause.pack(side=LEFT)
        self.btnBack.pack(side=LEFT)
        self.btnEject.pack(side=LEFT)

    def showTapes(self):
        self.playing = False
        self.mainFrame.pack_forget()
        self.tapes.showTapes()
        print(self.tapes.fileName)

    def change(self):
        global open
        if open:
            self.container.config(image=self.backgrounds[2])
            open=False
        else: 
            self.container.config(image=self.backgrounds[0])
            open=True

    def play(self):
        pygame.mixer.init()
        pygame.mixer.music.load(pathing+'albums\\'+self.tapes.fileName)
        self.playing = True
        self.color = ""
        if self.tapes.savedTapes[self.tapes.index]["bgIndex"] == 0:
            self.color = "blue"
            self.runGif()
        elif self.tapes.savedTapes[self.tapes.index]["bgIndex"] == 1:
            self.color = "brown"
            self.runGif()
        elif self.tapes.savedTapes[self.tapes.index]["bgIndex"] == 2:
            self.color = "red"
            self.runGif()
        pygame.mixer.music.play()
        pygame.event.wait()
        
    

    def pause(self):
        if(self.playing == True):
            self.playing = False
            self.runGif()
            pygame.mixer.music.pause()
        else:
            self.playing = True
            self.runGif()
            pygame.mixer.music.unpause()

    def showTapeName(self, playing=True):
        self.scotchTape.config(
            text=self.tapes.tapeName,
        )   
        if playing == True:
            app.after(100, self.showTapeName)
        else:
            self.container.config(
                image=self.bg[self.tapes.savedTapes[self.tapes.index]["bgIndex"]],
            )
        
    def runGif(self):
        global i
        if self.playing == True:
            self.gif = [
                PhotoImage(file = pathing+"img\\gif\\"+self.color+"\\frame1.png"),
                PhotoImage(file = pathing+"img\\gif\\"+self.color+"\\frame2.png"),
                PhotoImage(file = pathing+"img\\gif\\"+self.color+"\\frame3.png"),
                PhotoImage(file = pathing+"img\\gif\\"+self.color+"\\frame4.png")
            ]
            
            if(i == len(self.gif)-1):
                self.container.config(image=self.gif[i]) 
                i=0
            else:
                self.container.config(image=self.gif[i]) 
                i+=1
            
            self.showTapeName(True)
            app.after(100, self.runGif)
           
            

    def restart(self):
        pygame.mixer.music.rewind()
    def addTape(self):
        self.mainFrame.pack_forget()
        newTape = NewTape(self.body, self.mainFrame)
        newTape.createWidgets()
        newTape.addNewTape
        pass
            
objeto = App(app)
app.mainloop()