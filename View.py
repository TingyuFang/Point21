import tkinter as tk
import time

class App:
    def __init__(self, window):
        frame = tk.Frame(window)
        frame.pack()
        self.hi = tk.Button(frame, text="How r u?", fg="blue", command=self.say_hi())
        self.hi.pack()

    def say_hi(self):
        print("how r u?")


    


def main():
    # window = tk.Tk()
    # app = App(window)
    # window.mainloop()
    print("main function")


if __name__ == "__main__":
    main()