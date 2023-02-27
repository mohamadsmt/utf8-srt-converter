import codecs
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class SrtConverter:
    def __init__(self, master):
        # Create the main window
        self.master = master
        self.master.title('SRT File Converter')
        self.master.geometry('500x200')

        # Create a label to display the selected file path
        self.file_label = ttk.Label(self.master, text='No file selected.')
        self.file_label.pack(pady=20)

        # Create a button to select the input file
        self.select_button = ttk.Button(self.master, text='Select File', command=self.select_file)
        self.select_button.pack(pady=10)

        # Create a button to convert the file
        self.convert_button = ttk.Button(self.master, text='Convert File', command=self.convert_file)
        self.convert_button.pack(pady=10)

    # Function to select the input file
    def select_file(self):
        # Open a file dialog to select the input file
        file_path = filedialog.askopenfilename(
            title='Select SRT File',
            filetypes=[('SRT Files', '*.srt')]
        )

        # Update the file label with the selected file path
        self.file_label.config(text=file_path)

    # Function to convert the file
    def convert_file(self):
        # Get the input file path from the file label
        input_path = self.file_label.cget('text')

        # Check if a file is selected
        if not input_path:
            messagebox.showerror('Error', 'No file selected.')
            return

        # Get the file name and extension from the input path
        file_name, file_ext = os.path.splitext(os.path.basename(input_path))

        # Create the output file path with a new name
        output_path = f'{file_name}_new{file_ext}'

        # Open the input file with the correct encoding
        with codecs.open(input_path, 'r', encoding='cp1256') as input_file:
            # Read the contents of the input file
            input_contents = input_file.read()

        # Open the output file with UTF-8 encoding
        with codecs.open(output_path, 'w', encoding='utf-8') as output_file:
            # Write the contents of the input file to the output file
            output_file.write(input_contents)

        # Show a success message
        messagebox.showinfo('Success', 'File converted successfully.')


# Create a Tkinter window
root = tk.Tk()

# Set the window title
root.title('SRT File Converter')

# Set the window size and center it
width = 500
height = 200
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')



# Set the window style
style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', font=('Segoe UI', 12), foreground='#333')
style.configure('TButton', font=('Segoe UI', 12), background='#0072C6', foreground='#FFF', padding=10)
style.map('TButton', background=[('active', '#005EA6')])

# Create the SrtConverter object
srt_converter = SrtConverter(root)

# Start the main loop
root.mainloop()

