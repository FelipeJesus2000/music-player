from tkinter import *
import pathlib
import json


pathing = str(pathlib.Path(__file__).parent.absolute())+'\\'
# pathing = str(".\\lib\\")


class Tapes:
    def __init__(self, body, mainFrame, showTapeName):
        self.body = body
        self.mainFrame = mainFrame
        self.fileName = "vazio"
        self.showTapeName = showTapeName

        self.tapeImg = [
            PhotoImage(file = pathing+"img\\fitas\\fita-azul.png"),
            PhotoImage(file = pathing+"img\\fitas\\fita-marrom.png"),
            PhotoImage(file = pathing+"img\\fitas\\fita-vermelha.png")
        ]
        self.arrowImg = [
            PhotoImage(file = pathing+"img\\arrow-left.png"),
            PhotoImage(file = pathing+"img\\arrow-right.png")  
        ]
        self.backgrounds = [
            PhotoImage(file = pathing+"img\\fita-girando.gif"),
            PhotoImage(file = pathing+"img\\tampa-aberta.png"),
            PhotoImage(file = pathing+"img\\toca-fitas-escuro.png")
        ]
        self.bg = [
            PhotoImage(file = pathing+"img\\bg\\bg-blue.png"),
            PhotoImage(file = pathing+"img\\bg\\bg-brown.png"),
            PhotoImage(file = pathing+"img\\bg\\bg-red.png"),
            PhotoImage(file = pathing+"img\\bg\\bg-open.png")
        ]
        self.tapesFrame = Label(self.body)
        self.containerTapes = Label( self.tapesFrame)

        # abri o json que contem as informações das fitas e 
        # estancia na variável self.savedTapes
        with open(pathing+"tape-database.json", encoding="utf-8") as myJson:
            self.savedTapes = json.load(myJson)

        self.index=0
        print(self.savedTapes[self.index]['bgIndex'])

        self.btnLeftArrow = Button(
            self.containerTapes, 
            image=self.arrowImg[0],
            borderwidth=0,
            width=110,
            command=self.previousTape
        )
        self.btnLeftArrow.image = self.arrowImg[0]

        self.btnFita = Button(
            self.containerTapes, 
            image=self.tapeImg[self.savedTapes[self.index]["bgIndex"]],
            height=165,
            borderwidth=0, 
            command=self.selectTape
        )
        self.btnFita.image = self.tapeImg[self.savedTapes[self.index]["bgIndex"]]

        self.btnRightArrow = Button(
            self.containerTapes, 
            image=self.arrowImg[1],
            borderwidth=0,
            height=165,
            width=110,
            command=self.nextTape
        )   
        self.btnRightArrow.image = self.arrowImg[1]
        
        self.scotchTape = Frame(self.btnFita, width=220, height=18, bg='white')

        self.txtInfo = str(
            self.savedTapes[self.index]['album']+
            " - "+
            self.savedTapes[self.index]['artist']
        )
        self.infoTape = Label(
            self.scotchTape, 
            text=self.txtInfo,
            bg="white",
            fg="black",       		
            justify=CENTER,
            font=("DS-Digital", 10)
        )
        
        self.xInfoTape = 50
        self.tapeName = ""

    def showTapes(self):
        self.tapesFrame.pack(fill="both", expand=True)
        self.containerTapes.pack(side=LEFT)
        self.btnLeftArrow.pack(side=LEFT)
        self.btnFita.pack(side=LEFT)
        self.btnRightArrow.pack(side=LEFT)
        self.scotchTape.place(x=35, y=17)
        self.infoTape.place(x=self.xInfoTape)
        self.btnFita.bind('<Enter>', lambda e:
            self.infoTape.place(x=self.xInfoTape)
        )
        self.btnFita.bind('<Leave>', lambda e: 
            self.infoTape.place(x=self.xInfoTape)
        )
        self.marquee()
        self.fileName = self.savedTapes[self.index]['filename']
        self.tapeName = self.savedTapes[self.index]['album']+" - "+self.savedTapes[self.index]['artist']
        print(self.fileName)

    # função para passar para proxima fita
    def nextTape(self):
        if(self.index < len(self.savedTapes)-1):
            self.index+=1
        elif(self.index == len(self.savedTapes)-1):
            self.index=0

        # variavel com o nome do album e do artista
        self.tapeName = self.savedTapes[self.index]['album']+" - "+self.savedTapes[self.index]['artist']

        self.btnFita.config(
            image=self.tapeImg[self.savedTapes[self.index]['bgIndex']]
        )   
        self.infoTape.config(
            text=self.tapeName,
        )   
        self.fileName = self.savedTapes[self.index]['filename']
        print(self.fileName)
    # função para voltar para a fita anterior fita
    def previousTape(self):
        if(self.index > 0):
            self.index-=1
        elif(self.index == 0):
            self.index=len(self.savedTapes)-1
        
        # variavel com o nome do album e do artista
        self.tapeName = self.savedTapes[self.index]['album']+" - "+self.savedTapes[self.index]['artist']

        self.btnFita.config(
            image=self.tapeImg[self.savedTapes[self.index]['bgIndex']]
        )
        self.infoTape.config(
            text=self.tapeName,
        ) 
        self.fileName = self.savedTapes[self.index]['filename']
        print(self.fileName)
    # função para selecionar a fita
    def selectTape(self):
        self.tapesFrame.pack_forget()
        self.mainFrame.pack()
        self.mainFrame.pack( fill="both", expand=True)
        self.showTapeName(False)
    # passar o nome do album e do artista com efeito de rolagem
    def marquee(self):
        self.min = -68
        self.max = 210
        self.xInfoTape-=1
        if(self.xInfoTape <= self.min):
            self.xInfoTape = self.max
        self.infoTape.place(x=self.xInfoTape)
        self.body.after(100, self.marquee)
    
