import whisper
from whisper.utils import get_writer

model = whisper.load_model('large')


def get_transcribe(audio: str, language: str = 'ko'):
    return model.transcribe(audio=audio, language=language, verbose=True)


def save_file(results, format='txt', output_dir='.'):
    writer = get_writer(format, output_dir)
    writer(results, 'text_format')


if __name__ == "__main__":
    result = get_transcribe(audio='audio.mp3')
    print('-'*50)
    print(result.get('text', ''))
    save_file(result, output_dir='.')
