import numpy as np
import mne 
import pandas as pd
from scipy import signal
from scipy.signal import welch, filtfilt, butter, iirnotch
import matplotlib.pyplot as plt

def load_eeg_channels(file_path, channels, duration, fs_original):
    channels = int(channels)
    duration = int(duration)
    raw = mne.io.read_raw_bdf(file_path, preload=True) 
    df = raw.to_data_frame()
    df = df.iloc[:duration*fs_original, 1:channels]
    return df

def resample(eeg_df, fs_original, fs):
    eeg_array = eeg_df.values.T
    num_samples = int(eeg_array.shape[1] * fs / fs_original)
    resampled_eeg = np.zeros((eeg_array.shape[0], num_samples))
    for i in range(eeg_array.shape[0]):
        resampled_eeg[i] = np.interp(np.linspace(0, eeg_array.shape[1], num=num_samples, endpoint=False),
            np.arange(eeg_array.shape[1]),
            eeg_array[i]
        )
    return pd.DataFrame(resampled_eeg.T, columns=eeg_df.columns)

def filter_eeg_channel(eeg_df, high_pass, fs):
    x = eeg_df
    sos_high = signal.butter(4, high_pass, btype="high", fs=fs, output="sos")
    x = signal.sosfiltfilt(sos_high, x)

    b, a = signal.iirnotch(50, Q=30, fs=fs)
    x = signal.filtfilt(b, a, x)
    return pd.DataFrame(x, columns=eeg_df.columns)

def apply_car(eeg_df):
    # at each time point, find avg across 64 chan, 
    # then subtract the avg from each chan
    eeg = eeg_df.copy()
    eeg_cols = eeg.columns[-64:]
    mean_signal = eeg[eeg_cols].mean(axis=1)
    for col in eeg_cols:
        eeg[col] = eeg[col] - mean_signal
    return pd.DataFrame(eeg, columns=eeg_df.columns)

