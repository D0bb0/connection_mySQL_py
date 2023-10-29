from msilib.schema import Icon
from tkinter import *
from tkinter import messagebox
from tkinter import TclError
from turtle import color
import DBConection as DB
from tkinter.colorchooser import askcolor
import CreateFileSaveSettings as CRFSS
import convertFile as CV

class App():

    def __init__(self):
        self.bg_preconf = '#0F65C7'
        self.isSaveConfig()
        self.usuario = ''
        self.contrase = ''
        self.baseDatos = ''

        

    def isSaveConfig(self):
        file = CRFSS.saveConfig(self.bg_preconf)
        isSave = file.readFile()
        self.isSaveConn = False
        if isSave["status"]:
            self.text4 = isSave["credential"]["DB_NAME"]
            self.text5 = isSave["credential"]["DB_PASS"]
            self.text6  = isSave["credential"]["BD_NAMEBD"]
            self.bg_preconf = isSave["credential"]["USR_COLOR"]
            self.isSaveConn = True
            self.testConnectDB()
        else:
            self.initWindowNew()


    def initWindowNew(self):
        ventanaNew=Tk()
        ventanaNew.title("Cambio de Versión")
        ventanaNew.configure(bg=self.bg_preconf)
        ventanaNew.resizable(False, False)

        window_width = 400
        window_height = 200

        screen_width = ventanaNew.winfo_screenwidth()
        screen_height = ventanaNew.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        ventanaNew.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.confNew = ventanaNew
        self.nWin = True
        
        self.button3 = Button(ventanaNew,text='Cambiar color',command=self.change_color)
        self.button3.place(x=300,y=3)

        self.label4 = Label(ventanaNew,text='Usuario: ',bg=self.bg_preconf)
        self.label4.place(x=40,y=30)

        self.text4 = Entry(ventanaNew,bg='#E4E4E4')
        self.text4.place(x=90,y=30)

        self.label5 = Label(ventanaNew,text='Contraseña: ',bg=self.bg_preconf)
        self.label5.place(x=40,y=60)

        self.text5 = Entry(ventanaNew,bg='#E4E4E4')
        self.text5.place(x=110,y=60)

        self.label6 = Label(ventanaNew,text='Base de Datos: ',bg=self.bg_preconf)
        self.label6.place(x=40,y=90)

        self.text6 = Entry(ventanaNew,bg='#E4E4E4')
        self.text6.place(x=125,y=90)

        self.button2 = Button(ventanaNew,text='Aceptar',command=self.testConnectDB)
        self.button2.place(x=170,y=130)

        ventanaNew.mainloop()

    def initWindow(self):
        ventana=Tk()
        ventana.title("Cambio de Versión")
        ventana.configure(bg=self.bg_preconf)
        ventana.resizable(False, False)
        ventana.after(1, lambda: ventana.focus_force())
        window_width = 400
        window_height = 200

        screen_width = ventana.winfo_screenwidth()
        screen_height = ventana.winfo_screenheight()

        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)

        ventana.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.conf = ventana
        self.nWin = False
        
        self.button4 = Button(ventana,text='Cambiar color',command=self.change_color)
        self.button4.place(x=300,y=3)

        self.label1 = Label(ventana,text='Versión anterior: ',bg=self.bg_preconf)
        self.label1.place(x=40,y=30)

        self.text1 = Entry(ventana,bg='#E4E4E4')
        self.text1.place(x=135,y=30)
        self.text1.focus_set()

        self.label2 = Label(ventana,text='Versión nueva: ',bg=self.bg_preconf)
        self.label2.place(x=40,y=60)

        self.text2 = Entry(ventana,bg='#E4E4E4')
        self.text2.place(x=125,y=60)

        self.label3 = Label(ventana,text='Descripción Versión: ',bg=self.bg_preconf)
        self.label3.place(x=40,y=90)

        self.text3 = Entry(ventana,bg='#E4E4E4')
        self.text3.place(x=155,y=90)

        self.ch1 = IntVar()
        self.check1 = Checkbutton(ventana,text='Habilitado',variable=self.ch1, onvalue=1, offvalue=0,bg=self.bg_preconf)
        self.check1.place(x=40,y=120)
    
        self.button1 = Button(ventana,text='Ejecutar',command=self.connectDB)
        self.button1.place(x=170,y=160)

        ventana.mainloop()

    def testConnectDB(self):
        try:
            self.usuario = self.text4.get()
            self.contrasena = self.text5.get()
            self.baseDatos = self.text6.get()
        except AttributeError:
            self.usuario = self.text4
            self.contrasena = self.text5
            self.baseDatos = self.text6
        

        dbres = DB.DataConection(self.usuario,self.contrasena,self.baseDatos)
        res = dbres.testConnection()
        if self.isSaveConn:
            if res["status"]:
                messagebox.showinfo(title='Conexión Base de Datos',message=res["msg"])            
                self.initWindow()
            else:
                messagebox.showerror(title="Ocurrio un error",message=res["msg"])

        else:
            if res["status"]:
                messagebox.showinfo(title='Conexión Base de Datos',message=res["msg"])
                resSave = messagebox.askquestion(title=res["msg"],message="¿Desea guardar las credenciales?",icon='info')
                if resSave == 'yes':
                    file = CRFSS.saveConfig(self.bg_preconf,self.usuario,self.contrasena,self.baseDatos)
                    file.saveFile()
                else:
                    pass
                
                self.confNew.destroy()
                self.initWindow()
            else:
                messagebox.showerror(title="Error",message="Ocurrio un error: "+str(res["msg"]))


    def connectDB(self):
        oVersion = self.text1.get()
        nVersion = self.text2.get()
        descripcion = self.text3.get()

        resFile = {}

        resSure = messagebox.askquestion(title="¿Segur@?",message='¿Esta segur@ que la informacion es correcta?\n Versión anterior: '+nVersion+'\n Versión nueva: '+oVersion+'\n Descripción: '+descripcion,icon='warning')
        if resSure == 'yes':
            resFile = self.convertFile()
            dbres = DB.DataConection(self.usuario,self.contrasena,self.baseDatos,resFile["file"])
            res = dbres.ejecuteQuery()
            if res["status"] == 'true':
                self.text1.delete(0,END)
                self.text2.delete(0,END)
                self.text3.delete(0,END)
                self.text1.focus_set()
                messagebox.showinfo(title="Query Ejuecutada",message=res["msg"])

            else:
                messagebox.showerror(title="Query Ejuecutada",message=res["msg"])
        else:
            pass

    
    def change_color(self):
        colors = askcolor(title="Seleccion de Color")
        if self.nWin==False:
            self.conf.configure(bg=colors[1])
            self.label1.configure(bg=colors[1])
            self.label2.configure(bg=colors[1])
            self.label3.configure(bg=colors[1])
            self.check1.configure(bg=colors[1])
        else:
            self.confNew.configure(bg=colors[1])
            self.label4.configure(bg=colors[1])
            self.label5.configure(bg=colors[1])
            self.label6.configure(bg=colors[1])
        self.bg_preconf = colors[1]


    def convertFile(self):
        oVersion = self.text1.get()
        nVersion = self.text2.get()
        descripcion = self.text3.get()
        habilitado = self.ch1.get()
        re = {}

        try:
            resCV = CV.ConvertFile(nVersion,oVersion,descripcion,str(habilitado))
            file = resCV.getFile()
            re["status"] = True
            re["file"] = file
            return re
        except:
            messagebox.showerror(title="Error",message="Erro al cargar el archivo.")




Objeto_ventana = App()