import os
import time
import customtkinter


customtkinter.set_appearance_mode("System")

def button_pressed():
    print("shit")

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

def check_download():
    filepath = input("Enter file path: ") #try catch
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


def main():
    """Create an instance of the class."""
    print("Welcome, " + os.getlogin())
    root_tk.mainloop()
    #check_download()
    


if __name__ == "__main__":
    main()
