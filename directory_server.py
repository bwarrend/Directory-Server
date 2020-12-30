import os
from tkinter import filedialog
from tkinter import *
import tkinter as tk
import _thread
import http.server
import socketserver
import requests



root = Tk()
root.directory = os.getcwd()
port = 27015
external_ip = "127.0.0.1"

tk.Label(root, text="Port").grid(row=0)
label_root = tk.Label(root, text=root.directory)
label_root.grid(row=1)




def startServer(port, root):
    os.chdir(root.directory)
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), Handler) as httpd:
        httpd.serve_forever()



def pick_directory():
    global root
    root.directory = filedialog.askdirectory()

    global label_root
    label_root.config(text = root.directory)

    # tk.Label(root, text=root.directory).grid(row=1)


def copy_ip():
    # root.withdraw()
    root.clipboard_clear()
    ipAndPort = external_ip + ":" + str(port)
    root.clipboard_append(ipAndPort)

def start_server():
    global port
    port = int(port_entry.get())
    _thread.start_new_thread( startServer, (port, root, ))
    global external_ip
    external_ip = requests.get('http://ip.42.pl/raw').text
    startServerLabel = external_ip + ':' + str(port)

    serverLabel = tk.Label(root, text="Server hosted on: ").grid(row=5)
    
    copypasta = tk.Entry(root)
    copypasta.grid(row=5, column=1)
    copypasta.insert('end', startServerLabel)
    copypasta.config(state=DISABLED)
    port_entry.config(state=DISABLED)

    button_copy = tk.Button(root,
    text='Copy', command=copy_ip).grid(row=5, column=2, sticky=tk.W, pady=4)
 





port_entry = tk.Entry(root)

port_entry.grid(row=0, column=1)


button_pd = tk.Button(root, 
        text='Choose Directory', command=pick_directory).grid(row=1, column=1, sticky=tk.W, pady=4)

button_ss = tk.Button(root,
    text='Start Server', command=start_server).grid(row=3, column=0, sticky=tk.W, pady=4)

                                                    

root.title("Directory Hosting")
root.geometry("350x150")

icon = PhotoImage(file = "icon.png")
root.iconphoto(False, icon)


root.mainloop()