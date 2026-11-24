# ============================================================
# Yagi SDR Characterization - Spectrum, PSD, and Angular Sweep
# ============================================================
# Purpose:
# Capture complex IQ samples from an ADALM-Pluto SDR and
# analyze them with FFT, Welch PSD, and an interactive angular-sweep workflow.
#
# Outputs:
# 1. Received RF spectrum (FFT magnitude)
# 2. Power Spectral Density (Welch method)
# 3. Uncalibrated band-power estimates and software-test angular plot
# 4. PNG figures saved to results/plots/
#
# Note:
# Measurements use uncalibrated IQ sample values.
# Plotted magnitudes are not absolute RF power in dBm.
# ============================================================


# Windows compatibility workaround for the pylibiio library.
# On this Python installation, find_library("c") returns None,
# preventing the PlutoSDR interface library from importing.

import ctypes.util

# Preserve the original library lookup function.
original_find_library = ctypes.util.find_library

# Redirect requests for the C runtime to Windows' ucrtbase library.
def windows_find_library(name):
    if name == "c":
        return "ucrtbase"
    return original_find_library(name)

# Apply the Windows compatibility lookup override before importing pylibiio.
ctypes.util.find_library = windows_find_library

import adi
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch
from pathlib import Path
# %%

# Create the results folder if it does not already exist.
output_dir = Path("results/plots")
output_dir.mkdir(parents=True, exist_ok=True)

# 1. PlutoSDR initialization and Receiver Configuration

# Connect to the PlutoSDR using its USB Ethernet IP address
sdr = adi.Pluto(uri="ip:192.168.2.1")


print("PlutoSDR connection established!")

# Set the IQ sampling rate to approximately 3 million samples/second
sdr.sample_rate = int(3e6)

# Set the receiver local oscillator (center frequency) to 425 MHz
# This is our initial SDR test frequency, not the Yagi's 440 MHz design frequency
sdr.rx_lo = int(425e6)

# Set the analog receiver bandwidth to 2 MHz
sdr.rx_rf_bandwidth = int(2e6)

# Disable automatic gain control to maintain consistent receiver gain
sdr.gain_control_mode_chan0 = "manual"

# Apply 30 dB of receiver hardware gain
sdr.rx_hardwaregain_chan0 = 30 

# Acquire 16,384 complex IQ samples per receive buffer
sdr.rx_buffer_size = 16384

# %% 
# 2. IQ Sample Acquisition

# Capture one buffer of complex baseband IQ samples
# Each sample contain an in-phase (I) and quadrature (Q) component
samples = sdr.rx()

# %%
# 3. Fast Fourier Transform (FFT)

# Convert the received IQ samples from the time domain
# into a complex frequency-domain representation
fft_data = np.fft.fft(samples)

# Shift the FFT so negative frequencies appear on the left,
# zero frequency is centered, and positive frequencies are on the right
fft_shifted = np.fft.fftshift(fft_data)

# Generate the frequency associated with each FFT bin
# d represents the sampling interval (seconds/sample)
freq = np.fft.fftfreq(len(samples), d=1/sdr.sample_rate)

# Shift the frequency bins to match the shifted FFT data. 
freq_shifted = np.fft.fftshift(freq)

# %%
# 4. FFT Magnitude and Frequency Conversion 

# Calculate FFT magnitude and normalize by a sample count
# This is a simple amplitude scaling, not a calibrated power measurement
fft_magnitude = np.abs(fft_shifted) / len(samples)

# Convert the linear amplitude magnitude to decibels
# A small constant prevents log10(0), which is undefined
fft_db = 20 * np.log10(fft_magnitude + 1e-12)

# Convert baseband frequency offsets into absolute RF frequencies
# Divide by 1e6 to display the result in MHz
rf_freq = (freq_shifted + sdr.rx_lo) / 1e6

# %%
 # 5. Welch Power Spectral Density (PSD) Estimation
 
# Estimate power spectral density by averaging windowed segments.
# Welch uses a Hann window and 50% overlap by default.
psd_freq, psd = welch(
    samples,
    fs=sdr.sample_rate,       # Actual IQ sampling frequency (Hz)
    nperseg=2048,             # 2048 samples per Welch segment
    return_onesided=False    # Keep negative and positive IQ frequencies
)

# Shift the PSD and its frequency axis to center zero frequency
psd_shift = np.fft.fftshift(psd)
psd_freq_shifted = np.fft.fftshift(psd_freq)


# Convert linear PSD into logarithmic units for visualization
# PSD uses 10*log10 because it represents a power-related quantity.
# The result is uncalibrated logarithmic sample-power density,
# not absolute RF power in dBm/Hz.

psd_db = 10 * np.log10(psd_shift + 1e-20)

# Convert shifted PSD baseband frequencies into absolute RF frequencies (MHz)
psd_rf_freq = (psd_freq_shifted + sdr.rx_lo) / 1e6

# %%
# 6. FFT Spectrum Visualization

plt.figure(figsize=(10,5))

plt.plot(rf_freq, fft_db)

plt.xlabel("Frequency (MHz")
plt.ylabel("FFT Magnitude (dB, arbitrary reference)")

plt.title("PlutoSDR Received Spectrum")

# Save the FFT spectrum for documentation.
plt.grid(True)

plt.savefig(output_dir / "received_spectrum.png", dpi=300, bbox_inches="tight")

plt.show()

# %%
# 7. Receiver Configuration and Processing Diagnostics

print("Sampling rate:", sdr.sample_rate / 1e6, "MSPS")
print("Center frequency", sdr.rx_lo / 1e6, "MHz")
print("RF bandwidth:", sdr.rx_rf_bandwidth / 1e6, "MHz")
print("RX gain:", sdr.rx_hardwaregain_chan0, "dB")
print("IQ buffer size:", sdr.rx_buffer_size, "samples")
print("Number of IQ samples:", len(samples))
print("FFT bins:", len(fft_shifted))
print("First Frequency:", freq_shifted[0] / 1e6, "MHz")
print("Center Frequency:", freq_shifted[len(freq_shifted)//2], "Hz")
print("FFT magnitude bins:", len(fft_db))
print("Maximum FFT magnitude:", round(np.max(fft_db), 2), "dB")
print("PSD frequency bins:", len(psd_freq))
print("PSD magnitude bins:", len(psd))
print("PSD center frequency: ", psd_freq_shifted[len(psd_freq_shifted)//2], "Hz")
print("PSD dB bins:", len(psd_db))
print("Maximum PSD value:", round(np.max(psd_db), 2), "dB/Hz")
print("First PSD RF frequency:", psd_rf_freq[0], "MHz")
print("Center PSD RF frequency:", psd_rf_freq[len(psd_rf_freq)//2], "MHz")

# %% 
# 8. Welch PSD Spectrum Visualization

# Create a new figure for the PSD plot
plt.figure(figsize=(10,5))

# Plot the PSD against the absolute RF frequency
plt.plot(psd_rf_freq, psd_db)

# Label the axes 
plt.xlabel("Frequency (MHz)")
plt.ylabel("PSD (dB, arbitrary sample-power/Hz reference)")

# Add the graph title
plt.title("PlutoSDR Welch Power Spectral Density")

plt.grid(True)

print("Axes in current figure:", len(plt.gcf().axes))

# Save the Welch PSD plot to the results directory.
plt.savefig("results/plots/power_spectral_density.png", dpi=300, bbox_inches="tight")

# Verify the saved PSD image exists 
plot_path = output_dir / "power_spectral_density.png"

print("Plot saved:", plot_path.exists())
print("File location:", plot_path.resolve())

plt.show()
                                

# %%
# 9. Received-Power Estimation

# Define a temporary frequency band for testing.
f_min = 424.2  # MHz
f_max = 424.4  # MHz

# Select PSD bins within the specified frequency interval
band_mask = (psd_rf_freq >= f_min) & (psd_rf_freq <= f_max)

# Extract the linear PSD values inside the selected frequency band
band_psd = psd_shift[band_mask]

# Count the number of selected frequency bins
print("Selected PSD bins:", np.sum(band_mask))

# Verify how many PSD values were extracted
print("Selected PSD values:", len(band_psd))

# Calulate the frequency spacing between adjacent PSD bins (Hz)
delta_f = psd_freq_shifted[1] - psd_freq_shifted[0]

# Verify the calculated frequency resolution
print("PSD frequency-bin spacing:", delta_f, "Hz")

# Integrate the linear PSD across the selected frequency band
band_power = np.sum(band_psd) * delta_f

# Display the estimated power in uncalibrated sample-power units
print("Integrated band power:", band_power)

# Convert linear band power to decibels (uncalibrated)
band_power_db = 10 * np.log10(band_power)
print("Integrated band power (dB):", round(band_power_db, 2))

# Estimate the median noise-plus-signal PSD in the selected band
noise_psd = np.median(band_psd)

# Display the estimate in logarithmic units
noise_psd_db = 10 * np.log10(noise_psd)

print("Median PSD (dB/Hz):", round(noise_psd_db, 2))

# Estimate background power across the selected PSD bins
noise_power = noise_psd * len(band_psd) * delta_f

# Convert the estimated background power to decibels
noise_power_db = 10 * np.log10(noise_power)

print("Estimated background power (dB):", round(noise_power_db, 2))

# Subtract the estimated background from total band power
signal_power = band_power - noise_power

# Check whether a positive signal-power estimate reamains
print("Background-corrected power:", signal_power)
print("Positive signal estimate:", signal_power > 0)

# Convert positive background-corrected power to decibels 
if signal_power > 0:
    signal_power_db = 10 * np.log10(signal_power)
    print("Corrected signal estimate (dB):", round(signal_power_db, 2))
else:
    print("No positive signal-power estimate")
    

# %%
# 10. Yagi Antenna Angular Sweep

# Define antenna rotation angles in degrees
angles = np.arange(0, 361, 30)

# Display the measurement angles
print("Antenna angles:", angles)

# Create an empty list to store power measurements
power_measurements = []

# Display the number of planned measurement positions
print("Total measurement positions:", len(angles[:-1]))
print("Power measurements collected:", len(power_measurements))

# Loop through each unique antenna orientation
for angle in angles[:-1]:
    print("Position Yagi at:", angle, "degrees")

    # Wait for the operator to position the antenna
    input("Press Enter when the Yagi is positioned...")

    # Capture a fresh IQ buffer at the current antenna orientation
    angle_samples = sdr.rx()
    print("IQ samples captured:", len(angle_samples))

    # Calculate the PSD from the current angle's IQ samples
    angle_freq, angle_psd = welch(
        angle_samples,
        fs=sdr.sample_rate,
        nperseg=2048,
        return_onesided=False
    )

    # Shift the PSD so that 0 Hz is in the center
    angle_psd_shift = np.fft.fftshift(angle_psd)

    print("Angle:", angle, "| PSD bins:", len(angle_psd_shift))

    # Extract PSD values within the selected frequency band
    angle_band_psd = angle_psd_shift[band_mask]

    # Integrate the PSD to estimate received power
    angle_power = np.sum(angle_band_psd) * delta_f

    # Convert the power estimate into decibels
    angle_power_db = 10 * np.log10(angle_power)

    # Store the power measurement for this antenna orientation
    power_measurements.append(angle_power_db)

    # Debug: Check whether each measurement is being stored
    print("Stored angle:", angle)
    print("Measurements so far:", len(power_measurements))
    print("Received power:", round(angle_power_db, 2), "dB")

# %%
# 11. Verify Angular Measurements

# Verify the number of recorded angular measurements
print("Total angles measured:", len(angles[:-1]))
print("Power measurements stored:", len(power_measurements))

# Display the collected power values
print("Power measurements (dB):", power_measurements)

# %%
# 12. Normalize Angular Power Measurements

# Convert the power measurements into a NumPy array
power_array = np.array(power_measurements)

# Normalize each measurement to the strongest received power
relative_power_db = power_array - np.max(power_array)

# Display the normalized values
print("Relative power measurements (dB):", relative_power_db)

# %%
# 13. Preliminary Angular Sweep Polar Visualization (Software Test)

# Convert antenna angles from degrees to radians
angles_rad = np.deg2rad(angles)

# Repeat the first power measurment to close the polar plot
relative_power_closed = np.append(relative_power_db, relative_power_db[0])

# Verify the arrays have matching lengths
print("Angular positions:", len(angles_rad))
print("Power Values:", len(relative_power_closed))

# Shift the relative power values so all polar radii are positive.
plot_radius = relative_power_closed - np.min(relative_power_closed)

# Check the shifted values.
print("Minimum relative power:", np.min(relative_power_closed), "dB")
print("Plot radius values:", plot_radius)

# Create a polar plot for the angular sweep
fig, ax = plt.subplots(figsize=(8,8), subplot_kw={"projection": "polar"})

# Plot relative power against antenna orientation
ax.plot(angles_rad, plot_radius, marker="o")

# Add a descriptive title
ax.set_title("Yagi Antenna Angular Sweep (Software Test)", pad=20)

# Set the maximum radial value
ax.set_ylim(0, np.max(plot_radius))

# Display radial labels as relative power in dB
radial_ticks = np.linspace(0, np.max(plot_radius), 5)

ax.set_yticks(radial_ticks)

ax.set_yticklabels(
    [f"{value + np.min(relative_power_closed):.2f} dB"
     for value in radial_ticks]
)

# Save the angular sweep plot to the results directory
polar_plot_path = output_dir / "angular_sweep_software_test.png"

plt.savefig(polar_plot_path, dpi=300, bbox_inches="tight")

# Verify that the plot was saved successfully
print("Polar plot saved:", polar_plot_path.exists())
print("File location:", polar_plot_path.resolve())

# Display the plot
plt.show()