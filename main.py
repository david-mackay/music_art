import numpy as np
import librosa

def convert_audio_to_spectrogram(file_path):
    audio, sample_rate = librosa.load(file_path, sr=None, mono=False)
    audio = np.asfortranarray(audio)

    # Convert audio into spectrogram, one for each channel.
    # The output will be a 3D array with dimensions (channel, frequency, time).
    spectrograms = [librosa.stft(channel) for channel in audio]

    return spectrograms

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <audio_file>")
        return
    print("random edit to test review")
    audio_file = sys.argv[1]
    spectrograms = convert_audio_to_spectrogram(audio_file)

    # Here, each "spectrogram" is a 2D array representing frequency and time.
    # The overall structure is a 3D array for multi-channel audio.
    for i, spectrogram in enumerate(spectrograms):
        print(f"Spectrogram for channel {i + 1}:")
        print(spectrogram)

if __name__ == "__main__":
    main()

