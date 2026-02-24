# 1) Librerie
import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
import scipy.signal as signal


# 2) Caricamento del file mp3
file_path = "Squire Tuck - Squire Tuck - Sound of the Savanna.mp3"
y, sr = librosa.load(file_path, sr=None)

# 3) Spettrogramma, evoluzione temporale dello spettro
D = librosa.stft(y)

S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)

plt.figure(figsize=(10, 6))
librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(label='dB')
plt.title("Spettrogramma")
plt.show()

# 4) Frequenza fondamentale f0 e micro-variazioni
f0, voiced_flag, voiced_prob = librosa.pyin(
    y, fmin=librosa.note_to_hz('C2'),
    fmax=librosa.note_to_hz('C7')
)

times = librosa.times_like(f0)

plt.figure(figsize=(10, 4))
plt.plot(times, f0)
plt.title("Frequenza fondamentale (f0)")
plt.xlabel("Tempo (s)")
plt.ylabel("Hz")
plt.show()

plt.plot(times, np.gradient(f0))
plt.title("Micro-variazioni di intonazione")
plt.show()

# 5) Armoniche e inviluppo spettrale
y_harm, y_perc = librosa.effects.hpss(y)

S = np.abs(librosa.stft(y_harm))
mean_spectrum = np.mean(S, axis=1)

plt.plot(librosa.fft_frequencies(sr=sr), mean_spectrum)
plt.title("Inviluppo spettrale medio")
plt.xlabel("Hz")
plt.show()

# 6) Ampiezza (energia\dinamica)
rms = librosa.feature.rms(y=y)[0]
times = librosa.times_like(rms)

plt.plot(times, rms)
plt.title("Energia RMS (dinamica)")
plt.xlabel("Tempo (s)")
plt.show()

# 7) Fase
phase = np.angle(D)

plt.figure(figsize=(10, 6))
librosa.display.specshow(phase, sr=sr, x_axis='time', y_axis='log')
plt.title("Spettro di fase")
plt.colorbar()
plt.show()

# 8) Centroid spettrale (brillantezza)
centroid = librosa.feature.spectral_centroid(y=y, sr=sr)[0]

plt.plot(librosa.times_like(centroid), centroid)
plt.title("Centroid spettrale")
plt.xlabel("Tempo (s)")
plt.ylabel("Hz")
plt.show()

# 9) Componenti inarmoniche
peaks, _ = signal.find_peaks(mean_spectrum)
freqs = librosa.fft_frequencies(sr=sr)

peak_freqs = freqs[peaks]

print("Frequenze di picco:", peak_freqs[:20])

# 10) Rapporto segnale rumore
harm_power = np.mean(y_harm**2)
noise_power = np.mean(y_perc**2)

snr = 10 * np.log10(harm_power / noise_power)
print("SNR stimato (dB):", snr)

# 11) Formanti (approccio base con LPC)
import numpy as np
import librosa
import matplotlib.pyplot as plt

y, sr = librosa.load("Squire Tuck - Squire Tuck - Sound of the Savanna.mp3", sr=None)

# meglio analizzare una finestra breve e quasi stazionaria
frame = y[10000:12000]

# calcolo LPC
A = librosa.lpc(frame, order=16)

# radici del polinomio
roots = np.roots(A)

# prendi solo radici con parte immaginaria positiva
roots = roots[np.imag(roots) > 0]

# conversione in frequenze
formant_freqs = np.angle(roots) * (sr / (2 * np.pi))

print("Formanti stimati (Hz):")
print(np.sort(formant_freqs))