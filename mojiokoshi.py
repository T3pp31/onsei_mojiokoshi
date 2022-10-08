import whisper
import os
import sys
import subprocess

def mojiokoshi(file_path):
    model = whisper.load_model('large')
    result = model.transcribe(file_path, verbose = True)
    return result

def find_file():
    

    file_path = '音声ファイル/'

    files = os.listdir(file_path)
    files_file = [f for f in files if os.path.isfile(os.path.join(file_path, f))]
    file_number = 0

    if len(files_file) == 0:
        print('音楽フォルダにファイルを入れてください(.mp4 , .wav)')
        sys.exit()
    if len(files_file) > 0:
        while True:
            print(files_file)
            print('___________________')
            file_number = input('どのファイルを使用するかファイル番号を入れてください(左から1,2...):')
            try:
                file_number = int(file_number)
                break
            except:
                continue
            
    file_name = files_file[file_number-1]
    print(f'{file_name}を選択しました．')
    file_path = file_path + file_name
    print(file_path)
    return file_path

subprocess.run(['pip install git+https://github.com/openai/whisper.git'], shell = True)
subprocess.run(['brew install ffmpeg'], shell = True)


file_path = find_file()
result = mojiokoshi(file_path)
print(result["text"])

f = open('myfile.txt', 'w')
f.write(result['text'])