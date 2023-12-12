import os
import time
import customtkinter


customtkinter.set_appearance_mode("System")

class mainContent(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, *args, **kwargs, fg_color="gray12")
        self.grid(row=0, column=1, sticky="nsew")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1,2), weight=1) #row 4 not weight 1 for the entry

    def show(self):
        self.lift()

class welcomeContent(mainContent):
    def __init__(self, *args, **kwargs):
        mainContent.__init__(self, *args, **kwargs)
        self.welcome = customtkinter.CTkLabel(self, text="Welcome, " + os.getlogin(), font=customtkinter.CTkFont(size=30, weight="bold"))
        self.welcome.grid(row=1, column=0)

class downloadingContent(mainContent):
    def __init__(self, *args, **kwargs):
        mainContent.__init__(self, *args, **kwargs)

        self.download_description = customtkinter.CTkTextbox(self, width=400, height=200, font=customtkinter.CTkFont(size=15))
        self.download_description.insert("0.0","Automatically shutdown PC after download has finished successfully.\nPlease enter the file path below.")
        self.download_description.grid(row=0, column=0, padx=20, pady=20)

        self.download_list = customtkinter.CTkLabel(self, text="Downloads", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.download_list.grid(row=0, column=1, padx=20, pady=20)


        self.entry = customtkinter.CTkEntry(self, placeholder_text="File path")
        self.entry.grid(row=3, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")
        self.entry.bind("<Return>", self.check_download)
    
    def check_download(self, parameter):
        filepath = self.entry.get()
        if filepath == "test":
            print("hsihsoi")
            return 1
        
        while True:
            if os.path.exists(filepath):
                break
            else:
                filepath = input("Path doesn't exist. Please enter a valid file path: ")
        
        downloading = True
        while downloading:
            old_mods = os.path.getmtime(filepath)
            old_size = os.path.getsize(filepath)
            time.sleep(60*5)
            new_mods = os.path.getmtime(filepath)
            new_size = os.path.getsize(filepath)

            if old_size == new_size and old_mods == new_mods:
                downloading == False
                shutdown()


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("900x300")

        self.grid_columnconfigure(1, weight=1) #weight 1 means it fills all the space compared to weight 0, so this column is wider
        
        self.grid_rowconfigure(0, weight=1)
        self.welcome_frame = welcomeContent(self)
        self.download_frame = downloadingContent(self)

        self.sidebar = customtkinter.CTkFrame(self, width=140)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar.grid_rowconfigure(4, weight=1)
        
        self.functions = customtkinter.CTkLabel(self.sidebar, text="Functions", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.functions.grid(row=0, column=0, padx=20, pady=(20,10))
        
        self.downloads = customtkinter.CTkButton(self.sidebar, text="Downloads", command=self.download_frame.show)
        self.downloads.grid(row=1, column=0, padx=20, pady=10)


        

        self.welcome_frame.show()


    def button_pressed():
        print("shit")

    def testingshi(self, parameter):
        print(self.entry.get())#idk how to make the function call for return work

    def download_content(self):
        self.entry = customtkinter.CTkEntry(self, placeholder_text="File path")
        self.entry.grid(row=3, column=1, columnspan=2, padx=20, pady=(20,20), sticky="nsew")
        self.entry.bind("<Return>", self.check_download)





root_tk = customtkinter.CTk()

frame = customtkinter.CTkFrame(master=root_tk)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Welcome, " + os.getlogin())
label.pack(pady=12, padx=10)




def shutdown():
    if os.name == "nt":
        os.system("shutdown /s /t 1")
    
    elif os.name == "posix":
        os.system("sudo shutdown now")

    else:
        print("Shutdown not possible due to unrecognized operating system.")




def main():
    """Create an instance of the class."""
    print("Welcome, " + os.getlogin())
    app = App()
    app.mainloop()
    #check_download()
    


if __name__ == "__main__":
    main()
