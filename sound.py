#https://qiita.com/oknix/items/6cdbf853de6aeb474657

# librosaをインポート
import librosa
# numpyをインポート（配列を生成するため）
import numpy as np
# matplotlibをインポート（グラフ描画するため）
import matplotlib.pyplot as plt

y, sr = librosa.load("test.wav")

print(len(y))
print(sr)

time = np.arange(0,len(y)) / sr


#start=29000
#end=38000

start= 29000
end  =43000

y=y[start:end]
time=time[start:end]

fig, ax = plt.subplots()
ax.plot(time, y,linewidth=0.2)

ax.set_xlabel("Time(s)")
ax.set_ylabel("Sound Amplitude")
#ax.set_xlim(1.35, 1.75)
plt.show()

dt=sr
N=len(y)
F = np.fft.fft(y) # 変換結果
freq = np.fft.fftfreq(N, d=dt) # 周波数

Amp = np.abs(F/(N/2)) # 振幅

fig, ax = plt.subplots()
ax.plot(freq[1:int(N/8)], Amp[1:int(N/8)])
ax.set_xlabel("Freqency [Hz]")
ax.set_ylabel("Amplitude")
ax.grid()
plt.show()















'''

import matplotlib.pyplot as plt
import matplotlib
import librosa
import numpy as np

def make_waveform_pyplot(filename):
    y, sr = librosa.load(filename)
    totaltime = len(y)/sr
    time_array = np.arange(0, totaltime, 1/sr)
    mpl.rcParams['agg.path.chunksize'] = 100000
    fig, ax = plt.subplots()
    formatter = mpl.ticker.FuncFormatter(lambda s, x: time.strftime('%M:%S', time.gmtime(s)))
    ax.xaxis.set_major_formatter(formatter)
    ax.set_xlim(0, totaltime)
    ax.set_xlabel("Time")
    ax.plot(time_array, y)
    plt.show()

make_waveform_pyplot("test.wav")
'''
