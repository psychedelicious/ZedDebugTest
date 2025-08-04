import sys
import os
import site

print("=== Python Environment Diagnostics ===")
print(f"Python executable: {sys.executable}")
print(f"Python version: {sys.version}")
print(f"Python prefix: {sys.prefix}")
print(f"Base prefix: {sys.base_prefix}")
print(f"Is virtual env: {sys.prefix != sys.base_prefix}")

print("\n=== Virtual Environment Variables ===")
print(f"VIRTUAL_ENV: {os.environ.get('VIRTUAL_ENV', 'Not set')}")
print(f"VIRTUAL_ENV_PROMPT: {os.environ.get('VIRTUAL_ENV_PROMPT', 'Not set')}")

print("\n=== Python Path ===")
for i, path in enumerate(sys.path):
    print(f"  [{i}] {path}")

print("\n=== Site Packages ===")
print(f"Site packages dirs: {site.getsitepackages()}")
print(f"User site packages: {site.getusersitepackages()}")

import numpy as np


print("\n=== Numpy Info ===")
print(f"Numpy module: {np}")
print(f"Numpy location: {np.__file__}")
print(f"Numpy version: {np.__version__}")
