import PySimpleGUI as sg


def display_download(display_word):
    layout = [
        [sg.Text("↓は文字起こし結果")],
        [sg.Text(display_word)],
        [sg.Button("終了")],
    ]

    # ウィンドウの作成
    window = sg.Window("文字起こし結果", layout)

    # イベントループを使用してウィンドウを表示
    while True:
        event, value = window.read()
        if event == sg.WINDOW_CLOSED or event == "終了":
            break

    # ウィンドウを閉じる
    window.close()
