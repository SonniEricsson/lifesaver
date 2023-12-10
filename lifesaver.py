import os
import time
import customtkinter


customtkinter.set_appearance_mode("System")



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x300")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar = customtkinter.CTkFrame(self, width=140)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar.grid_rowconfigure(4, weight=1)
        
        self.functions = customtkinter.CTkLabel(self.sidebar, text="Functions", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.functions.grid(row=0, column=0, padx=20, pady=(20,10))
        
        self.downloads = customtkinter.CTkButton(self.sidebar, text="Downloads", command=self.download_content)
        self.downloads.grid(row=1, column=0, padx=20, pady=10)

        self.welcome = customtkinter.CTkLabel(self, text="Welcome, " + os.getlogin(), font=customtkinter.CTkFont(size=30, weight="bold"))
        self.welcome.grid(row=0, column=1)

    def button_pressed():
        print("shit")

        

    def download_content(self):
        self.entry = customtkinter.CTkEntry(self, placeholder_text="File path")
        self.entry.grid(row=3, column=1, columnspan=2, padx=20, pady=(20,20), sticky="nsew")
        self.entry.bind("<Return>", self.testingshi)

    def testingshi(self):
        print("shishsi")#idk how to make the function call for return work



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

def check_download(self):
    filepath = self.entry.get()
    if filepath == "test":
        print("hsihsoi")
        return 1
    
    while True:
        if os.path.exists(filepath):
            break
        #else:
        #    filepath = input("Path doesn't exist. Please enter a valid file path: ")
    
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


def main():
    """Create an instance of the class."""
    print("Welcome, " + os.getlogin())
    app = App()
    app.mainloop()
    #check_download()
    


if __name__ == "__main__":
    main()
