import whisper


def mojiokoshi(file_path):
    model = whisper.load_model("large")
    result = model.transcribe(file_path, verbose=True)
    return result
