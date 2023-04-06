from src.display_download_def import display_download
from src.find_file_def import find_file
from src.whisper_def import mojiokoshi

file_path = find_file()
result = mojiokoshi(file_path)
display_download(result)
