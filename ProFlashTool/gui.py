import tkinter as tk

class AppGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ProFlashTool")
        
        self.label = tk.Label(self.window, text="Welcome to ProFlashTool")
        self.label.pack()

        self.flash_button = tk.Button(self.window, text="Flash Device", command=self.flash_device)
        self.flash_button.pack()

    def run(self):
        self.window.mainloop()

    def flash_device(self):
        print("Flashing device...")
