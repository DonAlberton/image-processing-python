import tkinter as tk
from tkinter import BooleanVar, ttk, filedialog
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk


def get_images(filters: tuple[bool,bool,bool,bool,bool], image: str) -> list[str]:
    # PLACEHOLDER
    return ["test.png"] * 27


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # root window
        self.title('PROJ')
        self.geometry('830x600')
        self.resizable(False, False)

        # Filtry
        settings = ttk.LabelFrame(self, text="Ustawienia")
        settings.pack(fill='y', padx=10, pady=10, side='left')

        # Wybierz plik
        btn = ttk.Button(settings, text='Wybierz plik', command=self.select_file)
        btn.pack(padx=10, pady=10)

        #  wybrany
        self.selected_file = "blank.png"
        self.selected_image = ImageTk.PhotoImage(Image.open(self.selected_file).resize((64,64)))

        self.selected_image_preview = ttk.Label(settings, image=self.selected_image, padding=5)
        self.selected_image_preview.pack()

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
        search = ttk.Button(settings, text='Szukaj', command=self.search)
        search.pack(padx=10, pady=10)

        # Wyczyść
        clear = ttk.Button(settings, text='Wyczyść', command=self.clear_images)
        clear.pack(padx=10, pady=5)

        # Znalezione obrazy
        text = ScrolledText(self, state='disable')
        text.pack(fill='both', expand=True, padx=10, pady=10, side="right")
        self.found_images = tk.Frame(text)
        text.window_create('1.0', window=self.found_images)

    def select_file(self):
        self.selected_file = filedialog.askopenfilename()

        img = Image.open(self.selected_file)
        img.thumbnail((64,64))
        self.selected_image = ImageTk.PhotoImage(img)
        self.selected_image_preview.configure(image=self.selected_image)

    def search(self):
        filters = (self.filter_1_value.get(), self.filter_2_value.get(), self.filter_3_value.get(), self.filter_4_value.get(), self.filter_5_value.get())

        files = get_images(filters, self.selected_file)
        self.images = []
        for file in files:
            img = Image.open(file)
            img.thumbnail((128,128))
            self.images.append(ImageTk.PhotoImage(img))

        self.clear_images()
        for i in range(len(self.images)):
            img_button = tk.Button(self.found_images, image=self.images[i], height=128, width=128, command=lambda file=files[i]: self.image_preview(file))
            img_button.grid(row=i//5, column=i%5)

    def clear_images(self):
        for widget in self.found_images.winfo_children():
            widget.destroy()

    def image_preview(self, file):
        preview_window = tk.Toplevel(self)
        preview_window.title("Podgląd obrazu") 
        preview_window.resizable(False, False)
        preview_window.grab_set()

        img = Image.open(file)
        img.thumbnail((800,800))
        self.preview_image = ImageTk.PhotoImage(img)

        ttk.Label(preview_window, image=self.preview_image, padding=5).pack()
        ttk.Label(preview_window, text=file, padding=5).pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()