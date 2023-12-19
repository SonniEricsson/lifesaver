import os
import time
import customtkinter
import tkinter as tk


customtkinter.set_appearance_mode("System")

class mainContent(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        customtkinter.CTkFrame.__init__(self, *args, **kwargs, fg_color="transparent")
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
        
        self.download_description = customtkinter.CTkLabel(self, text="Automatically shutdown PC after download has finished successfully.\nPlease enter the file path below.", font=customtkinter.CTkFont(size=15), wraplength=500)
        self.download_description.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

        #self.download_list = customtkinter.CTkLabel(self, text="Downloads", font=customtkinter.CTkFont(size=20, weight="bold"))
        #self.download_list.grid(row=0, column=1, padx=20, pady=20)

        self.check_path = customtkinter.CTkLabel(self, text="", font=customtkinter.CTkFont(size=15))
        self.check_path.grid(row=2, column=0, padx=20)

        self.entry = customtkinter.CTkEntry(self, placeholder_text="File path")
        self.entry.grid(row=3, column=0, columnspan=2, padx=20, pady=20, sticky="nsew")
        self.entry.bind("<Return>", self.check_download)

        #self.cancel = customtkinter.CTkButton(self, text="Cancel shutdown")
        #self.cancel.grid(row=3, column=2, padx=(0,20), pady=20, sticky="nsew")

        self.counter = 0
        self.counter2 = 0
        self.filepath = 0
        self.size_comparison = [] #index 0 is old mod, index 1 is old size, index 2 is new mod, index 3 is new size
    
    def check_download(self, parameter):
        self.filepath = self.entry.get()
        
        self.after(0, self.checking_path)
        
        
        #print("test")
        #if old_size == new_size:
        #    self.check_path.configure(text="File path has been found.\nNo current download.")
        #else:
        #    downloading = False
        #    while downloading:
        #        old_mods = os.path.getmtime(self.filepath)
        #        old_size = os.path.getsize(self.filepath)
        #        #time.sleep(60*2)
        #        self.update_download1()
        #        self.counter = 0
        #        new_mods = os.path.getmtime(self.filepath)
        #        new_size = os.path.getsize(self.filepath)

        #        if old_size == new_size and old_mods == new_mods:
        #            downloading == False
        #            self.check_path.configure(text="Download has completed. Shutting down...")
        #            time.sleep(30)
        #            #shutdown()
    def update_sizes(self):
        self.size_comparison.append(os.path.getmtime(self.filepath)) 
        self.size_comparison.append(os.path.getsize(self.filepath))
        if len(self.size_comparison) == 4:
            if self.size_comparison[1] == self.size_comparison[3]: #no download progression
                self.check_path.configure(text="Download has completed. Shutting down...")
                #self.after(30000, self.shutdown)
            else:
                self.size_comparison.pop() #reset list
                self.size_comparison.pop()
        self.after(0, self.update_download1)
    
    def first_sizes(self):
        self.size_comparison.append(os.path.getmtime(self.filepath)) 
        self.size_comparison.append(os.path.getsize(self.filepath))
        if len(self.size_comparison) == 4:
            if self.size_comparison[1] == self.size_comparison[3]: #no download progression
                self.check_path.configure(text="File path has been found.\nNo current download.")
            else:
                self.size_comparison.pop() #reset list
                self.size_comparison.pop()
                self.after(0, self.update_download1)
        

    def checking_path(self):
        if os.path.exists(self.filepath):
            self.check_path.configure(text="File path has been found.\nChecking for download, please wait.")
            self.after(0, self.do_nothing)
        else:
            self.check_path.configure(text="File path does not exist. Please enter a valid path.")
            
        
    def do_nothing(self):
        print("1")
        if self.counter2 == 0:
            self.after(0, self.first_sizes)
        elif self.counter2 == 10:
            self.after(0, self.first_sizes)
            return None
        self.check_path.configure(text="File path has been found.\nChecking for download, please wait.")
        self.counter2 += 1
        self.after(1000, self.do_nothing)

    def update_download1(self):
        print("2")
        if self.counter == 10:
            self.after(0, self.update_sizes)
            return None
        self.check_path.configure(text="File path has been found.\nDownload in progress.")
        self.counter += 1
        self.after(1000, self.update_download2)
    def update_download2(self):
        print("2")
        if self.counter == 10:
            self.after(0, self.update_sizes)
            return None
        self.check_path.configure(text="File path has been found.\nDownload in progress..")
        self.counter += 1
        self.after(1000, self.update_download3)
    def update_download3(self):
        print("2")
        if self.counter == 10:
            
            return None
        self.check_path.configure(text="File path has been found.\nDownload in progress...")
        self.counter += 1
        self.after(1000, self.update_download1)

class sleepContent(mainContent):
    def __init__(self, *args, **kwargs):
        mainContent.__init__(self, *args, **kwargs)
        #self.grid_rowconfigure((0,1,2), weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.sleep_description = customtkinter.CTkLabel(self, text="Automatically shutdown PC after a set amount of time.\nUse this feature if you want to go to sleep with something running in the background.\n\nSet the timer in minutes down below.", font=customtkinter.CTkFont(size=15), wraplength=400)
        self.sleep_description.grid(row=0, column=0, columnspan=4, padx=20, pady=20)

        #self.time_label = customtkinter.CTkLabel(self, text="Set the timer in minutes", font=customtkinter.CTkFont(size=18, weight="bold"))
        #self.time_label.grid(row=1, column=0, padx=20)

        var=tk.IntVar()
        self.time_slider = customtkinter.CTkSlider(self, from_=0, to=100, command=self.sliding)
        self.time_slider.grid(row=1, column=0, columnspan=4)
        self.time_slider.set(50)

        self.time_value = customtkinter.CTkLabel(self, text=self.time_slider.get(), font=customtkinter.CTkFont(size=18))
        self.time_value.grid(row=1, column=0, padx=120)

        self.time_button = customtkinter.CTkButton(self, text="Start sleep timer", command=self.start_sleep)
        self.time_button.grid(row=2, column=0, columnspan=4)

        #Time countdown
    
    def sliding(self, value):
        self.time_value.configure(text=int(value))

    def start_sleep(self):
        time.sleep(60*self.time_slider.get())
        shutdown()



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("900x300")

        self.grid_columnconfigure(1, weight=1) #weight 1 means it fills all the space compared to weight 0, so this column is wider
        
        self.grid_rowconfigure(0, weight=1)

        self.welcome_frame = welcomeContent(self)
        self.download_frame = downloadingContent(self)
        self.sleep_frame = sleepContent(self)

        self.sidebar = customtkinter.CTkFrame(self, width=140)
        self.sidebar.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar.grid_rowconfigure(4, weight=1)
        
        self.functions = customtkinter.CTkLabel(self.sidebar, text="Functions", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.functions.grid(row=0, column=0, padx=20, pady=(20,10))
        
        self.download_button = customtkinter.CTkButton(self.sidebar, text="Downloads", command=self.download_frame.show)
        self.download_button.grid(row=1, column=0, padx=20, pady=10)

        self.sleep_button = customtkinter.CTkButton(self.sidebar, text="Sleep", command=self.sleep_frame.show)
        self.sleep_button.grid(row=2, column=0, padx=20, pady=10)
        

        self.welcome_frame.show()

        self.protocol('WM_DELETE_WINDOW', self.closeWindow)


    def closeWindow(self):
        self.destroy()

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
