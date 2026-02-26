#!/usr/bin/env python3
"""
Version checker for PID-Analyzer dependencies
"""
import sys

def check_versions():
    """Check versions of all required packages"""
    print(f"Python version: {sys.version}")
    print("\nPackage versions:")
    
    try:
        import numpy as np
        print(f"NumPy: {np.__version__}")
    except ImportError:
        print("NumPy: ❌ Not installed")
    
    try:
        import scipy
        print(f"SciPy: {scipy.__version__}")
    except ImportError:
        print("SciPy: ❌ Not installed")
    
    try:
        import pandas as pd
        print(f"Pandas: {pd.__version__}")
    except ImportError:
        print("Pandas: ❌ Not installed")
    
    try:
        import matplotlib
        print(f"Matplotlib: {matplotlib.__version__}")
    except ImportError:
        print("Matplotlib: ❌ Not installed")
    
    try:
        import six
        print(f"Six: {six.__version__}")
    except ImportError:
        print("Six: ❌ Not installed")
    
    # Check if all imports work together
    try:
        from scipy.ndimage import gaussian_filter1d
        import matplotlib.pyplot as plt
        print("\n✅ All imports successful - PID-Analyzer should work!")
    except ImportError as e:
        print(f"\n❌ Import error: {e}")

if __name__ == "__main__":
    check_versions()