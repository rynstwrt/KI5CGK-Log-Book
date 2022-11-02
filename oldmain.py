# import PySimpleGUI as sg
#
# sg.theme("DarkBlue")
#
# col_size = (20, None)
# text_padding = (0, 10)
#
# existing_values = []
#
# layout = [
#     [sg.Column(layout=[[
#         sg.Frame("Date", key="date-frame", layout=[[
#             sg.CalendarButton("Select Date",
#                               close_when_date_chosen=True,
#                               auto_size_button=True,
#                               no_titlebar=True,
#                               format="%Y-%m-%d",
#                               enable_events=True,
#                               key="button-calendar",
#                               button_color="#ff885e",
#                               )
#
#         ]]),
#         sg.Frame("Time", layout=[[
#             sg.InputText(key="time", size=col_size)
#         ]]),
#         sg.Frame("Frequency", layout=[[
#             sg.InputText(key="frequency", size=col_size)
#         ]]),
#         sg.Frame("Mode", layout=[[
#             sg.InputText(key="mode", size=col_size)
#         ]]),
#         sg.Frame("Call Sign", layout=[[
#             sg.InputText(key="call-sign", size=col_size)
#         ]]),
#         sg.Frame("Name", layout=[[
#             sg.InputText(key="name", size=col_size)
#         ]]),
#         sg.Frame("Location", layout=[[
#             sg.InputText(key="location", size=col_size)
#         ]])
#     ]], element_justification="c")],
#     [
#         sg.Table(values=existing_values,
#                  headings=["Date", "Time", "Frequency", "Mode", "Call Sign", "Name", "Location"],
#                  auto_size_columns=True,
#                  justification="center",
#                  key="table",
#                  enable_events=True,
#                  expand_x=True,
#                  expand_y=True,
#                  vertical_scroll_only=True,
#                  enable_click_events=True,
#                  selected_row_colors=("white", "black"),
#                  header_relief="test"
#                  ),
#         sg.Column(element_justification="c", layout=[
#             [sg.Button("Add Entry", key="button-add", expand_x=True, button_color="#ff885e")],
#             [sg.Button("Delete Selected Row", key="button-delete", expand_x=True, button_color="#ff885e")]
#         ])
#     ]
# ]
#
# window = sg.Window(title="Log Book", layout=layout, resizable=True, element_justification="c")
# num_entries = 0
#
# while True:
#     event, values = window.read()
#
#     if event == sg.WIN_CLOSED:
#         break
#
#     if event == "button-calendar":
#         window["date-frame"].update(value=values["button-calendar"])
#
#     if event == "button-add":
#         num_entries += 1
#         existing_values = [[
#             values["button-calendar"],
#             values["time"],
#             values["frequency"],
#             values["mode"],
#             values["call-sign"],
#             values["name"],
#             values["location"],
#         ]] + existing_values
#
#         window["table"].update(values=existing_values)
#
#     if event == "button-delete":
#         del_row_index = window["table"].last_clicked_position[0]
#         existing_values.remove(existing_values[del_row_index])
#         window["table"].update(values=existing_values)
#
# window.Close()
