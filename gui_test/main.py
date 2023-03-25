import PySimpleGUI as sg

sg.theme("Dark")

# Define the window's contents
# layout = [[sg.Text("What's your name?")],
#           [sg.Input(key='-INPUT-')],
#           [sg.Text(size=(40,1), key='-OUTPUT-')],
#           [sg.Button('Ok'), sg.Button('Quit')]]

column_left = [
    [sg.FileBrowse("Wybierz plik", file_types=[("Obraz", "*.png")], size=(10, 1))],
    [sg.Frame("Twój obraz:", layout=[[]], expand_x=True, expand_y=True)],
    [sg.Frame("Wybierz filtry:", layout=[
        [sg.Checkbox("Filtr 1", default=True)],
        [sg.Checkbox("Filtr 2", default=True)],
        [sg.Checkbox("Filtr 3", default=True)],
        [sg.Checkbox("Filtr 4", default=True)],
        [sg.Checkbox("Filtr 5", default=True)],
    ])],
    [sg.Button("Szukaj", size=(10, 1))],
]

column_right = [
    [sg.Frame("Znalezione obrazy pasujące do wybranych filtrów:", layout=[[]], expand_x=True, expand_y=True)],

    [sg.Button(f'{n+1}', size=(4, 1)) for n in range(4)],
]

layout = [[
    sg.Column(column_left, element_justification="center", expand_x=True, expand_y=True),
    sg.VSeperator(),
    sg.Column(column_right, element_justification="center", expand_x=True, expand_y=True),
]]

# Create the window
window = sg.Window('PROJ', layout, size=(900, 600))

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    #window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()