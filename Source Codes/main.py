import tkinter as tk
from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
from QAsystem import QAsystem

def send_message():
    user_input = input_box.get().strip()
    if not user_input:
        return

    display_message(user_input, "user")
    response = QAsystem(user_input)
    display_message(response, "bot")
    input_box.delete(0, tk.END)

def display_message(message, sender):
    chat_log.configure(state='normal')

    if sender == "user":
        tag = "user_tag"
        color = "black"
        justify = "left"
        lmargin1 = 30  
        rmargin = 30 
        bg=None
        font=("Helvetica")
        
    else:
        tag = "bot_tag"
        color = "green"
        justify = "left"
        lmargin1 = 30
        rmargin = 50 
        bg = "LightCyan2"
        font=("Helvetica", 12, "bold")
        
        icon = Image.open("Source Codes/bot.png")
        icon = icon.resize((40, 40))
        icon = ImageTk.PhotoImage(icon)
        chat_log.window_create(tk.END, window=tk.Label(chat_log, image=icon, bg=bg))
        chat_log.image = icon 

    chat_log.tag_configure(tag, foreground=color, background=bg, justify=justify, lmargin1=lmargin1, rmargin=rmargin, font=font)

    formatted_message = f"{message}\n\n"
    chat_log.insert(tk.END, formatted_message, tag)

    chat_log.configure(state='disabled')
    chat_log.see(tk.END)


# button hover
def on_button_enter(event):
    send_button.config(bg="#C38154", fg="white")

def on_button_leave(event):
    send_button.config(bg="#D6CDA4", fg="black")

window = tk.Tk()
window.title("Chatbot")
window.geometry("500x500")

# Create a Canvas widget and set it as the window background
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

background_image = Image.open("Source Codes/food bg.png")
background_image = background_image.resize((500, 500))
background_photo = ImageTk.PhotoImage(background_image)
canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)

label = tk.Label(canvas, text="MAKANAN MALAYSIA", bg='#1C6758', fg='white', font=("Helvetica", 20, "bold"))
label.pack(pady=10)

chat_log = tk.Text(canvas, height=20, width=80)
chat_log.configure(state='disabled')
chat_log.pack(padx=10, pady=10)

input_box = tk.Entry(canvas, width=40)
input_box.pack(padx=10, pady=10)

send_button = tk.Button(canvas, text="SEND", command=send_message, width=8, height=2, font=font.Font(size=10, weight="bold"))
send_button.config(bg="#D6CDA4", fg="black")
send_button.pack(pady=10)

send_button.bind("<Enter>", on_button_enter)
send_button.bind("<Leave>", on_button_leave)

window.mainloop()
