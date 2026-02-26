
# PID-Analyzer (Python 3.8+ Compatible)

> **🔄 Modernized Version:** This is an updated version of the original PID-Analyzer with full Python 3.8+ compatibility and modern package support.

### PID-Analyzer 0.52 changes:
- Fixed the noise plot ranges for better visual comparability with option for custom or auto range
- slight change to s/n in deconvolution: Gaussian instead of digital s/n

### Python 3.8+ Compatibility Updates:
- ✅ Updated for NumPy 2.0+ compatibility
- ✅ Fixed SciPy import deprecations  
- ✅ Matplotlib 3.7+ compatibility
- ✅ Python 3.14 tested and working
- ✅ Modern dependency versions

# PID-Analyzer

This program reads Betaflight blackbox logs and calculates the PID step response. It is made as a tool for a more systematic approach to PID tuning.

The step response is a characteristic measure for PID performance and often referred to in tuning techniques.
For more details read: https://en.wikipedia.org/wiki/PID_controller#Manual_tuning 
The program is Python based but utilizes Blackbox_decode.exe from blackbox_tools (https://github.com/cleanflight/blackbox-tools) to read logfiles.

As an example: 
This was the BF 3.15 stock tune (including D Setpoint weight) on my 2.5" CS110: 
![stock tune](images/stock_tune.png)

This a nice tune I came up with after some testing: 
![good tune](images/good_tune.png)

You can even use angle mode, the result should be the same!
The program calculates the system response from input (PID loop input = What the quad should do) and output (Gyro = The quad does). 
Mathematically this is called deconvolution, which is the invers to convolution: Input * Response = Output. 
A 0.5s long response is calculated from a 1.5s long windowed region of interest. The window is shifted roughly 0.2s to calculate each next response. 
From a mathematical point of view this is necessary, but makes each momentary response correspond to an interval of roughly +-0.75s.
 
Any external input (by forced movement like wind) will result in an incomplete system and thus in a corrupted response. 
Based on RC-input and quality the momentary response functions are weighted to reduces the impact of corruptions. Due to statistics, more data (longer logs) will further improve reliability of the result. 

If D Setpoint Transition is set in Betaflight, your tune and thus the response will differ for high RC-inputs. 
This fact is respected by calculating separate responses for inputs above and below 500 deg/s. With just moderate input, you will get one result, if you also do flips there will be two.

Keep in mind that if you go crazy on the throttle it will cause more distortion.  If throttle-PID-attenuation (TPA) is set in Betaflight there will be a different response caused by a dynamically lower P. 
This is the reason why the throttle and TPA threshold is additionally plotted.

The whole thing is still under development and results/input of different and more experienced pilots will be appreciated!

## Requirements

**Python Version:** This project has been updated to support Python 3.8+ (tested with Python 3.14).

### Installation

1. **Download blackbox_decode tool:**
   
   Download the appropriate version for your platform from:
   **https://github.com/cleanflight/blackbox-tools/releases**
   
   - **Windows:** Download and extract `Blackbox_decode.exe`
   - **macOS/Linux:** Download and extract `blackbox_decode`
   
   Place the executable in the same directory as `PID-Analyzer.py`

2. **Create and activate a virtual environment:**
   ```bash
   python3 -m venv fpv
   source fpv/bin/activate  # On Windows: fpv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Or install individually:
   ```bash
   pip install numpy scipy pandas matplotlib six
   ```

### Compatibility Updates

This version has been updated for modern Python versions with the following changes:
- Updated NumPy histogram API (normed → density)
- Fixed SciPy import paths (scipy.ndimage.filters → scipy.ndimage)
- Updated matplotlib pcolormesh for new dimension requirements
- Fixed deprecated matplotlib methods
- Compatible with Python 3.8 through 3.14+

## How to use this program:

1. **Setup Python environment** (see Requirements section above)
2. **Record your log.** Logs of 20s seem to give sufficient statistics. If it's slightly windy, longer logs can still give reasonable results. You can record multiple logs in one session: Each entry will yield a separate plot.
3. **Place your logfiles** and ensure `blackbox_decode` (or `blackbox_decode.exe` on Windows) is available. You can specify the path via command-line flags if needed.
4. **Run the analyzer:**
   
   **Interactive mode:**
   ```bash
   python PID-Analyzer.py
   ```
   
   **Command line mode:**
   ```bash
   python PID-Analyzer.py --log your_log.BBL --name "My Analysis"
   ```
   
   **Multiple logs:**
   ```bash
   python PID-Analyzer.py --log log1.BBL --log log2.BBL --name "Comparison"
   ```

5. **View results:** The logs are processed, analyzed, and plots are saved as PNG images in a folder corresponding to your analysis name.

### Example Usage

```bash
# Activate virtual environment
source fpv/bin/activate

# Analyze a single log
python PID-Analyzer.py --log ~/Downloads/LOG00001.BBL --name "Test_Flight"

# Analyze without showing plot window
python PID-Analyzer.py --log ~/Downloads/LOG00001.BBL --name "Batch_Analysis" --show N
```

### Troubleshooting

- **Import errors:** Make sure your virtual environment is activated and all dependencies are installed
- **"Could not find blackbox_decode" error:** 
  - Download from [blackbox-tools releases](https://github.com/cleanflight/blackbox-tools/releases)
  - Windows: Place `Blackbox_decode.exe` in the project folder
  - macOS/Linux: Place `blackbox_decode` in the project folder  
- **Python version issues:** This updated version requires Python 3.8+

The windows executable includes a virtual python environment and only requires you to drag and drop your Betaflight blackbox logfile into the cmd window.


In case of problems (if the cmd closes for example), please report including the log file.

Tested on Win7/10 and MacOS 10.10, with 3.15/3.2/3.3 logs.



Happy tuning,

Flo

