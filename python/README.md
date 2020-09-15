# Python specific instructions

See general instructions for the exercises [here](../README.md).

Complete the functions specified by the exercise in a single file (e.g. `ex1_functions.py`), and submit it in [moodle](https://moodle.oulu.fi/course/view.php?id=4366&section=3).

For OpenCV help see the OpenCV-Python [documentation](https://docs.opencv.org/4.4.0/d0/de3/tutorial_py_intro.html).

## Installation

Python 3.5 or newer (preferably 3.8) and pip are required.

### Install python, pip and setuptools

* On Ubuntu/Debian simply `sudo apt install python3-pip python3-setuptools`
* On Windows install the following manually:
    * [`Python 3`](https://www.python.org/downloads/windows/)
    * [`pip`](https://pip.pypa.io/en/stable/installing/) (includes `setuptools`)

### Make a virtual environment

* Navigate to your project folder (.../cvmbi_exercises/python) in terminal/cmd
* Create a [virtual environment (venv)](https://docs.python.org/3/library/venv.html) with
    * `python3 -m venv venv` (Linux/Mac)
    * `python -m venv venv` (Windows)
* Activate your virtual environment with
    * `source venv/bin/activate` (bash/zsh)
    * `source venv/bin/activate` (csh/tcsh)
    * `venv\Scripts\activate.bat` (Windows)
* Install requirements locally (to venv)
    * `pip install -r requirements.txt`

## Use the virtual environment and run exercise scripts

Every time you work on this project, you should
* navigate to the project folder, and
* activate your virtual environment as shown [above](#make-a-virtual-environment).

From your venv you can run the main files to check your progress:
* `python ex1.py`
* `python ex2.py`
* `python ex3.py`

