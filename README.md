# Sound Speed Experiment

This Python script is used to calculate the speed of sound at room temperature using different frequencies emitted by a speaker. The script also calculates the percentage error of the measured values with respect to the theoretical value.

![image](https://github.com/qzxtu/Sound-Speed-Experiment/assets/69091361/74748872-c5c1-43d3-9827-d04eaf438f84)

## Dependencies

This script requires the following Python libraries:
- numpy
- matplotlib

You can install these dependencies using pip:
```bash
pip install numpy matplotlib
```

## How it works

1. The script first defines the frequencies of the sound emitted by the speaker and the theoretical speed of sound in air at room temperature.
2. It then calculates the speed of sound for each frequency by multiplying the frequency with the corresponding wavelength. This is based on the formula $$v = f \lambda$$ where $$v$$ is the speed of sound, $$f$$ is the frequency, and $$\lambda$$ is the wavelength.
3. The script calculates the percentage error of the measured speed of sound with respect to the theoretical value. This is based on the formula $$\text{Error \%} = \left|\frac{v_{\text{measured}} - v_{\text{theoretical}}}{v_{\text{theoretical}}}\right| \times 100$$.
4. The results for each frequency, including the wavelength, the measured speed of sound, and the percentage error, are printed out.
5. Finally, the script plots a graph of wavelength versus frequency.

## Modifying the Script

If you want to use this script for your own experiment, you may need to modify the following parts of the script:

- `frequencies`: Replace the array with the frequencies of the sound emitted by your speaker.
- `wavelengths`: Replace the array with the wavelengths corresponding to your frequencies.
- `v_s_theoretical`: Replace the value with the theoretical speed of sound in your medium (if not air at room temperature).

After modifying these values, you can run the script to calculate the speed of sound and the percentage error for your own experiment.
