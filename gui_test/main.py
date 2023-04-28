import tkinter as tk
from tkinter import BooleanVar, IntVar, ttk, filedialog
from PIL import Image, ImageTk


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # root window
        self.title('PROJ')
        self.geometry('850x600')


        self.test_image = ImageTk.PhotoImage(Image.open("test.png").resize((64,64)))

        # Filtry
        settings = ttk.LabelFrame(self, text="Ustawienia")
        settings.pack(fill='y', padx=10, pady=10, side='left')

        # Wybierz plik
        btn = ttk.Button(settings, text='Wybierz plik')
        btn.pack(padx=10, pady=10)

        #  wybrany
        selected_image = ttk.Label(settings, image=self.test_image, padding=5)
        selected_image.pack()

        self.filter_1_value = BooleanVar(value=True)
        filter_1 = ttk.Checkbutton(settings, text="Filtr 1", variable=self.filter_1_value, onvalue=True, offvalue=False)
        filter_1.pack()

        self.filter_2_value = BooleanVar(value=True)
        filter_2 = ttk.Checkbutton(settings, text="Filtr 2", variable=self.filter_2_value, onvalue=True, offvalue=False)
        filter_2.pack()

        self.filter_3_value = BooleanVar(value=True)
        filter_3 = ttk.Checkbutton(settings, text="Filtr 3", variable=self.filter_3_value, onvalue=True, offvalue=False)
        filter_3.pack()

        self.filter_4_value = BooleanVar(value=True)
        filter_4 = ttk.Checkbutton(settings, text="Filtr 4", variable=self.filter_4_value, onvalue=True, offvalue=False)
        filter_4.pack()

        self.filter_5_value = BooleanVar(value=True)
        filter_5 = ttk.Checkbutton(settings, text="Filtr 5", variable=self.filter_5_value, onvalue=True, offvalue=False)
        filter_5.pack()

        # Szukaj
        search = ttk.Button(settings, text='Szukaj')
        search.pack(padx=10, pady=10)

        # Znalezione obrazy
        images = ttk.LabelFrame(self, text="Znalezione obrazy")
        images.pack(fill='both', expand=True, padx=10, pady=10, side="right")

        for i in range(8):
            test = ttk.Label(images, image=self.test_image, padding=10)
            test.pack(anchor='nw', side="left")



if __name__ == "__main__":
    app = App()
    app.mainloop()