import PySimpleGUI as sg


def find_file():
    """ファイルを選択させるウィンドウ
    Returns:
    --------
    file_path: File Path

    """
    layout = [
        [sg.Text("ファイルを選択してください:")],
        [sg.Input(), sg.FileBrowse()],
        [sg.OK(), sg.Cancel()],
    ]

    window = sg.Window("ファイルアップロード", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        elif event == "OK":
            file_path = values[0]
            sg.popup(f"選択されたファイル: {file_path}")
            break
    sg.popup("しばらく時間がかかります．")
    sg.popup("終了したら，終了を確認するウィンドウが表示されるので，それまでお待ちください")
    window.close()

    return file_path


if __name__ == "__main__":
    find_file()
