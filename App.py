import tkinter as tk
import tkinter.font as tkFont
import ctypes
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
import os

class App:
    def __init__(self, root):

        self.cwd = os.getcwd()
        self.dirs = ["dati", "giorni", "ore"]
        self.colonna_1 = ""
        self.colonna_2 = ""
        self.colonna_3 = ""
        self.sep = ""
  
        self.media_giorni = []
        self.tot_giorni = 0
        self.media_O3_giorni = []
        self.media_H_giorni = []
        self.tot_O3_giorni = 0
        self.tot_H_giorni = 0

        self.media_O3_ore = []
        self.media_H_ore = []
        self.media_ore = []
        self.tot_ore = 0
        self.tot_O3_ore = 0
        self.tot_H_ore = 0

        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        #setting title
        root.title("EuroTech Data Analyzer")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.GLabel_564=tk.Label(root)
        self.GLabel_564["bg"] = "#1e2226"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_564["font"] = ft
        self.GLabel_564["fg"] = "#333333"
        self.GLabel_564["justify"] = "center"
        self.GLabel_564["text"] = ""
        self.GLabel_564.place(x=0,y=60,width=600,height=440)

        self.GButton_656=tk.Button(root)
        self.GButton_656["anchor"] = "center"
        self.GButton_656["bg"] = "#393d49"
        self.GButton_656["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=13)
        self.GButton_656["font"] = ft
        self.GButton_656["fg"] = "#ffffff"
        self.GButton_656["justify"] = "center"
        self.GButton_656["text"] = "Upload"
        self.GButton_656["relief"] = "groove"
        self.GButton_656.place(x=200,y=370,width=200,height=45)
        self.GButton_656["command"] = self.GButton_656_command

        self.GLabel_868=tk.Label(root)
        self.GLabel_868["bg"] = "#1e2226"
        ft = tkFont.Font(family='Times',size=11)
        self.GLabel_868["font"] = ft
        self.GLabel_868["fg"] = "#ffffff"
        self.GLabel_868["justify"] = "center"
        self.GLabel_868["text"] = "Per iniziare caricare il file contenente i dati da analizzare."
        self.GLabel_868.place(x=120,y=335,width=356,height=30)

        self.GLabel_200=tk.Label(root)
        self.GLabel_200["bg"] = "#1e2226"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_200["font"] = ft
        self.GLabel_200["fg"] = "#fff4f4"
        self.GLabel_200["justify"] = "center"
        self.GLabel_200["text"] = "Marco Beltrame © 2021-2022"
        self.GLabel_200.place(x=0,y=470,width=166,height=30)

        self.GLabel_358=tk.Label(root)
        self.GLabel_358["bg"] = "#2b2e39"
        ft = tkFont.Font(family='Times',size=18)
        self.GLabel_358["font"] = ft
        self.GLabel_358["fg"] = "#ffffff"
        self.GLabel_358["justify"] = "center"
        self.GLabel_358["text"] = "EuroTech Data Analyzer"
        self.GLabel_358.place(x=0,y=0,width=600,height=70)

        self.GLabel_40=tk.Label(root)
        self.GLabel_899=tk.Label(root)
        self.GLabel_660=tk.Label(root)
        self.GLineEdit_24=tk.Entry(root)
        self.GLineEdit_906=tk.Entry(root)
        self.GLabel_660=tk.Label(root)
        self.GLineEdit_376=tk.Entry(root)
        self.GButton_853=tk.Button(root)
        self.grafico_giorni_btn=tk.Button(root)
        self.grafico_ore_btn=tk.Button(root)
        
    def show_fatt(self):
        self.GLabel_40["bg"] = "#1e2226"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_40["font"] = ft
        self.GLabel_40["fg"] = "#ffffff"
        self.GLabel_40["justify"] = "center"
        self.GLabel_40["text"] = f"Fattore di scala per {self.colonna_1}"
        self.GLabel_40.place(x=30,y=100,width=200,height=20)
        
        self.GLineEdit_24["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_24["font"] = ft
        self.GLineEdit_24["fg"] = "#000000"
        self.GLineEdit_24["justify"] = "center"
        self.GLineEdit_24["text"] = self.GLineEdit_24.insert(0, "")
        self.GLineEdit_24.place(x=30,y=120,width=200,height=35)
    
        self.GLabel_899["bg"] = "#1e2226"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_899["font"] = ft
        self.GLabel_899["fg"] = "#ffffff"
        self.GLabel_899["justify"] = "center"
        self.GLabel_899["text"] = f"Fattore di scala per {self.colonna_2}"
        self.GLabel_899.place(x=30,y=180,width=200,height=20)

        self.GLineEdit_906["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_906["font"] = ft
        self.GLineEdit_906["fg"] = "#000000"
        self.GLineEdit_906["justify"] = "center"
        self.GLineEdit_906["text"] =  self.GLineEdit_906.insert(0, "")
        self.GLineEdit_906.place(x=30,y=200,width=200,height=35)

        self.GLabel_660["bg"] = "#1e2226"
        ft = tkFont.Font(family='Times',size=10)
        self.GLabel_660["font"] = ft
        self.GLabel_660["fg"] = "#ffffff"
        self.GLabel_660["justify"] = "center"
        self.GLabel_660["text"] = f"Fattore di scala per {self.colonna_3}"
        self.GLabel_660.place(x=320,y=100,width=200,height=20)

        self.GLineEdit_376["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.GLineEdit_376["font"] = ft
        self.GLineEdit_376["fg"] = "#000000"
        self.GLineEdit_376["justify"] = "center"
        self.GLineEdit_376["text"] = self.GLineEdit_376.insert(0, "")
        self.GLineEdit_376.place(x=320,y=120,width=200,height=35)

        self.GButton_853["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=10)
        self.GButton_853["relief"] = "groove"
        self.GButton_853["font"] = ft
        self.GButton_853["fg"] = "#ffffff"
        self.GButton_853["justify"] = "center"
        self.GButton_853["text"] = "Inizia"
        self.GButton_853.place(x=320,y=200,width=200,height=35)
        self.GButton_853["command"] = self.GButton_853_command

    def show_grafici(self):
        self.grafico_giorni_btn["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=10)
        self.grafico_giorni_btn["relief"] = "groove"
        self.grafico_giorni_btn["font"] = ft
        self.grafico_giorni_btn["fg"] = "#ffffff"
        self.grafico_giorni_btn["justify"] = "center"
        self.grafico_giorni_btn["text"] = "Crea grafico giornaliero"
        self.grafico_giorni_btn.place(x=30,y=280,width=200,height=35)
        self.grafico_giorni_btn["command"] = self.crea_grafico_giorni

        self.grafico_ore_btn["bg"] = "#393d49"
        ft = tkFont.Font(family='Times',size=10)
        self.grafico_ore_btn["relief"] = "groove"
        self.grafico_ore_btn["font"] = ft
        self.grafico_ore_btn["fg"] = "#ffffff"
        self.grafico_ore_btn["justify"] = "center"
        self.grafico_ore_btn["text"] = "Crea grafico orario"
        self.grafico_ore_btn.place(x=320,y=280,width=200,height=35)
        self.grafico_ore_btn["command"] = self.crea_grafico_ore

    def GButton_656_command(self):
        print("button")
        self.dati = filedialog.askopenfilename()
        if self.dati[-4:] != ".csv":
            self.GLabel_868.config(text="Il formato del file è invalido! (Utilizzare file '.csv')")
        elif self.dati[-4:] == ".csv":
            self.GLabel_868.config(text="Il file è stato caricato con successo!")
            print(self.dati)
            self.setup()
            self.get_column_names()
            self.show_fatt()

    def GButton_853_command(self):
        self.fattore_scala_1 = self.GLineEdit_24.get()
        self.fattore_scala_2 = self.GLineEdit_906.get()
        self.fattore_scala_3 = self.GLineEdit_376.get()
        if self.fattore_scala_1.replace(".","",1).isdigit() == False or self.fattore_scala_2.replace(".","",1).isdigit() == False or self.fattore_scala_1.replace(".","",1).isdigit() == False:
            self.GLabel_868.config(text="Uno o più dei valori inseriti è invalido.")
        else:
            self.GLabel_868.config(text="Analizzando i dati . . .")
            try:
                self.GLabel_868.config(text="Analizzando i dati . . .")
                self.menu()
                self.Divisore_giorni()
                self.Media_giorni()
                self.Divisore_ore()
                self.Media_ore()
                self.show_grafici()
                self.GLabel_868.config(text="Dati analizzati con successo!")
            except Exception as error:
                self.GLabel_868.config(text=error)

    def Divisore_giorni(self):
        with open(self.dati, "r") as f:
            self.lines = f.readlines()
        for i in range(1,31):
            if i < 10:
                i = "0" + str(i)
            else:
                i = str(i)         
            with open(os.path.join(self.cwd, "giorni", f"{i}.csv"), "w") as f1:
                f1.write(f'Timestamp (UTC){self.sep}{self.colonna_1}{self.sep}{self.colonna_2}{self.sep}{self.colonna_3}\n')
                print(f"File creato: {i}.csv")
            for line in self.lines:
                for i in range(1, 31):
                    if i < 10:
                        i = "0" + str(i)
                    else:
                        i = str(i)  
                    if (line[3] + line[4]) == i:
                        with open(os.path.join(self.cwd, "giorni", f"{i}.csv"), "a") as f1:
                            f1.write(line)

    def setup(self):
        for dir in self.dirs:
            if os.path.exists(os.path.join(self.cwd, dir)) == False:
                os.system(f"md {dir}")
            else:
                print(f"[*] '{dir}' already exists.")
        
    def get_column_names(self):
        try:
            with open(self.dati, "r") as f:
                self.lines = f.readlines()
        except:
            print(f"[!] Impossibile trovare il file '{self.dati}'!")
            print("[*] Assicurarsi che i dati siano nella cartella 'dati'.")
            self.get_column_names()
        self.sep = self.lines[0][15]
        self.lines = self.lines[0]
        self.lines = self.lines.split(self.sep)

        self.colonna_1 = self.lines[1]
        self.colonna_2 = self.lines[2]
        self.colonna_3 = self.lines[3]
        self.colonna_3 = self.colonna_3.rstrip("\n")

        self.GLabel_40.config(text=f"Fattore di scala per {self.colonna_1}")
        self.GLabel_899.config(text=f"Fattore di scala per {self.colonna_2}")
        self.GLabel_660.config(text=f"Fattore di scala per {self.colonna_3}")

    def Media_giorni(self):
        with open(os.path.join(self.cwd, "dati", "media_giorni.csv"), "w") as f:
            f.write(f'Giorno{self.sep}{self.colonna_1}{self.sep}{self.colonna_2}{self.sep}{self.colonna_3}\n')

        for i in range(1, 31):

            self.media_giorni.clear()
            self.media_O3_giorni.clear()
            self.media_H_giorni.clear()
            self.tot_giorni = 0
            self.tot_O3_giorni = 0
            self.tot_H_giorni = 0
            
            if i < 10:
                i = "0" + str(i)
            try:
                with open(os.path.join(self.cwd, "giorni", f"{i}.csv"), "r") as f:
                    self.lines = f.readlines()
                    for line in self.lines:
                        if line == self.lines[0]:
                            pass
                        else:
                            self.dato_giorni = line.split(self.sep)
                            self.media_giorni.append(self.dato_giorni[1])
                            self.media_O3_giorni.append(self.dato_giorni[2])
                            self.media_H_giorni.append(self.dato_giorni[3])

                for x in range(len(self.media_giorni)):
                    try:
                        self.tot_giorni += float(self.media_giorni[x])
                    except:
                        print("[!] Dato invalido")
                try:
                    self.tot_giorni = self.tot_giorni / (len(self.lines) - 1)
                except ZeroDivisionError:
                    print("[!] Dato non trovato")

                for x in range(len(self.media_O3_giorni)):
                    try:
                        self.tot_O3_giorni += float(self.media_O3_giorni[x])
                    except:
                        print("[!] Dato invalido")
                try:
                    self.tot_O3_giorni = self.tot_O3_giorni / (len(self.lines) - 1)
                except ZeroDivisionError:
                    print("[!] Dato non trovato")

                for x in range(len(self.media_H_giorni)):
                    try:
                        self.tot_H_giorni += float(self.media_H_giorni[x])
                    except:
                        print("[!] Dato invalido")
                try:
                    self.tot_H_giorni = self.tot_H_giorni / (len(self.lines) - 1)
                except ZeroDivisionError:
                    print("[!] Dato non trovato")

                with open(os.path.join(self.cwd, "dati", "media_giorni.csv"), "a") as f:
                    f.write(f'{int(i)}{self.sep}{self.tot_giorni*self.fattore_scala_1}{self.sep}{self.tot_O3_giorni*self.fattore_scala_2}{self.sep}{self.tot_H_giorni*self.fattore_scala_3}\n')
            
            except FileNotFoundError:
                print(f"File not Found: giorni/{i}.csv | Passing . .")
                pass

    def Divisore_ore(self):
        with open(self.dati, "r") as f:
            self.lines = f.readlines()
        for i in range(1,31):
            if i < 10:
                i = "0" + str(i)
            else:
                i = str(i)         
            with open(os.path.join(self.cwd, "ore", f"{i}.csv"), "w") as f1:
                f1.write(f'Timestamp (UTC){self.sep}{self.colonna_1}{self.sep}{self.colonna_2}{self.sep}{self.colonna_3}\n')
                print(f"File creato: {i}.csv")
        for line in self.lines:
            for i in range(0, 24):
                if i < 10:
                    i = "0" + str(i)
                else:
                    i = str(i)
                if (line[11] + line[12]) == i:
                    with open(os.path.join(self.cwd, "ore", f"{i}.csv"), "a") as f1:
                        f1.write(line) 

    def Media_ore(self):
        with open(os.path.join(self.cwd, "dati", "media_ore.csv"), "w") as f:
            f.write(f'Ora{self.sep}{self.colonna_1}{self.sep}{self.colonna_2}{self.sep}{self.colonna_3}\n')

        for i in range(0, 24):

            self.media_ore.clear()
            self.media_O3_ore.clear()
            self.media_H_ore.clear()
            self.tot_H_ore = 0
            self.tot_O3_ore = 0
            self.tot_ore = 0

            if i < 10:
                i = "0" + str(i)
            try:
                with open(os.path.join(self.cwd, "ore", f"{i}.csv"), "r") as f:
                    self.lines = f.readlines()
                    print(self.lines)
                    for line in self.lines:
                        if line == self.lines[0]:
                            pass
                        else:
                            self.dato_ore = line.split(self.sep)
                            try:
                                self.media_ore.append(self.dato_ore[1])
                                self.media_O3_ore.append(self.dato_ore[2])
                                self.media_H_ore.append(self.dato_ore[3])
                            except:
                                print("Dato non trovato")
                                pass

                    for x in range(len(self.media_ore)):
                        print(f"{self.colonna_1}: {self.media_H_ore[x]}")
                        try:
                            self.tot_ore += float(self.media_ore[x])
                        except:
                            print("[!] Valore invalido")
                    try:
                        self.tot_ore = self.tot_ore / (len(self.lines) - 1)
                    except:
                        pass

                    for x in range(len(self.media_O3_ore)):
                        print(f"{self.colonna_2}: {self.media_H_ore[x]}")
                        try:
                            self.tot_O3_ore += float(self.media_O3_ore[x])
                        except:
                            print("[!] Valore invalido")
                    try:
                        self.tot_O3_ore = self.tot_O3_ore / (len(self.lines) - 1)
                    except:
                        pass

                    for x in range(len(self.media_H_ore)):
                        print(f"{self.colonna_3}: {self.media_H_ore[x]}")
                        try:
                            self.tot_H_ore += float(self.media_H_ore[x])
                        except:
                            print("[!] Valore invalido")
                    try:
                        self.tot_H_ore = self.tot_H_ore / (len(self.lines) - 1)
                    except:
                        pass


                with open(os.path.join(self.cwd, "dati", "media_ore.csv"), "a") as f:
                    f.write(f'{int(i)}{self.sep}{self.tot_ore*self.fattore_scala_1}{self.sep}{self.tot_O3_ore*self.fattore_scala_2}{self.sep}{self.tot_H_ore*self.fattore_scala_3}\n')
                    
            except FileNotFoundError:
                print(f"File not Found: giorni/{i}.csv | Passing . .")
                pass

    def crea_grafico_ore(self):
        
        print(self.colonna_1,self.colonna_2,self.colonna_3)
        self.df = pd.read_csv(os.path.join(self.cwd, "dati", "media_ore.csv"), sep=self.sep)
        print(self.df)

        self.data = self.df["Ora"]
        self.NO2 = self.df[self.colonna_1]
        self.O3 = self.df[self.colonna_2]
        self.H = self.df[self.colonna_3]
        print(self.data)
        plt.style.use("classic")
        self.x = plt.xlabel("Ora", fontsize=18)
        self.y = plt.ylabel(f"{self.colonna_1} - {self.colonna_2} - {self.colonna_3}", fontsize=16)
        plt.plot(self.data, self.NO2, label=self.colonna_1)
        plt.plot(self.data, self.O3, label=self.colonna_2)
        plt.plot(self.data, self.H, label=self.colonna_3)

        plt.legend()
        plt.show()

    def crea_grafico_giorni(self):

        self.df = pd.read_csv(os.path.join(self.cwd, "dati", "media_giorni.csv"), sep=self.sep)
        os.system("cls")
        print(self.df)

        self.data = self.df["Giorno"]
        self.NO2 = self.df[self.colonna_1]
        self.O3 = self.df[self.colonna_2]
        self.H = self.df[self.colonna_3]
        print(self.data)
        plt.style.use("classic")
        self.x = plt.xlabel("Giorno", fontsize=18)
        self.y = plt.ylabel(f"{self.colonna_1} - {self.colonna_2} - {self.colonna_3}", fontsize=16)
        plt.plot(self.data, self.NO2, label=self.colonna_1)
        plt.plot(self.data, self.O3, label=self.colonna_2)
        plt.plot(self.data, self.H, label=self.colonna_3)

        plt.legend()
        plt.show()

    def menu(self):
        print(self.fattore_scala_1)
        if self.fattore_scala_1 != "":
            try:
                self.fattore_scala_1 = int(self.fattore_scala_1)
            except:
                self.fattore_scala_1 = float(self.fattore_scala_1)
        else:
            self.fattore_scala_1 == float(1)
        print(self.fattore_scala_1)
        if self.fattore_scala_2 != "":
            try:
                self.fattore_scala_2 = int(self.fattore_scala_2)
            except:
                self.fattore_scala_2 = float(self.fattore_scala_2)
        else:
            self.fattore_scala_2 == float(1)

        if self.fattore_scala_3 != "":
            try:
                self.fattore_scala_3 = int(self.fattore_scala_3)
            except:
                self.fattore_scala_3 = float(self.fattore_scala_3)
        else:
            self.fattore_scala_3 == float(1)
        
        print("Ft:", self.fattore_scala_1,self.fattore_scala_2,self.fattore_scala_3)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

