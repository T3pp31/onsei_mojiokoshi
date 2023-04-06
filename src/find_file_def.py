import PySimpleGUI as sg


def find_file():
    """ファイルを選択させるウィンドウ
    Returns:
    --------
    file_path: File Path

    """
    layout = [
        [
            sg.Text("音声ファイルを選択してください"),
            sg.InputText(),
            sg.FileBrowse(key="file1"),
        ],
        [sg.Submit(), sg.Cancel()],
    ]
    window = sg.Window("ファイル選択", layout)

    event, values = window.read()
    window.close()
    file_path = values["file1"]
    print(file_path)


if __name__ == "__main__":
    find_file()
