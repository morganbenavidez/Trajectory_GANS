# Trajectory_GANS

## Overview

This repository contains code for comparing six different Trajectory Generative Adversarial Networks (Trajectory GANs) implemented in Python. The project is designed to run on Manjaro Linux with Python version 3.11.6. It should work on other Linux distributions as long as the Python version matches. You must have Git installed in order to clone this project, and you need to have a Cuda enabled GPU.

## Installation

Follow the steps below to set up the project on your machine:

1. Open the terminal.

2. Navigate to your Desktop directory (The code is written to train these models from Desktop -> This can be altered in the train_all.py file if necessary):
    ```bash
    cd Desktop
    ```

3. Clone the repository:
    ```bash
    git clone https://github.com/morganbenavidez/Trajectory_GANS.git
    ```

4. Change into the project directory:
    ```bash
    cd Trajectory_GANS
    ```

5. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

6. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

7. Install dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```

This process will create a virtual environment and install all required dependencies for the Trajectory_GAN project.

## Usage

Now that the project is set up, you can proceed with using the Trajectory_GAN.

To begin training, run the file: train_all.py. In this file you can set which models, datasets, epochs and batch size you want to use. You can run every model consecutively, or pick and choose which ones you want to run. 

## Note

Make sure that your system matches the specified Python version (3.11.6) for compatibility. The instructions assume that you have Git, Python, and virtualenv installed on your machine. It also assumes that you have a NVIDIA GPU.


