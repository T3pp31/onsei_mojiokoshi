import PySimpleGUI as sg
import whisper


def mojiokoshi(file_path):
    model = whisper.load_model("large")
    result = model.transcribe(file_path, verbose=True)

    return result["text"]


layout = [
    [sg.Text("ファイルパス"), sg.Input(), sg.FileBrowse()],
    [sg.Button("実行"), sg.Button("キャンセル")],
    [sg.Output(size=(60, 20))],
]


window = sg.Window("文字起こし", layout)

# イベントループ
while True:
    event, values = window.read()

    if event == "実行":
        file_path = values[0]
        sg.popup("実行中です，時間がかかります")
        result = mojiokoshi(file_path)
        print(result)

    elif event == "キャンセル" or event == sg.WIN_CLOSED:
        break

window.close()
