# Changelog

## [Unreleased] - 2026-02-26

### Added
- Python 3.8+ compatibility (tested up to Python 3.14)
- Virtual environment setup instructions
- Modern package version requirements
- Git support files (.gitignore)
- Detailed compatibility documentation

### Changed
- **BREAKING**: Updated minimum Python requirement to 3.8+
- Updated `requirements.txt` with modern package versions
- Fixed deprecated NumPy `normed` parameter → `density`
- Fixed deprecated SciPy import path `scipy.ndimage.filters` → `scipy.ndimage`
- Fixed matplotlib `pcolormesh` dimension compatibility
- Fixed matplotlib deprecated `get_cmap()` function
- Fixed matplotlib deprecated `join()` → `joined()` method
- Updated README.md with comprehensive installation instructions

### Fixed
- Compatibility with modern NumPy versions (2.0+)
- Compatibility with modern SciPy versions (1.10+)
- Compatibility with modern matplotlib versions (3.7+)
- Array dimension mismatches in plotting functions
- Type conversion issues for histogram bins

### Technical Details
The following code changes were made for modern Python compatibility:
- Line 13: `from scipy.ndimage.filters import gaussian_filter1d` → `from scipy.ndimage import gaussian_filter1d`
- Line 57: `normed=True` → `density=True` in np.histogram
- Line 273: `normed=False` → `density=False` in np.histogram2d
- Line 294: `len(freq)/4` → `int(len(freq)/4)` for bins parameter
- Multiple lines: Added `shading='gouraud'` and array slicing `[:-1]` to pcolormesh calls
- Lines 423, 447, 474, 498, 520: `join()` → `joined()` for matplotlib axes
- Lines 623, 635: `plt.cm.get_cmap()` → `plt.get_cmap()`

## [0.52] - Original Release
- Original PID-Analyzer functionality
- Support for Betaflight blackbox log analysis
- PID step response calculation
- Noise analysis capabilities
- Compatible with Python 2.7/3.6 and older package versions