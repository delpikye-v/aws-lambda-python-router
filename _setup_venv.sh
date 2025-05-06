#!/bin/bash

# 1. Log environment information
echo "** Environment Information **"
echo "Python version: $(python3.12 --version)"

# 2. Create a virtual environment named "product_venv"
echo "** Creating virtual environment **"
rm -rf venv
python3.12 -m venv venv

# 3. Activate the virtual environment
echo "** Activating virtual environment **"
source venv/bin/activate

# 4. Install required Python dependencies from a requirements.txt file
echo "** Installing dependencies from requirements-dev.txt **"
pip install -r requirements-dev.txt
