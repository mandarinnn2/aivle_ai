import pyaudio
import wave

def record_audio(filename, duration, sample_rate=44100, channels=2, chunk=1024):
    audio_format = pyaudio.paInt16  # 16-bit resolution
    audio = pyaudio.PyAudio()

    # Open stream
    stream = audio.open(format=audio_format, 
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk)
    print("Recording...")

    frames = []

    for _ in range(0, int(sample_rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording finished.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded data as a WAV file
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(audio_format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

if __name__ == "__main__":
    filename = "audio.mp3"
    duration = 5  # seconds
    record_audio(filename, duration)
    print(f"Audio recorded and saved as {filename}")