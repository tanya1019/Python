import tkinter as tk
from compressmodule import compress,decompress

def compression(i,o):
    compress(i,o)
    
def decompression(i,o):
    decompress(i,o)


window = tk.Tk()

window.title("Compression Window")
window.geometry('600x400')

input_entry = tk.Entry(window)
output_entry = tk.Entry(window)

input_label = tk.Label(window,text =  "Add Compression File")
output_label = tk.Label(window,text = "See Compression File")

button1 = tk.Button(window, text = "Compress", command = lambda : compression(input_entry.get(), output_entry.get()))

input_entry.grid(row = 0, column = 1)
input_label.grid(row = 0, column = 0)
output_entry.grid(row = 1, column = 1)
output_label.grid(row = 1, column = 0)
button1.grid(row = 2, column = 1)

# for decompression

input_entry1 = tk.Entry(window)
output_entry1 = tk.Entry(window)

input_label1 = tk.Label(window,text =  "Add Decompression File")
output_label1 = tk.Label(window,text = "See Decompression File")

button2 = tk.Button(window, text = "Decompress", command = lambda : decompression(input_entry1.get(), output_entry1.get()))

input_entry1.grid(row = 6, column = 1)
input_label1.grid(row = 6, column = 0)
output_entry1.grid(row = 7, column = 1)
output_label1.grid(row = 7, column = 0)
button2.grid(row = 9, column = 1)


window.mainloop()