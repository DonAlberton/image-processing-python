import os
import tkinter as tk
from tkinter import BooleanVar, ttk, filedialog
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk
from typing import List, Dict

from filters_implementation import classify_given_image


def get_images(filters: Dict[str, bool], image: str) -> tuple:

    images = []
    classification = classify_given_image(image)
    print(classification)

    for filename in os.listdir("baza"):
        file = os.path.join("baza", filename)
        if os.path.isfile(file):

            values = filename.split('-')[0].strip()
            if len(values) < 5: continue
            winter = (classification["isWinter"] == (values[0]=='1')) if filters["isWinter"] else True
            beach = (classification["isBeach"] == (values[1]=='1')) if filters["isBeach"] else True
            indoor = (classification["isIndoor"] == (values[2]=='1')) if filters["isIndoor"] else True
            faces = (classification["hasFaced"] == (values[3]=='1')) if filters["hasFaced"] else True
            glasses = (classification["glasses"] == (values[4]=='1')) if filters["glasses"] else True

            if winter and beach and indoor and faces and glasses:
                images.append(file)

    return (images, classification)


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
        self.selected_file = "gui/blank.png"
        self.selected_image = ImageTk.PhotoImage(Image.open(self.selected_file).resize((64,64)))

        self.selected_image_preview = tk.Button(settings, image=self.selected_image, height=64, width=64, command=lambda file=self.selected_file: self.image_preview(file))
        self.selected_image_preview.pack()

        info_label = ttk.Label(settings, text="Uwzględnione filtry:")
        info_label.pack()

        self.filter_1_value = BooleanVar(value=False)
        filter_1 = ttk.Checkbutton(settings, text="Zima/Inne", variable=self.filter_1_value, onvalue=True, offvalue=False)
        filter_1.pack()

        self.filter_2_value = BooleanVar(value=False)
        filter_2 = ttk.Checkbutton(settings, text="Plaża/Nie", variable=self.filter_2_value, onvalue=True, offvalue=False)
        filter_2.pack()

        self.filter_3_value = BooleanVar(value=False)
        filter_3 = ttk.Checkbutton(settings, text="Wewnątrz/Zewnątrz", variable=self.filter_3_value, onvalue=True, offvalue=False)
        filter_3.pack()

        self.filter_4_value = BooleanVar(value=False)
        filter_4 = ttk.Checkbutton(settings, text="Twarze/Brak", variable=self.filter_4_value, onvalue=True, offvalue=False)
        filter_4.pack()

        self.filter_5_value = BooleanVar(value=False)
        filter_5 = ttk.Checkbutton(settings, text="Okulary/Brak", variable=self.filter_5_value, onvalue=True, offvalue=False)
        filter_5.pack()

        # Szukaj
        search = ttk.Button(settings, text='Szukaj', command=self.search)
        search.pack(padx=10, pady=10)

        # Wyczyść
        clear = ttk.Button(settings, text='Wyczyść', command=self.clear_images)
        clear.pack(padx=10, pady=5)

        # Czekaj
        self.wait_label = tk.Label(settings, text=" ")
        self.wait_label.pack()

        # Cechy
        self.classification_label = tk.Label(settings, text=" ")
        self.classification_label.pack()

        # Liczba
        self.count_label = tk.Label(settings, text=" ")
        self.count_label.pack()

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
        self.selected_image_preview.configure(command=lambda file=self.selected_file: self.image_preview(file))

    def search(self):
        self.wait_label.configure(text="Prosimy czekać...")
        self.update_idletasks()

        filters = {
            'isWinter': self.filter_1_value.get(), 
            'isBeach': self.filter_2_value.get(), 
            'isIndoor': self.filter_3_value.get(), 
            'hasFaced': self.filter_4_value.get(),
            'glasses': self.filter_5_value.get(),
        }

        (files, classification) = get_images(filters, self.selected_file)
        self.images = []
        for file in files:
            img = Image.open(file)
            img.thumbnail((128,128))
            self.images.append(ImageTk.PhotoImage(img))

        self.clear_images()
        for i in range(len(self.images)):
            img_button = tk.Button(self.found_images, image=self.images[i], height=128, width=128, command=lambda file=files[i]: self.image_preview(file))
            img_button.grid(row=i//5, column=i%5)
        
        self.wait_label.configure(text=" ")

        classification_text = "Znalezione cechy:"
        if classification["isWinter"]: classification_text += "\nZima"
        if classification["isBeach"]: classification_text += "\nPlaża"
        if classification["isIndoor"]: classification_text += "\nWewnątrz"
        if classification["hasFaced"]: classification_text += "\nTwarze"
        if classification["glasses"]: classification_text += "\nOkulary"
        self.classification_label.configure(text=classification_text)

        self.count_label.configure(text=f"Liczba obrazów: {str(len(self.images))}")


    def clear_images(self):
        self.classification_label.configure(text=" ")
        self.count_label.configure(text=" ")
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