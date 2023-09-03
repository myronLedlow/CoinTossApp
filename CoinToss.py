from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
from random import randint

class CoinTossApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Coin Toss App")
        self.create_ui()

    def create_ui(self):
        my_style = ttk.Style()
        my_style.configure("TLabel")
        label = tk.Label(self.root, text="Coin Toss App", font=(
            "Arial", 38, "bold"), bg="white", fg="black")
        label.pack(pady=5)
        ttk.Style().configure("TButton", padding=6, relief="raised", background="#000")
        
        create_button = ttk.Button(
            self.root, text="Toss A Coin", command=self.toss)
        create_button.pack(pady=20)

        exit_button = ttk.Button(
            self.root, text="Exit", command=exit)
        exit_button.pack(pady=5)

    def create_scrollable_frame(self, parent):
        canvas = tk.Canvas(parent)
        canvas.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(parent, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas.configure(yscrollcommand=scrollbar.set)

        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor='nw')

        return frame

    def toss(self):
        num = randint(0, 1)
        
        if num == 0:
            img = Image.open("heads.png")
            self.heads_image = ImageTk.PhotoImage(img)
            new_win = tk.Toplevel()
            new_win.title("Heads")
            window_height = 500
            window_width = 340
            screen_width = new_win.winfo_screenwidth()
            screen_height = new_win.winfo_screenheight()
            x_cordinate = int((screen_width/2) - (window_width/2))
            y_cordinate = int((screen_height/2) - (window_height/2))
            new_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

            frame = self.create_scrollable_frame(new_win)
            label_2 = tk.Label(frame, text="You Got Heads", font=("Arial", 18))
            label_2.pack(pady=5)
            label = tk.Label(frame, image=self.heads_image)
            label.pack(pady=5)
            

        else:
            img_2 = Image.open("tails.png")
            self.tails_image = ImageTk.PhotoImage(img_2)
            new_win = tk.Toplevel()
            new_win.title("Tails")
            window_height = 500
            window_width = 340
            screen_width = new_win.winfo_screenwidth()
            screen_height = new_win.winfo_screenheight()
            x_cordinate = int((screen_width/2) - (window_width/2))
            y_cordinate = int((screen_height/2) - (window_height/2))
            new_win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate)) 

            frame = self.create_scrollable_frame(new_win)
            label_2 = tk.Label(frame, text="You Got Tails", font=("Arial", 18))
            label_2.pack(pady=10)
            label = tk.Label(frame, image=self.tails_image)
            label.pack(pady=5)
            

if __name__ == "__main__":
    win = tk.Tk()
    win.config(bg="white")
    win.resizable(False, False)
    frame = tk.Frame(win, width=600, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)
    win.attributes('-fullscreen', True)
    app = CoinTossApp(win)
    win.mainloop()
