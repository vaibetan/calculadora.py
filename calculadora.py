from tkinter import *


root = Tk()
root.title('Na falta do antonio temos:')
root.geometry('408x355')
root.minsize(408,355)
root.maxsize(408,355)

numero1 = ''
divisao = FALSE
multiplica = FALSE
Menos = FALSE
Mais = FALSE
numero2 = ''

root.configure(background='#282828')

e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF', bg='#a7a28f', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0,
    column=0,
    columnspan=4,
    pady=2
)
#------------------------------------------------------------

def butao_click(num):
    e.insert(END, num)
def butao_divisao():
    global numero1
    global divisao
    divisao = TRUE
    numero1 = e.get()
    e.delete(0, END)    
def butao_multiplica():
    global numero1
    global multiplica
    multiplica = TRUE
    numero1 = e.get()
    e.delete(0, END)  
def butao_subtracao():
    global numero1
    global Menos
    Menos = TRUE
    numero1 = e.get()
    e.delete(0, END)  
def butao_adicao():
    global numero1
    global Mais
    Mais = TRUE
    numero1 = e.get()
    e.delete(0, END)
def butao_limpa():
    e.delete(0, END)
def butao_igual():
    global divisao
    global multiplica
    global Mais
    global Menos
    numero2 = e.get()
    e.delete(0, END)
    if Mais == TRUE:
        e.insert(0, int(numero1) + int(numero2))
        Mais = FALSE
    if Menos == TRUE:
        e.insert(0, int(numero1) - int(numero2))
        Menos = FALSE
    if multiplica == TRUE:
        e.insert(0, int(numero1) * int(numero2))
        multiplica = FALSE  
    if divisao == TRUE:
        e.insert(0, int(numero1) / int(numero2))
        divisao = FALSE  
        

divide = Button(root,
                text='÷',
                padx=40,
                pady=20,
                command=butao_divisao,
                fg='#FFFFFF',
                activeforeground='#FFFFFF',
                bg='#320064',
                activebackground='#240046',
                relief=FLAT,
                font=('futura', 12, 'bold')
)
divide.grid(row=0, column=4)
#-----------------------------------------------------------------
UM = Button(root,
            text='1',
            padx=40,
            pady=20,
            command=lambda: butao_click(1),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
UM.grid(row=1, column=1)
#------------------------------------------------------------------------------
DOIS = Button(root,
            text='2',
            padx=40,
            pady=20,
            command=lambda:  butao_click(2),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
DOIS.grid(row=1, column=2)
#-----------------------------------------------------------------------------------------
TRES = Button(root,
            text='3',
            padx=40,
            pady=20,
            command=lambda: butao_click(3),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
TRES.grid(row=1, column=3)
#------------------------------------------------------------
multiplica = Button(root,
            text='x',
            padx=40,
            pady=20,
            command=butao_multiplica,
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
multiplica.grid(row=1, column=4)
#-------------------------------------------------------------------------------------------
Quatro = Button(root,
            text='4',
            padx=40,
            pady=20,
            command=lambda: butao_click(4),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
Quatro.grid(row=2, column=1)
#-----------------------------------------------------------------------------------------
Cinco = Button(root,
            text='5',
            padx=40,
            pady=20,
            command=lambda: butao_click(5),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
Cinco.grid(row=2, column=2)
#-------------------------------------------------------------------------------------
Seis = Button(root,
            text='6',
            padx=40,
            pady=20,
            command=lambda: butao_click(6),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
Seis.grid(row=2, column=3)
#--------------------------------------------------------------------------------------
Menos = Button(root,
            text='-',
            padx=41.5,
            pady=20,
            command=butao_subtracao,
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
Menos.grid(row=2, column=4)
#--------------------------------------------------------------------------------------
sete = Button(root,
            text='7',
            padx=40,
            pady=20,
            command=lambda: butao_click(7),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
sete.grid(row=3, column=1)
#--------------------------------------------------------------------------------------
Oito = Button(root,
            text='8',
            padx=40,
            pady=20,
            command=lambda: butao_click(8),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
Oito.grid(row=3, column=2)
#---------------------------------------------------------------------------
Nove = Button(root,
            text='9',
            padx=40,
            pady=20,
            command=lambda: butao_click(9),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
Nove.grid(row=3, column=3)
#------------------------------------------------------------------------
Mais = Button(root,
            text='+',
            padx=40,
            pady=20,
            command=butao_adicao,
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
Mais.grid(row=3, column=4)
#--------------------------------------------------------------------------------------------------
Zero = Button(root,
            text='0',
            padx=91,
            pady=20,
            command=lambda: butao_click(0),
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
Zero.grid(row=4,column=1, columnspan=2)
#---------------------------------------------------------------------------------
Limpa = Button(root,
            text='c',
            padx=40,
            pady=20,
            command=butao_limpa,
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
Limpa.grid(row=4, column=3)
#---------------------------------------------------------------------
Igual = Button(root,
            text='=',
            padx=40,
            pady=20,
            command=butao_igual,
            fg='#FFFFFF',
            activeforeground='#FFFFFF',
            bg='#320064',
            activebackground='#240046',
            relief=FLAT,
            font=('futura', 12, 'bold')
)
Igual.grid(row=4, column=4 )




root.mainloop()


#KAUABRENO