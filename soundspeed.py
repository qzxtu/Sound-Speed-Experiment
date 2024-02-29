import numpy as np
import matplotlib.pyplot as plt

# Frequencies of the sound emitted by the speaker
frequencies = np.array([1400, 1500, 1600, 1700, 1800])  # in Hz

# Speed of sound in air at room temperature (approximately)
v_s_theoretical = 343  # in m/s

# Wavelengths
wavelengths = np.array([0.24, 0.23, 0.22, 0.21, 0.20])  # in m

# Calculation of the sound speeds
sound_speeds = wavelengths * frequencies

# Calculation of the percentage errors
percentage_errors = abs((sound_speeds - v_s_theoretical) / v_s_theoretical) * 100

# Print the results for each frequency
for i in range(len(frequencies)):
    print(f"For the frequency {frequencies[i]} Hz:")
    print(f"The wavelength is {wavelengths[i]} m")
    print(f"The speed of sound measured in the experiment is {sound_speeds[i]} m/s")
    print(f"The percentage error with respect to the theoretical value is {percentage_errors[i]}%")
    print()

# Create a figure and an axis
fig, ax = plt.subplots()

# Plot the wavelength vs the frequency
ax.plot(frequencies, wavelengths, 'o-')

# Set the titles of the graph and the axes
ax.set_title('Wavelength vs Frequency')
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Wavelength (m)')

# Show the graph
plt.show()