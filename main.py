import tkinter
import customtkinter
import requests


# récupére les élement de data.txt 
data_file = open("data.txt")
dlist = data_file.readlines()
dlist = [element.replace('\n', '') for element in dlist]

print(dlist)
print(len(dlist))
data_file.close()

#les different chemin d'accés au applis
path1  = [ dlist[1],  dlist[2]  ]
path2  = [ dlist[4],  dlist[5]  ]
path3  = [ dlist[7],  dlist[8]  ]
path4  = [ dlist[10], dlist[11] ]
path5  = [ dlist[13], dlist[14] ]
path6  = [ dlist[16], dlist[17] ]
path7  = [ dlist[19], dlist[20] ]
path8  = [ dlist[22], dlist[23] ]
path9  = [ dlist[25], dlist[26] ]
path10 = [ dlist[28], dlist[29] ]

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
#Verifie la version de l'app (requete azarma.cf)
    app_version = "1.1"
    serv_version = requests.get("https://azarma.000webhostapp.com/app-version.txt")
    print(serv_version.text)
    
    def update_toplevel():
        global app_version
        window = customtkinter.CTkToplevel()
        window.title("Atlas Manager have an update!")
        window.geometry("300x100")

        # create label on CTkToplevel window
        label = customtkinter.CTkLabel(window, text="Your current Atlas Manager version " + app_version)
        label.pack(side="top", fill="both", expand=True, padx=10, pady=10)
        label2 = customtkinter.CTkLabel(window, text="Lastest version online " + serv_version)
        label2.pack(side="top", fill="both", expand=True, padx=10, pady=20)


    if serv_version != app_version:
        update_toplevel()
        print("marche pas égal")    
        
        # configure window
        self.title("Atlas Manager")
        self.geometry(f"{1100}x{580}")
        self.minsize(1100,580)
        self.maxsize(1100,580)
        self.iconbitmap("Atlas-white.ico")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Atlas Manager", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="About", command=self.about_toplevel)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Reset", command=self.sidebar_button_reset, state="disabled")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%", "150%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        #Main area
        
        #1 rangée de slots 1 nombre = rangé | 2 nombre = id
        self.game_frame1_1 = customtkinter.CTkFrame(self, width=150,height=150, corner_radius=10)
        self.game_frame1_1.place(relx=0.175, rely=0.04)
        self.game1_label = customtkinter.CTkLabel(self.game_frame1_1, text=path1[1], anchor="center", font=("",17))
        self.game1_label.place(relx=0.25, rely=0.11)
        self.game1_start = customtkinter.CTkButton(self.game_frame1_1, text="Start ▷", command=self.start_slot1)
        self.game1_start.place(relx=0.03, rely=0.45 )
        self.edit1_start = customtkinter.CTkButton(self.game_frame1_1, width=70, height=30, text="Edit Path", command=self.path_edit1)
        self.edit1_start.place(relx=0.02, rely=0.7 )
        self.edit1_start = customtkinter.CTkButton(self.game_frame1_1, width=70, height=30, text="Edit Name", command=self.name_edit1)
        self.edit1_start.place(relx=0.50, rely=0.7 )
       #self.game_frame1_1.grid(row=1, column=1, rowspan=1)
        
        self.game_frame1_2 = customtkinter.CTkFrame(self, width=150,height=150, corner_radius=10)
        self.game_frame1_2.place(relx=0.325, rely=0.04)
        self.game2_label = customtkinter.CTkLabel(self.game_frame1_2, text=path2[1], anchor="center", font=("",17))
        self.game2_label.place(relx=0.25, rely=0.11)
        self.game2_start = customtkinter.CTkButton(self.game_frame1_2, text="Start ▷", command=self.start_slot2)
        self.game2_start.place(relx=0.03, rely=0.45)
        self.edit2_start = customtkinter.CTkButton(self.game_frame1_2, width=70, height=30, text="Edit Path", command=self.path_edit2)
        self.edit2_start.place(relx=0.02, rely=0.7 )
        self.edit2_start = customtkinter.CTkButton(self.game_frame1_2, width=70, height=30, text="Edit Name", command=self.name_edit2)
        self.edit2_start.place(relx=0.50, rely=0.7 )
        
        self.game_frame1_3 = customtkinter.CTkFrame(self, width=150,height=150, corner_radius=10)
        self.game_frame1_3.place(relx=0.475, rely=0.04)
        self.game3_label = customtkinter.CTkLabel(self.game_frame1_3, text=path3[1], anchor="center", font=("",17))
        self.game3_label.place(relx=0.25, rely=0.11)
        self.game3_start = customtkinter.CTkButton(self.game_frame1_3, text="Start ▷", command=self.start_slot3)
        self.game3_start.place(relx=0.03, rely=0.45)
        self.edit3_start = customtkinter.CTkButton(self.game_frame1_3, width=70, height=30, text="Edit Path", command=self.path_edit3)
        self.edit3_start.place(relx=0.02, rely=0.7 )
        self.edit3_start = customtkinter.CTkButton(self.game_frame1_3, width=70, height=30, text="Edit Name", command=self.name_edit3)
        self.edit3_start.place(relx=0.50, rely=0.7 )
        
        
        self.game_frame1_4 = customtkinter.CTkFrame(self, width=150,height=150, corner_radius=10)
        self.game_frame1_4.place(relx=0.625, rely=0.04)
        self.game4_label = customtkinter.CTkLabel(self.game_frame1_4, text=path4[1], anchor="center", font=("",17))
        self.game4_label.place(relx=0.25, rely=0.11)
        self.game4_start = customtkinter.CTkButton(self.game_frame1_4, text="Start ▷", command=self.start_slot4)
        self.game4_start.place(relx=0.03, rely=0.45)
        self.edit4_start = customtkinter.CTkButton(self.game_frame1_4, width=70, height=30, text="Edit Path", command=self.path_edit4)
        self.edit4_start.place(relx=0.02, rely=0.7 )
        self.edit4_start = customtkinter.CTkButton(self.game_frame1_4, width=70, height=30, text="Edit Name", command=self.name_edit4)
        self.edit4_start.place(relx=0.50, rely=0.7 )
        
        self.game_frame1_5 = customtkinter.CTkFrame(self, width=150,height=150, corner_radius=10)
        self.game_frame1_5.place(relx=0.775, rely=0.04)
        self.game5_label = customtkinter.CTkLabel(self.game_frame1_5, text=path5[1], anchor="center", font=("",17))
        self.game5_label.place(relx=0.25, rely=0.11)
        self.game5_start = customtkinter.CTkButton(self.game_frame1_5, text="Start ▷", command=self.start_slot5)
        self.game5_start.place(relx=0.03, rely=0.45)
        self.edit5_start = customtkinter.CTkButton(self.game_frame1_5, width=70, height=30, text="Edit Path", command=self.path_edit5)
        self.edit5_start.place(relx=0.02, rely=0.7 )
        self.edit5_start = customtkinter.CTkButton(self.game_frame1_5, width=70, height=30, text="Edit Name", command=self.name_edit5)
        self.edit5_start.place(relx=0.50, rely=0.7 )
        
        #_________________2 rangée_________________
        
        self.game_frame2_1 = customtkinter.CTkFrame(self, width=150,height=150, corner_radius=10)
        self.game_frame2_1.place(relx=0.175, rely=0.340)
        self.game6_label = customtkinter.CTkLabel(self.game_frame2_1, text=path6[1], anchor="center", font=("",17))
        self.game6_label.place(relx=0.25, rely=0.11)
        self.game6_start = customtkinter.CTkButton(self.game_frame2_1, text="Start ▷", command=self.start_slot6)
        self.game6_start.place(relx=0.03, rely=0.45)
        self.edit6_start = customtkinter.CTkButton(self.game_frame2_1, width=70, height=30, text="Edit Path", command=self.path_edit6)
        self.edit6_start.place(relx=0.02, rely=0.7 )
        self.edit6_start = customtkinter.CTkButton(self.game_frame2_1, width=70, height=30, text="Edit Name", command=self.name_edit6)
        self.edit6_start.place(relx=0.50, rely=0.7 )
 
        self.game_frame2_2 = customtkinter.CTkFrame(self, width=150,height=150, corner_radius=10)
        self.game_frame2_2.place(relx=0.325, rely=0.340)
        self.game7_label = customtkinter.CTkLabel(self.game_frame2_2, text=path7[1], anchor="center", font=("",17))
        self.game7_label.place(relx=0.25, rely=0.11)
        self.game7_start = customtkinter.CTkButton(self.game_frame2_2, text="Start ▷", command=self.start_slot7)
        self.game7_start.place(relx=0.03, rely=0.45)
        self.edit7_start = customtkinter.CTkButton(self.game_frame2_2, width=70, height=30, text="Edit Path", command=self.path_edit7)
        self.edit7_start.place(relx=0.02, rely=0.7 )
        self.edit7_start = customtkinter.CTkButton(self.game_frame2_2, width=70, height=30, text="Edit Name", command=self.name_edit7)
        self.edit7_start.place(relx=0.50, rely=0.7 )

        self.game_frame2_3 = customtkinter.CTkFrame(self, width=150,height=150, corner_radius=10)
        self.game_frame2_3.place(relx=0.475, rely=0.340)
        self.game8_label = customtkinter.CTkLabel(self.game_frame2_3, text=path8[1], anchor="center", font=("",17))
        self.game8_label.place(relx=0.25, rely=0.11)
        self.game8_start = customtkinter.CTkButton(self.game_frame2_3, text="Start ▷", command=self.start_slot8)
        self.game8_start.place(relx=0.03, rely=0.45)
        self.edit8_start = customtkinter.CTkButton(self.game_frame2_3, width=70, height=30, text="Edit Path", command=self.path_edit8)
        self.edit8_start.place(relx=0.02, rely=0.7 )
        self.edit8_start = customtkinter.CTkButton(self.game_frame2_3, width=70, height=30, text="Edit Name", command=self.name_edit8)
        self.edit8_start.place(relx=0.50, rely=0.7 )
        
        self.game_frame2_4 = customtkinter.CTkFrame(self, width=150,height=150, corner_radius=10)
        self.game_frame2_4.place(relx=0.625, rely=0.340)
        self.game9_label = customtkinter.CTkLabel(self.game_frame2_4, text=path9[1], anchor="center", font=("",17))
        self.game9_label.place(relx=0.25, rely=0.11)
        self.game9_start = customtkinter.CTkButton(self.game_frame2_4, text="Start ▷", command=self.start_slot9)
        self.game9_start.place(relx=0.03, rely=0.45)
        self.edit9_start = customtkinter.CTkButton(self.game_frame2_4, width=70, height=30, text="Edit Path", command=self.path_edit9)
        self.edit9_start.place(relx=0.02, rely=0.7 )
        self.edit9_start = customtkinter.CTkButton(self.game_frame2_4, width=70, height=30, text="Edit Name", command=self.name_edit9)
        self.edit9_start.place(relx=0.50, rely=0.7 )
        
        self.game_frame2_5 = customtkinter.CTkFrame(self, width=150,height=150, corner_radius=10)
        self.game_frame2_5.place(relx=0.775, rely=0.340)
        self.game10_label = customtkinter.CTkLabel(self.game_frame2_5, text=path10[1], anchor="center", font=("",17))
        self.game10_label.place(relx=0.25, rely=0.11)
        self.game10_start = customtkinter.CTkButton(self.game_frame2_5, text="Start ▷", command=self.start_slot10)
        self.game10_start.place(relx=0.03, rely=0.45)
        self.edit10_start = customtkinter.CTkButton(self.game_frame2_5, width=70, height=30, text="Edit Path", command=self.path_edit10)
        self.edit10_start.place(relx=0.02, rely=0.7 )
        self.edit10_start = customtkinter.CTkButton(self.game_frame2_5, width=70, height=30, text="Edit Name", command=self.name_edit10)
        self.edit10_start.place(relx=0.50, rely=0.7 )

        # set default values
        
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
        print(new_appearance_mode)
        if new_appearance_mode == "Light":
            self.iconbitmap("Atlas-black.ico")
        else:
            self.iconbitmap("Atlas-white.ico")


    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)


    
    def sidebar_button_reset(self):
        print("reset button click")
 
    def about_toplevel(self):
        window = customtkinter.CTkToplevel(self)
        window.title("About Atlas Manager")
        window.geometry("300x100")

        # create label on CTkToplevel window
        label = customtkinter.CTkLabel(window, text="Atlas Manager version " + app_version)
        label.pack(side="top", fill="both", expand=True, padx=10, pady=10)
        label2 = customtkinter.CTkLabel(window, text="Coded by Azarma#4670")
        label2.pack(side="top", fill="both", expand=True, padx=10, pady=20)
    
 
#Definition des fonction d'excecution des application

    def start_slot1(self):
        global path1
        os.startfile(path1[0])
        print("Slot 1 lancer")

    def start_slot2(self):
        global path2
        os.startfile(path2[0])
        print("Slot 2 lancer")
        
    def start_slot3(self):
        global path3
        os.startfile(path3[0])
        print("Slot 3 lancer")

    def start_slot4(self):
        global path4
        os.startfile(path4[0])
        print("Slot 4 lancer")

    def start_slot5(self):
        global path5
        os.startfile(path5[0])
        print("Slot 5 lancer")

    def start_slot6(self):
        global path6
        os.startfile(path6[0])
        print("Slot 6 lancer")

    def start_slot7(self):
        global path7
        os.startfile(path7[0])
        print("Slot 7 lancer")
        
    def start_slot8(self):
        global path8
        os.startfile(path8[0])
        print("Slot 8 lancer")
        
    def start_slot9(self):
        global path9
        os.startfile(path9[0])
        print("Slot 9 lancer")
        
    def start_slot10(self):
        global path10
        os.startfile(path10[0])
        print("Slot 10 lancer")
        
    #definition des edit path
        
    def path_edit1(self):
        global path1, dlist
        print("Edit path 1  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the file path. current path : " + str(path1[0]), title="Edit path")
        dlist[1] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        print(dlist)
        path1[0] = dlist[1]
        return path1, dlist
    
    def path_edit2(self):
        global path2
        print("Edit path 2  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the file path. current path : " + str(path2[0]), title="Edit path")
        dlist[4] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        path2[0] = dlist[4]
        return path2
        
    def path_edit3(self):
        global path3
        print("Edit path 3  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the file path. current path : " + str(path3[0]), title="Edit path")
        dlist[7] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        path3[0] = dlist[7]
        return path3
    
    def path_edit4(self):
        global path4
        print("Edit path 4  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the file path. current path : " + str(path4[0]), title="Edit path")
        dlist[10] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        path4[0] = dlist[10]
        return path4
        
    def path_edit5(self):
        global path5
        print("Edit path 5  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the file path. current path : " + str(path5[0]), title="Edit path")
        dlist[13] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        path5[0] = dlist[13]
        return path5
        
    def path_edit6(self):
        global path6
        print("Edit path 6  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the file path. current path : " + str(path6[0]), title="Edit path")
        dlist[16] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        path6[0] = dlist[16]
        return path6
        
    def path_edit7(self):
        global path7
        print("Edit path 7  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the file path. current path : " + str(path7[0]), title="Edit path")
        dlist[19] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        path7[0] = dlist[19]
        return path7
        
    def path_edit8(self):
        global path8
        print("Edit path 8  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the file path. current path : " + str(path8[0]), title="Edit path")
        dlist[22] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        path8[0] = dlist[22]
        return path8
        
    def path_edit9(self):
        global path9
        print("Edit path 9  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the file path. current path : " + str(path9[0]), title="Edit path")
        dlist[25] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        path9[0] = dlist[25]
        return path9
        
    def path_edit10(self):
        global path10
        print("Edit path 10  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the file path. current path : " + str(path10[0]), title="Edit path")
        dlist[28] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        path10[0] = dlist[28]
        return path10
    
    #Name edit :
    
    def name_edit1(self):
        global path1, game1_label, dlist
        print("Edit name 1  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the Name. current name : " + path1[1], title="Edit Name")
        dlist[2] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        self.game1_label.configure(text=dlist[2])
        return path1,dlist
  
    def name_edit2(self):
        global path2, game2_label
        print("Edit name 2  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the Name. current name : " + path2[1], title="Edit Name")
        dlist[5] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        self.game2_label.configure(text=dlist[5])
        return path2

    def name_edit3(self):
        global path3, game3_label
        print("Edit name 3 lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the Name. current name : " + path3[1], title="Edit Name")
        dlist[8] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        self.game3_label.configure(text=dlist[8])
        return path3
    
    def name_edit4(self):
        global path4, game4_label
        print("Edit name 4  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the Name. current name : " + path4[1], title="Edit Name")
        dlist[11] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        self.game4_label.configure(text=dlist[11])
        return path4


    def name_edit5(self):
        global path5, game5_label
        print("Edit name 5  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the Name. current name : " + path5[1], title="Edit Name")
        dlist[14] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        self.game5_label.configure(text=dlist[14])
        return path5
    
    def name_edit6(self):
        global path6, game6_label
        print("Edit name 6  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the Name. current name : " + path6[1], title="Edit Name")
        dlist[17] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        self.game6_label.configure(text=dlist[17])
        return path6

    def name_edit7(self):
        global path7, game7_label
        print("Edit name 7  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the Name. current name : " + path7[1], title="Edit Name")
        dlist[20] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        self.game7_label.configure(text=dlist[20])
        return path7
    
    def name_edit8(self):
        global path8, game8_label
        print("Edit name 8  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the Name. current name : " + path8[1], title="Edit Name")
        dlist[23] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        self.game8_label.configure(text=dlist[23])
        return path8
    
    def name_edit9(self):
        global path9, game9_label
        print("Edit name 9  lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the Name. current name : " + path9[1], title="Edit Name")
        dlist[26] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        self.game9_label.configure(text=dlist[26])
        return path9
    
    def name_edit10(self):
        global path10, game10_label
        print("Edit name 10 lancer")
        dialog = customtkinter.CTkInputDialog(text="Change the Name. current name : " + path10[1], title="Edit Name")
        dlist[29] = dialog.get_input()
        data_file = open("data.txt", "w")
        for items in dlist:
            data_file.write('%s\n' %items)
        data_file.close()
        self.game10_label.configure(text=dlist[29])
        return path10

if __name__ == "__main__":
    app = App()
    app.mainloop()