import PySimpleGUI as sg
sg.theme("darkgreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Imam heri",
                    layout=[[sg.Text("Contoh Button")],
                            [sg.Button("Button Simpan")],
                            [sg.Button("Button Keluar")],
                            ],
                    size= (600,500),
                    font= ("Times",20))
kejadian,nilai = window.read()
print(kejadian,">",nilai)
window.close()