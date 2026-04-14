from data_mgmt import *
from preprocessing import *

path = r"C:\Users\kngu0289\OneDrive - The University of Sydney (Staff)\\2. SHARED SHORTCUTS\Yvonne Tran's files - EEG analysis" 
name = "002baseline1.2.bdf"
file_path = f"{path}\\{name}"


fs_original = 2048
fs = 512


eeg = load_eeg_channels(file_path, channels=65, duration=120, fs_original=fs_original)
eeg_resamp = resample(eeg, fs_original, fs)
eeg_fil = filter_eeg_channel(eeg_resamp, high_pass=0.5, fs=fs)
eeg_pp = apply_car(eeg_fil)

fig, axes = plt.subplots(3, 1, figsize=(15, 9))
axes[0].plot(eeg_resamp["B1"][:512*30])
axes[1].plot(eeg_fil["B1"][:512*30])
axes[2].plot(eeg_pp["B1"][:512*30])

plt.show()
