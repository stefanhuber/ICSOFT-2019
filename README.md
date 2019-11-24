# Analysing the performance of mobile cross-platform development approaches using UI interaction scenarios

## Requirements

 - `adb` must be available via command line
 - Currently `androidviewclient` requires python 2, a python 2 version is required (might change after `androidviewclient` update)

## Installation
  
 - Virtual environment: `python -m venv venv --python=PATH_TO_PYTHON_2_EXE`
 - Activate virtual environment: `venv/Scripts/activate`
 - Install pip dependencies: `pip install -r requirements.txt`
 
## Run interactions

 - **Virtual environment must be activated**
 - **Connect a device in developer mode vi USB** (ensure that tha `adb daemon` is running)
 - Execute `python main.py` to start the test procedure
