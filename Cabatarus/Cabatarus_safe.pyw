import tkinter as tk
import random

root = tk.Tk()
root.withdraw()

warning_window = None


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

    root.after(250, create_window)


def show_warning():
    global warning_window
    warning_window = tk.Toplevel(root)
    warning_window.title("Warning")
    warning_window.geometry("1000x150")

    # Center the warning window on the screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    warning_x = (screen_width - 1000) // 2
    warning_y = (screen_height - 150) // 2
    warning_window.geometry("+{}+{}".format(warning_x, warning_y))

    label = tk.Label(warning_window, text='This Application Is Harmless But It May Cause Full RAM Usage! '
                                          'Would You Like To Continue? '
                                          'The Creator Will Not Be Responsible For Any Damages!!!')
    label.pack(pady=20)

    button_yes = tk.Button(warning_window, text="Yes, I Accept The Risk And Continue", command=accept_warning)
    button_yes.pack(pady=10)

    button_no = tk.Button(warning_window, text="No, Close This Window And Nothing Happens", command=close_warning)
    button_no.pack(pady=10)


def accept_warning():
    global warning_window
    warning_window.destroy()
    create_window()

    root.deiconify()
    stop = tk.Button(root, text="STOP VIRUS", command=destroy)
    stop.pack()


def close_warning():
    global warning_window
    warning_window.destroy()
    root.destroy()


def destroy():
    root.destroy()
    quit()


show_warning()

root.mainloop()
