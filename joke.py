import pyjokes
from tkinter import *
from tkinter import ttk
import requests


def tell_a_joke():
    """
    Fetches a neutral programming joke in English using the `pyjokes` library
    and displays it in the output label.
    """
    joke = pyjokes.get_joke("en", "neutral")
    output.config(text=joke)

# Send a joke to the user as mobile notification
def send_joke():
    """
    Fetches a neutral programming joke and sends it as a mobile notification
    using the `ntfy.sh` service.

    It updates the output label to indicate the joke was sent.
    """
    joke = pyjokes.get_joke("en", "neutral")
    requests.post("https://ntfy.sh/zed_jokes", data=f"""Here's a programming joke for you! 😅 {joke}""".encode(encoding='utf-8'))
    output.config(text='Sent!')


# Initialize the main application window
root = Tk()
root.title("Programming Jokes")

# Create a frame for better layout management
frm = ttk.Frame(root, padding=10)
frm.grid()

# Create UI components
instruction = (Label(frm, text="GENERATE A JOKE OR QUIT"))
output = Label(frm, text="")

# Buttons for user interactions
generate = Button(frm, text="Generate", command=tell_a_joke, fg='white', bg='green',  width=10, height=1)
send = Button(frm, text="Send me a joke", command=send_joke, fg='white', bg='blue')
close = Button(frm, text="Quit", command=root.destroy, fg='white', bg='red', width=10, height=1)

# Proper placement of widgets
instruction.grid(column=0, row=0)
output.grid(column=0, row=1)
generate.grid(column=0, row=2, pady=5)
send.grid(column=0, row=3, pady=5)
close.grid(column=0, row=4, pady=5)

# Run the application event loop
root.mainloop()



