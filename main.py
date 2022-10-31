import PySimpleGUI as sg


sg.theme("DarkBlue")


col_size = (20, 1)


date_col = [
    [sg.Text("Date")],
    [sg.InputText(size=col_size)]
]

frequency_col = [
    [sg.Text("Frequency")],
    [sg.InputText(size=col_size)]
]

mode_col = [
    [sg.Text("Mode")],
    [sg.InputText(size=col_size)]
]

call_sign_col = [
    [sg.Text("Call Sign")],
    [sg.InputText(size=col_size)]
]

name_col = [
    [sg.Text("Name")],
    [sg.InputText(size=col_size)]
]

location_col = [
    [sg.Text("Location")],
    [sg.InputText(size=col_size)]
]


existing_row = [[
    sg.Text("Date", size=col_size, background_color="orange"),
    sg.Text("Frequency", size=col_size),
    sg.Text("Mode", size=col_size),
    sg.Text("Call Sign", size=col_size),
    sg.Text("Name", size=col_size),
    sg.Text("Location", size=col_size),
]]


layout = [
    [
        sg.Column(date_col),
        sg.Column(frequency_col),
        sg.Column(mode_col),
        sg.Column(call_sign_col),
        sg.Column(name_col),
        sg.Column(location_col)
    ],
    [
        [
            sg.Button("Add Entry")
        ]
    ],
    [
        existing_row
    ]
]


window = sg.Window(title="Log Book", layout=layout, resizable=True, element_justification="c")


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "Add Entry":
        break