from cgitb import text
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
import pathlib
import json
import os
# import time

app = Tk()
app.title('Toca Fitas')
app.geometry('510x510')


formTape = Frame(
    app,
    border=1,
    highlightbackground="black",
    highlightthickness="1"
)
formTape.place(x=0,y=0)
# nome
# artista
# nome do arquivo
# cor

# formTape.columnconfigure(0, weight=1)
# formTape.columnconfigure(1, weight=1)
# formTape.columnconfigure(2, weight=1)
formTape.rowconfigure(0, weight=1)
formTape.rowconfigure(1, weight=1)
formTape.rowconfigure(2, weight=1)
global color, pathFile, filename, pathing
pathFile = ""
color = ""
filename = ""
pathing = str(pathlib.Path(__file__).parent.absolute())+'\\'


# essa função server para verificar se os campos do formulario foram preenchidos
def checkFields():
    global color, pathFile, pathing, filename
    if(txtAlbum.get() == ""):
        showinfo(
            title='Atenção',
            message="Preencha o campo 'Album'!!!"
        )
        return
    elif(txtArtist.get() == ""):
        showinfo(
            title='Atenção',
            message="Preencha o campo 'Artista'!!!"
        )
        return
    elif(txtFilename.get() == ""):
        showinfo(
            title='Atenção',
            message="Selecione um arquivo .mp3 no campo 'Nome do arquivo'!!!"
        )
        return
    elif(color == ""):
        showinfo(
            title='Atenção',
            message="Seleciona uma Cor!!!"
        )
        return
    else:
        showinfo(
            title='Atenção',
            message="Cadastro preenchido com sucesso!!!!!!"
        )
        colorNumber = 0
        if(color.lower() == "azul"):
            colorNumber = 0
        if(color.lower() == "marrom"):
            colorNumber = 1
        if(color.lower() == "vermelho"):
            colorNumber = 2
        registerTape(
            txtAlbum.get(),     
            txtArtist.get(),
            txtFilename.get(),
            colorNumber
        )
        os.rename(pathFile, pathing+'albums\\'+filename)

# esta função altera o json e leva a musica para a pasta albums
def registerTape(album, artist, filename, color):
    
    newTape = {
        "album": album,
        "artist": artist,
        "filename": filename,
        "bgIndex": color
    }
    with open(pathing+"tape-database.json") as myJson:
        savedTapes = json.load(myJson)
        savedTapes.append(newTape)
        print((savedTapes))

    with open(pathing+"tape-database.json", 'w') as myJson:
        json.dump(savedTapes, myJson, indent=4)


# função para selecionar o arquivo
def selectFile():
    global filename, pathFile
    pathFile = askopenfilename()
    lenght = len(pathFile)
    i = lenght
    
    while pathFile[i-1] != "/":
        filename += pathFile[i-1]
        i-=1
    filename = filename[::-1]
    pathTape.set(filename)
    print(filename)
    
    
# função de selecionar a cor e coloca-la em uma variavel
def selectColor(event):
    global color
    color = listColor.get(listColor.curselection())




# nome do album
# label
lblAlbum = Label(
    formTape,
    text="Album:"
)
lblAlbum.grid(column=0, row=0)
# campo
txtAlbum = Entry(
    formTape
)
txtAlbum.grid(column=1, row=0)

# nome do artista
# label
lblArtist = Label(
    formTape,
    text="Artista:"
)
lblArtist.grid(column=0, row=1)
# campo
txtArtist = Entry(
    formTape
)
txtArtist.grid(column=1, row=1)


# nome do arquivo
# label
lblFilename = Label(
    formTape,
    text="Nome do arquivo:"
)
lblFilename.grid(column=0, row=2)

pathTape = StringVar()
# pathTape.set("Testando o texto")

# campo
txtFilename = Entry(
    formTape,
    state="disable",
    textvariable=pathTape
)
txtFilename.grid(column=1, row=2)

# botão para selecionar arquivo
btnGetPath = Button(
    formTape,
    text="Selecionar arquivo",
    command=selectFile
)
btnGetPath.grid(column=2, row=2)

# Cor
# label
lblColor = Label(
    formTape,
    text="Cor"
)
lblColor.grid(column=0, row=3, columnspan=3)

colors = ("Azul", "Marrom", "Vermelha")
colors = StringVar(value=colors)

# listbox
listColor = Listbox(
    formTape,
    listvariable=colors,
    height=3,
    selectmode='extended',
    fg="black"
)
listColor.grid(column=0, row=4, columnspan=3)

# evento ao selecionar listbox
listColor.bind('<<ListboxSelect>>', selectColor)


# button de submit
btnSubmit = Button(
    formTape,
    text="Adicionar",
    command=checkFields
)
btnSubmit.grid(column=1, row=5)

# Agora devo criar uma classe que receberá os dados do formulario
# quando a classe receber os dados ela deverá alterar o json
# e mover o arquivo selecionado para a pasta albums(tudo já foi programado);
# não devo esquecer de melhorar o design da tela de formulario, esta muito feio;
# o json selecionado é o de teste;



app.mainloop()