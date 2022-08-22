from asyncio.windows_events import NULL
from importlib.resources import path
from tkinter import*
from turtle import bgcolor
from PIL import ImageTk, Image
#Funçao para as janelas(Geral)========================================================================================
def criarJanela(title = 'Titulo'):
    global janela
    janela=Tk()
    janela.configure(bg="#f0f0f0")
    janela.geometry("600x550")
    janela.title(title)
    return janela
#Funçao para atribuiçao de cores as percentagens obtidas============================================================
def checkColor(percentagem):
    if (percentagem >= 70):
        return "green"
    elif (percentagem < 50):
        return "red"
    else:
        return "yellow"
#Precentagem(Vitoria/Derrota/Empate)========================================================================
def precentagem (inputT, inputCJ1, inputCJ2, inputCJ3, inputCF1, inputCF2,inputCF3):
    #numero total de jogos
    t=int(inputT)
    #casa(Vitoria1,Empate2,Derrota3)
    cj1=int(inputCJ1)
    cj2=int(inputCJ2)
    cj3=int(inputCJ3)
    #Fora(Vitoria1,Empate2,Derrota3)
    cf1=int(inputCF1)
    cf2=int(inputCF2)
    cf3=int(inputCF3)
    #Formulas usadas para obter os resultados(Casa)
    pc1=(cj1/t)*100
    pc2=(cj2/t)*100
    pc3=(cj3/t)*100
    #Formulas usadas para obter os resultados(Fora)
    pf1=(cf1/t)*100
    pf2=(cf2/t)*100
    pf3=(cf3/t)*100
    #Resultados das percentagens(Casa)
    rc1=Label(janela,text="A pertentagem de vitoria do casa: " + str(pc1), fg=checkColor(pc1),bg="#000000")
    rc1.place(x=250,y=100)
    rc2=Label(janela,text="A pertentagem de empate do casa: " + str(pc2), fg=checkColor(pc2),bg="#000000")
    rc2.place(x=250,y=140)
    rc3=Label(janela,text="A pertentagem de Derrota do casa: " + str(pc3), fg=checkColor(pc3),bg="#000000")
    rc3.place(x=250,y=180)
    #Resultados das percentagens(Fora)
    rf1=Label(janela,text="A percentagem de vitoria do Fora: " + str(pf1), fg=checkColor(pf1),bg="#000000")
    rf1.place(x=250,y=220)
    rf2=Label(janela,text="A percentagem de empate do Fora: " + str(pf2),fg=checkColor(pf2), bg="#000000")
    rf2.place(x=250,y=260)
    rf3=Label(janela,text="A percentagem de derrota do Fora: " + str(pf3),fg=checkColor(pf3),bg="#000000")
    rf3.place(x=250,y=300)
#precentagem/Golos(1.5/2.5/3.5)====================================================================================
def precentagem2 (inputT2=0,inputGC1=0,inputGC2=0,inputGC3=0,inputGC4=0,inputGC5=0,inputGC6=0,inputGF1=NULL,inputGF2=NULL,inputGF3=NULL,inputGF4=NULL,inputGF5=NULL,inputGF6=NULL):
    #Numero total de jogos
    t2=int(inputT2)
    #Equipa da casa(-)1.5,2.5,3.5)
    gc1=int(inputGC1)
    gc2=int(inputGC2)
    gc3=int(inputGC3)
    #Equipa da casa(+)1.5,2.5,3.5)
    gc4=int(inputGC4)
    gc5=int(inputGC5)
    gc6=int(inputGC6)
    #Equipa de fora(-)1.5,2.5,3.5)
    gf1=int(inputGF1)
    gf2=int(inputGF2)
    gf3=int(inputGF3)
    #Equipa de fora(+)1.5,2.5,3.5)
    gf4=int(inputGF4)
    gf5=int(inputGF5)
    gf6=int(inputGF6)
    #Formula usada para obter os resultados(Casa/Golos)
    pgc1=(gc1/t2)*100
    pgc2=(gc2/t2)*100
    pgc3=(gc3/t2)*100
    pgc4=(gc4/t2)*100
    pgc5=(gc5/t2)*100
    pgc6=(gc6/t2)*100
    #Formula usada para obter os resultados(Fora/Golos)
    pgf1=(gf1/t2)*100
    pgf2=(gf2/t2)*100
    pgf3=(gf3/t2)*100
    pgf4=(gf4/t2)*100
    pgf5=(gf5/t2)*100
    pgf6=(gf6/t2)*100
    #Resultados(Casa/Golos)
    rg1=Label(janela,text="Casa: A percentagem de marcar - 1.5/Golos: " + str(pgc1),fg=checkColor(pgc1),bg="#000000")
    rg1.place(x=250,y=80)
    rg2=Label(janela,text="Casa: A percentagem de marcar + 1.5/Golos: " + str(pgc4),fg=checkColor(pgc4),bg="#000000")
    rg2.place(x=250,y=110)
    rg3=Label(janela,text="Casa: A percentagem de marcar - 2.5/Golos: " + str(pgc2),fg=checkColor(pgc2),bg="#000000")
    rg3.place(x=250,y=140)
    rg4=Label(janela ,text="Casa: A percentagem de marcar + 2.5/Golos: " + str(pgc5),fg=checkColor(pgc5),bg="#000000")
    rg4.place(x=250,y=170)
    rg5=Label(janela,text="Casa: A percentagem de marcar - 3.5/Golos: " + str(pgc3),fg=checkColor(pgc3),bg="#000000")
    rg5.place(x=250,y=200)
    rg6=Label(janela ,text="Casa: A percentagem de marcar + 3.5/Golos: " + str(pgc6),fg=checkColor(pgc6),bg="#000000")
    rg6.place(x=250,y=230)
    #Resultados(Fora/Golos)
    if pgf1 != NULL:
        rg11=Label(janela,text="Fora: A percentagem de marcar - 1.5/Golos: " + str(pgf1),fg=checkColor(pgf1),bg="#000000")
        rg11.place(x=250,y=270)
    if pgf4 != NULL:
        rg12=Label(janela,text="Fora: A percentagem de marcar + 1.5/Golos: " + str(pgf4),fg=checkColor(pgf4),bg="#000000")
        rg12.place(x=250,y=300)
    if pgf2 != NULL:
        rg13=Label(janela,text="Fora: A percentagem de marcar - 2.5/Golos: " + str(pgf2),fg=checkColor(pgf2),bg="#000000")
        rg13.place(x=250,y=330)
    if pgf5 != NULL:
        rg14=Label(janela,text="Fora: A percentagem de marcar + 2.5/Golos: " + str(pgf5),fg=checkColor(pgf5),bg="#000000")
        rg14.place(x=250,y=360)
    if pgf3 != NULL:
        rg15=Label(janela,text="Fora: A percentagem de marcar - 3.5/Golos: " + str(pgf3),fg=checkColor(pgf3),bg="#000000")
        rg15.place(x=250,y=390)
    if pgf6 != NULL:
        rg16=Label(janela,text="Fora: A percentagem de marcar + 3.5/Golos: " + str(pgf6),fg=checkColor(pgf6),bg="#000000")
        rg16.place(x=250,y=420)
#Funçao de fechar a janela aberta e voltar ao inicio(localizada na pagina 4 e reinicia na pagina 1)================================
def inico():
    global janela
    janela.destroy()
    pagMenu()
#Funçao para a pagina 4==============================================================
def p4():
    #Criaçao da janela 4
    janela4= criarJanela("GUESS GAME")
    imagem1=ImageTk.PhotoImage(Image.open("C:/Users/rui/OneDrive/Área de Trabalho/ft35.21.jpg"))
    imagem2=Label(janela4,image=imagem1)
    imagem2.pack()
    #Aqui temos as perguntas que sao feitas ao utilizador
    #Aqui pergunta os jogos que estao a ser avaliados(t2)
    t2=Label(janela4,text="Quantos jogos estamos a avaliar??",bg="#555555",fg="#ffffff")
    #Aqui temos as pergunta em relaçao aos jogos(Golos)
    g1=Label(janela4,text="Quantos jogos marcou -1.5??",bg="#555555",fg="#ffffff")
    g2=Label(janela4,text="Quantos jogos marcou +1.5??",bg="#555555",fg="#ffffff")
    g3=Label(janela4,text="Quantos jogos marcou -2.5??",bg="#555555",fg="#ffffff")
    g4=Label(janela4,text="Quantos jogos marcou +2.5??",bg="#555555",fg="#ffffff")
    g5=Label(janela4,text="Quantos jogos marcou -3.5??",bg="#555555",fg="#ffffff")
    g6=Label(janela4,text="Quantos jogos marcou +3.5??",bg="#555555",fg="#ffffff")
    #Aqui entra o valores vindos da funçao percentagens2
    inputT2=Entry(janela4)
    #Aqui entra os valores vindos da funçao percentagens2(casa/fora)
    inputGC1=Entry(janela4)
    inputGC2=Entry(janela4)
    inputGC3=Entry(janela4)
    inputGC4=Entry(janela4)
    inputGC5=Entry(janela4)
    inputGC6=Entry(janela4)
    #Esta funçao vai buscar os valores a funçao percentagens2
    def chamarPercentagem4():
        precentagem2(inputT2.get(),inputGC1.get(),inputGC2.get(),inputGC3.get(),inputGC4.get(),inputGC5.get(),inputGC6.get())
    #Aqui temos os botoes e suas funcionalidades
    botao4=Button(janela4,text="Calcular",command=chamarPercentagem4,bg="#555555",fg="#ffffff")
    botao44=Button(janela4,text="Menu",command =inico,bg="#555555",fg="#ffffff")
    #Aqui temos o local onde encontramos a pergunta(Nº de jogos) e local onde colocamos a resposta
    t2.place(x=270,y=10)
    inputT2.place(x=300,y=30,width=130)
    ##Aqui temos o local onde encontramos a pergunta(em relaçao aos golos)e local onde colocamos a resposta
    g1.place(x=5,y=60)
    inputGC1.place(x=30,y=90)
    g2.place(x=5,y=120)
    inputGC4.place(x=30,y=150)
    g3.place(x=5,y=180)
    inputGC2.place(x=30,y=210)
    g4.place(x=5,y=240)
    inputGC5.place(x=30,y=270)
    g5.place(x=5,y=300)
    inputGC3.place(x=30,y=330)
    g6.place(x=5,y=360)
    inputGC6.place(x=30,y=390)
    #Aqui temos o local onde se localiza os botoes
    botao4.place(x=300,y=450,width=300,height=50)
    botao44.place(x=300,y=500,width=300, height=50)
    janela4.mainloop()
#Funçao para fechar janela atual e abrir a proxima(pagina 4)=======================================================================
def pseguinte3():
    global janela
    janela.destroy()
    pagMenu()
#Aqui funçao para a pagina 3============================================================================================
def p3():
    #Criaçao da janela 3
    janela3= criarJanela("GUESS GAME")
    imagem1=ImageTk.PhotoImage(Image.open("C:/Users/rui/OneDrive/Área de Trabalho/ft35.21.jpg"))
    imagem2=Label(janela3,image=imagem1)
    imagem2.pack()
    #Aqui temos a pergunta em relaçao ao numero de jogos
    t=Label(janela3,text="Quantos jogos estamos a avaliar??",bg="#555555",fg="#ffffff")
    #Aqui temos as perguntas em relaçao aos resultados(V/E/D)(Casa)
    c1=Label(janela3,text="Quantos jogos ganhou o da casa??",bg="#555555",fg="#ffffff")
    c2=Label(janela3,text="Quantos jogos empatou o da casa??",bg="#555555",fg="#ffffff")
    c3=Label(janela3,text="Quantos jogos perdeu o da casa??",bg="#555555",fg="#ffffff")
    #Aqui temos as perguntas em relaçao aos resultados(V/E/D)(Fora)
    f1=Label(janela3,text="Quantos jogos ganhou o da Fora??",bg="#555555",fg="#ffffff")
    f2=Label(janela3,text="Quantos jogos empatou o da Fora??",bg="#555555",fg="#ffffff")
    f3=Label(janela3,text="Quantos jogos derrota o da Fora??",bg="#555555",fg="#ffffff")
    ###
    inputT=Entry(janela3)
    ##casa
    inputCJ1=Entry(janela3)
    inputCJ2=Entry(janela3)
    inputCJ3=Entry(janela3)
    ###fora
    inputCF1=Entry(janela3)
    inputCF2=Entry(janela3)
    inputCF3=Entry(janela3)
    #Esta funçao vai buscar os valores a funçao percetagem
    def chamarPercentagem3():
        precentagem(inputT.get(),
        inputCJ1.get(), 
        inputCJ2.get(), 
        inputCJ3.get(), 
        inputCF1.get(),
        inputCF2.get(), 
        inputCF3.get())
    #Aqui temos os botoes(Calcular e para mudar de pagina)
    botao3=Button(janela3, text="Calcular", command=chamarPercentagem3,bg="#555555",fg="#ffffff")
    botao13 = Button(janela3, text="Menu",command=pseguinte3,bg="#555555",fg="#ffffff")
    #Aqui temos a pergunta e local onde o utilizador introduz o numero de jogos que estao a ser avaliados
    t.place(x=270,y=10)
    inputT.place(x=300,y=30,width=130)
    #Aqui temos os perguntas e o local onde o utilizador introduz o numero de jogos(V/E/D)(Casa)
    c1.place(x=5,y=60)
    inputCJ1.place(x=30,y=90)
    c2.place(x=5,y=120)
    inputCJ2.place(x=30,y=150)
    c3.place(x=5,y=180)
    inputCJ3.place(x=30,y=210)
    #Aqui temos os perguntas e o local onde o utilizador introduz o numero de jogos(V/E/D)(Fora)
    f1.place(x=5,y=240)
    inputCF1.place(x=30,y=270)
    f2.place(x=5,y=300)
    inputCF2.place(x=30,y=330)
    f3.place(x=5,y=360)
    inputCF3.place(x=30,y=390)
    #Aqui temos a localizaçao dos botoes
    botao3.place(x=300,y=450,width=300,height=50)
    botao13.place(x=300,y=500,width=300, height=50)
    janela3.mainloop()
#Funçao de mudança de pagina====================================================================================================
def pseguinte2():
    global janela
    janela.destroy()
    pagMenu()
#Funçao para a pagina 2=====================================================================
def p2():
    #Aqui temos a criaçao da pagina2 atraves de uma funçao
    janela2= criarJanela("GUESS GAME")
    imagem1=ImageTk.PhotoImage(Image.open("C:/Users/rui/OneDrive/Área de Trabalho/ft35.21.jpg"))
    imagem2=Label(janela2,image=imagem1)
    imagem2.pack()
    #Aqui temos as perguntas que sao feitas ao utilizador
    t2=Label(janela2,text="Quantos jogos estamos a avaliar??",bg="#555555",fg="#ffffff")
    #Casa
    g1=Label(janela2,text="Casa: Quantos jogos marcou -1.5??",bg="#555555",fg="#ffffff")
    g2=Label(janela2,text="Casa: Quantos jogos marcou +1.5??",bg="#555555",fg="#ffffff")
    g3=Label(janela2,text="Casa: Quantos jogos marcou -2.5??",bg="#555555",fg="#ffffff")
    g4=Label(janela2,text="Casa: Quantos jogos marcou +2.5??",bg="#555555",fg="#ffffff")
    g5=Label(janela2,text="Casa: Quantos jogos marcou -3.5??",bg="#555555",fg="#ffffff")
    g6=Label(janela2,text="Casa: Quantos jogos marcou +3.5??",bg="#555555",fg="#ffffff")
    #Fora
    g11=Label(janela2,text="Fora: Quantos jogos marcou -1.5??",bg="#555555",fg="#ffffff")
    g12=Label(janela2,text="Fora: Quantos jogos marcou +1.5??",bg="#555555",fg="#ffffff")
    g13=Label(janela2,text="Fora: Quantos jogos marcou -2.5??",bg="#555555",fg="#ffffff")
    g14=Label(janela2,text="Fora: Quantos jogos marcou +2.5??",bg="#555555",fg="#ffffff")
    g15=Label(janela2,text="Fora: Quantos jogos marcou -3.5??",bg="#555555",fg="#ffffff")
    g16=Label(janela2,text="Fora: Quantos jogos marcou +3.5??",bg="#555555",fg="#ffffff")
    #
    inputT2=Entry(janela2)
    #casa
    inputGC1=Entry(janela2)
    inputGC2=Entry(janela2)
    inputGC3=Entry(janela2)
    inputGC4=Entry(janela2)
    inputGC5=Entry(janela2)
    inputGC6=Entry(janela2)
    #fora
    inputGF1=Entry(janela2)
    inputGF2=Entry(janela2)
    inputGF3=Entry(janela2)
    inputGF4=Entry(janela2)
    inputGF5=Entry(janela2)
    inputGF6=Entry(janela2)
    def chamarPercentagem2():
        precentagem2(inputT2.get(),inputGC1.get(),inputGC2.get(),inputGC3.get(),inputGC4.get(),inputGC5.get(),inputGC6.get(),inputGF1.get(),inputGF2.get(),inputGF3.get(),inputGF4.get(),inputGF5.get(),inputGF6.get())
    #Aqui e temos os botoes
    botao22=Button(janela2,text="Calcular",bg="#555555",fg="#ffffff",command=chamarPercentagem2)
    button2 = Button(janela2, text="Menu",command=pseguinte2,bg="#555555",fg="#ffffff")
    #Aqui temos a localizaçao da pergunta e onde colocar a resposta(janela2)
    t2.place(x=270,y=10)
    inputT2.place(x=300,y=30,width=130)
    #Aqui temos a localizaçao das perguntas e onde responder(casa)
    g1.place(x=5,y=25)
    inputGC1.place(x=30,y=45)
    g2.place(x=5,y=65)
    inputGC4.place(x=30,y=85)
    g3.place(x=5,y=105)
    inputGC2.place(x=30,y=125)
    g4.place(x=5,y=145)
    inputGC5.place(x=30,y=165)
    g5.place(x=5,y=185)
    inputGC3.place(x=30,y=205)
    g6.place(x=5,y=225)
    inputGC6.place(x=30,y=245)
    ##Aqui temos a localizaçao das perguntas e onde responder(Fora)
    g11.place(x=5,y=265)
    inputGF1.place(x=30,y=285)
    g12.place(x=5,y=305)
    inputGF4.place(x=30,y=325)
    g13.place(x=5,y=345)
    inputGF2.place(x=30,y=365)
    g14.place(x=5,y=385)
    inputGF5.place(x=30,y=405)
    g15.place(x=5,y=425)
    inputGF3.place(x=30,y=445)
    g16.place(x=5,y=465)
    inputGF6.place(x=30,y=485)
    #Aqui temos a localizaçao dos botoes
    botao22.place(x=300,y=450,width=300,height=50)
    button2.place(x=300,y=500,width=300, height=50)
    janela2.mainloop()
#Funçao de mudança de pagina ======================================================================================
def pseguinte1():
    global janela
    janela.destroy()
    pagMenu()
#Funçao para a pagina1 =========================================================
def p1():
    #Funçao para criaçao da pagina
    janela = criarJanela("GUESS GAME")
    imagem1=ImageTk.PhotoImage(Image.open("C:/Users/rui/OneDrive/Área de Trabalho/ft35.21.jpg"))
    imagem2=Label(janela,image=imagem1)
    imagem2.pack()
    #Aqui temos as perguntas feitas ao utilizador
    t=Label(janela,text="Quantos jogos estamos a avaliar??",bg="#555555",fg="#ffffff")
    #casa
    c1=Label(janela,text="Quantos jogos ganhou o da casa??",bg="#555555",fg="#ffffff")
    c2=Label(janela,text="Quantos jogos empatou o da casa??",bg="#555555",fg="#ffffff")
    c3=Label(janela,text="Quantos jogos perdeu o da casa??",bg="#555555",fg="#ffffff")
    #fora
    f1=Label(janela,text="Quantos jogos ganhou o da Fora??",bg="#555555",fg="#ffffff")
    f2=Label(janela,text="Quantos jogos empatou o da Fora??",bg="#555555",fg="#ffffff")
    f3=Label(janela,text="Quantos jogos derrota o da Fora??",bg="#555555",fg="#ffffff")
    #
    inputT=Entry(janela)
    #casa
    inputCJ1=Entry(janela)
    inputCJ2=Entry(janela)
    inputCJ3=Entry(janela)
    #fora
    inputCF1=Entry(janela)
    inputCF2=Entry(janela)
    inputCF3=Entry(janela)
    #Aqui temos os botoes e tambem usei o lambda para chamar a funçao precentagem(sem criar outra funçao)
    botao1=Button(janela,text="Calcular",bg="#555555",fg="#ffffff",command=lambda:precentagem (inputT.get(), inputCJ1.get(), inputCJ2.get(), inputCJ3.get(), inputCF1.get(),inputCF2.get(), inputCF3.get()))
    botao11 = Button(janela, text="Menu",command=pseguinte1,bg="#555555",fg="#ffffff")
    #Aqui temos a localizao das pergunta e local para respoonder
    t.place(x=270,y=10)
    inputT.place(x=300,y=30,width=130)
    #casa
    c1.place(x=5,y=60)
    inputCJ1.place(x=30,y=90)
    c2.place(x=5,y=120)
    inputCJ2.place(x=30,y=150)
    c3.place(x=5,y=180)
    inputCJ3.place(x=30,y=210)
    #fora
    f1.place(x=5,y=240)
    inputCF1.place(x=30,y=270)
    f2.place(x=5,y=300)
    inputCF2.place(x=30,y=330)
    f3.place(x=5,y=360)
    inputCF3.place(x=30,y=390)
    #aqui temos a localizaçao dos botoes
    botao1.place(x=300,y=450,width=300,height=50)
    botao11.place(x=300,y=500,width=300, height=50)
    janela.mainloop()
#==================================================================janela principapal(Menu)===========================
def mp1():
    global janela
    janela.destroy()
    p1()
def mp2():
    global janela
    janela.destroy()
    p2()
def mp3():
    global janela
    janela.destroy()
    p3()
def mp4():
    global janela
    janela.destroy()
    p4()
def fechar():
    global janela
    janela.destroy()

def pagMenu():
    janelamenu=criarJanela("GUESS GAME")
    imagem1=ImageTk.PhotoImage(Image.open("C:/Users/rui/OneDrive/Área de Trabalho/ft35.21.jpg"))
    imagem2=Label(janela,image=imagem1)
    imagem2.pack()
    info=Label(janelamenu,text="Email:rui.costa.177@Hotmail.com",fg="BLACK",bg="#f4f0ec")
    info2=Label(janelamenu,text="Instagram:@rfcosta98",fg="BLACK",bg="#f4f0ec")
    botaop1=Button(janelamenu,text="Conf. Individuais:V/E/D",command=mp1,bg="#555555",fg="#ffffff")
    botaop1.place(x=315,y=50,width=260,height=160)
    botaop2=Button(janelamenu,text="Conf. Individuais:Golos",command=mp2,bg="#555555",fg="#ffffff")
    botaop2.place(x=315,y=300,width=260,height=160)
    botaop3=Button(janelamenu,text="Conf. Diretos:V/E/D",command=mp3,bg="#555555",fg="#ffffff")
    botaop3.place(x=30,y=50,width=260,height=160)
    botaop4=Button(janelamenu,text="Conf. Diretos:Golos",command=mp4,bg="#555555",fg="#ffffff")
    botaop4.place(x=30,y=300,width=260, height=160)
    botaof=Button(janelamenu,text="Encerrar",command=fechar, bg="BLACK",fg="WHITE")
    botaof.place(x=0,y=500,width=600, height=50)
    info.place(x=0.1, y=0.1)
    info2.place(x=480,y=0)
    janelamenu.mainloop()
pagMenu()