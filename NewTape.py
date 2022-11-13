from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
import pathlib
import json
import os

pathing = str(pathlib.Path(__file__).parent.absolute())+'\\'
# pathing = str(".\\lib\\")

class NewTape:
    def __init__(self, body, mainFrame):
        self.body = body
        self.mainFrame = mainFrame
        self.pathFile = ""
        self.color = ""
        self.filename = ""
        self.pathTape = ""
        self.listColor = ""
        
    


    def createWidgets(self):
        bgImage = PhotoImage(file = pathing+"img\\bg\\bg-form.png")
        self.bg = Label(
            self.body,
            # bg='black',
            image=bgImage,
        )
        print(pathing)
        self.bg.pack(fill="both", expand=True)
        self.bg.image=bgImage
        
        self.formTape = Frame(
            self.bg,
            border=1,
            highlightbackground="black",
            highlightthickness="5"
        )
        self.formTape.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.formTape.rowconfigure(0, weight=1)
        self.formTape.rowconfigure(1, weight=1)
        self.formTape.rowconfigure(2, weight=1)
        lblTitle = Label(
            self.formTape,
            text="Adicionar nova fita",
            font=(15)
        )
        lblTitle.grid(column=1, row=0)
        # nome do album
        # label
        lblAlbum = Label(
            self.formTape,
            text="Album:"
        )
        lblAlbum.grid(column=0, row=1)
        # campo
        self.txtAlbum = Entry(
            self.formTape
        )
        self.txtAlbum.grid(column=1, row=1)

        # nome do artista
        # label
        lblArtist = Label(
            self.formTape,
            text="Artista:"
        )
        lblArtist.grid(column=0, row=2)
        # campo
        self.txtArtist = Entry(
            self.formTape
        )
        self.txtArtist.grid(column=1, row=2)


        # nome do arquivo
        # label
        lblFilename = Label(
            self.formTape,
            text="Nome do arquivo:"
        )
        lblFilename.grid(column=0, row=3)
        self.pathTape = StringVar()

        # campo
        self.txtFilename = Entry(
            self.formTape,
            state="disable",
            textvariable=self.pathTape
        )
        self.txtFilename.grid(column=1, row=3)

        # botão para selecionar arquivo
        btnGetPath = Button(
            self.formTape,
            text="Selecionar arquivo",
            command=self.selectFile
        )
        btnGetPath.grid(column=2, row=3)

        # Cor
        # label
        lblColor = Label(
            self.formTape,
            text="Cor"
        )
        lblColor.grid(column=0, row=4, columnspan=3)
        # setando cores da lista
        colors = ("Azul", "Marrom", "Vermelha")
        colors = StringVar(value=colors)

        # listbox de cores
        listColor = Listbox(
            self.formTape,
            listvariable=colors,
            height=3,
            selectmode='extended',
            fg="black"
        )
        listColor.grid(column=0, row=5, columnspan=3)

        # função de selecionar a cor e coloca-la em uma variavel
        def selectColor(event):
            self.color =listColor.get(listColor.curselection())

        # evento ao selecionar listbox
        listColor.bind('<<ListboxSelect>>', selectColor)

        # button de submit
        btnSubmit = Button(
            self.formTape,
            text="Adicionar",
            command=self.addNewTape
        )
        btnSubmit.grid(column=0, row=6) 
        # button de cancel
        btnCancel = Button(
            self.formTape,
            text="Cancelar",
            command=self.disappearForm
        )
        btnCancel.grid(column=2, row=6) 

    # verifica se o campo album foi preenchido
    def checkNameAlbum(self):
        if(self.txtAlbum.get() == ""):
            showinfo(
                title='Atenção',
                message="Preencha o campo 'Album'!!!"
            )
            return False
    # verifica se o campo artista foi preenchido
    def checkNameArtist(self):
        if(self.txtArtist.get() == ""):
            showinfo(
                title='Atenção',
                message="Preencha o campo 'Artista'!!!"
            )
            return False
    # verifica se o arquivo é do tipo mp3
    def vrfExtension(self):
        lenght = len(self.pathFile)
        ext = ""
        while self.pathFile[lenght-1] != ".":
            ext += self.pathFile[lenght-1]
            lenght-=1
        ext = '.' + ext[::-1]
        print("arquivo do tipo: ", ext)
        return ext.lower()
    # verifica se um arquivo foi selecionado
    def checkFile(self):
        if(self.txtFilename.get() == ""):
            showinfo(
                title='Atenção',
                message="Selecione um arquivo no campo 'Nome do arquivo'!!!"
            )
            return False
    # verifica se alguma cor foi selecionada
    def checkColor(self):
        if(self.color == ""):
            showinfo(
                title='Atenção',
                message="Seleciona uma Cor!!!"
            )
            return False
    # passa a cor para a posição no index do json
    def getColorIndex(self):
        if(self.color.lower() == "azul"): return 0
        if(self.color.lower() == "marrom"): return 1
        if(self.color.lower() == "vermelho"): return 2
  
    # função para alterar json
    def registerTape(self, album, artist, filename, color):
        newTape = {
            "album": album,
            "artist": artist,
            "filename": filename,
            "bgIndex": color
        }
        # carrega o json
        with open(pathing+"tape-database.json") as myJson:
            savedTapes = json.load(myJson)
            savedTapes.append(newTape)
            print((savedTapes))
        # altera o json
        with open(pathing+"tape-database.json", 'w') as myJson:
            json.dump(savedTapes, myJson, indent=4)

    # função para selecionar o arquivo e setar ele 
    # na variáveis
    def selectFile(self):
        self.pathFile = askopenfilename()
        lenght = len(self.pathFile)
        self.filename = ""
        while self.pathFile[lenght-1] != "/":
            self.filename += self.pathFile[lenght-1]
            lenght-=1
        self.filename = self.filename[::-1]
        self.pathTape.set(self.filename)
        print(self.filename)
        

    # move o arquivo para a pasta do programa
    def moveFile(self):
        os.rename(self.pathFile, pathing+'albums\\'+self.filename)
    
    # função para executar os comandos na ordem
    def addNewTape(self):
        if(self.checkNameAlbum() == False): return
        if(self.checkNameArtist() == False): return
        if(self.checkFile() == False): return
        if(self.checkColor() == False): return
        if(self.vrfExtension() != ".mp3"):
            showinfo(
                title='Atenção',
                message="Selecione um arquivo do tipo .mp3!!!"
            ) 
            return
        try:
            colorNumber = self.getColorIndex()
            self.registerTape(
                self.txtAlbum.get(),     
                self.txtArtist.get(),
                self.txtFilename.get(),
                colorNumber
            )
            self.moveFile()
            showinfo(
                title='Atenção',
                message="Cadastro preenchido com sucesso!!!!!!"
            )
            self.disappearForm()
        except:
            showinfo(
                title='Atenção',
                message="Ops não foi possivel cadastrar a fita!!!!!!"
            )

    # desaparece o formulario e volta para a pagina inicial
    def disappearForm(self):
        self.bg.destroy()
        self.mainFrame.pack()
        self.mainFrame.pack( fill="both", expand=True)