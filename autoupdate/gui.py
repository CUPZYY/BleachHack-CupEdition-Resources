from tkinter import *
import tkinter.ttk as ttk

class guiClass():

    def gui(self):
        self.root = Tk()

        # Get the Tk instance

        # Set the layout dimension
        self.root.geometry("500x300")

        # Title the window
        self.root.title("BH-CupEdition Update")

        label = Label(text="Updating BleachHack CupEdition", font=("Consolas", 20))

        # Prepare the type of Progress bar needed.
        # Look out for determinate mode and pick the suitable one
        # Other formats of display can be suitably explored
        processing_bar = ttk.Progressbar(self.root, orient='horizontal', mode='indeterminate', length=380, maximum=40)

        self.successLabel = Label(self.root, text="", font=("Consolas", 20))

        self.successLabel.place(relx=0.5, rely=0.4, anchor=CENTER)
        label.place(relx=0.5, rely=0.3, anchor=CENTER)
        processing_bar.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Start the bar.
        # use processing_bar.stop() to stop it
        processing_bar.start(30)

        self.root.mainloop()



    def done(self):
        self.successLabel.config(text="Update was successful", width=500, height=300)

    def doneF(self):
        self.successLabel.config(text="Update was unsuccessful", width=500, height=300)

    def minecraft(self):
        self.successLabel.config(text="Please close minecraft", width=500, height=300)

    def isOpen(self):
        try:
            self.root.winfo_exists()
        except Exception:
            return False
        return True
