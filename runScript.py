#!/usr/bin/python3
# Author: Govine I.T Solutions
# Date: 20 August 2022
# Description: This is use to run the batch file.
from createBatchScript import create_batch_script as create_script
import subprocess
from createBatchScript import SCRIPT_PATH, SCRIPT_NAME


def run_script() -> None:
    """
    This function is used to run the batch file.
    """
    
    # Call the create_batch_script function each time the script is run.
    create_script()
    
    try:
        subprocess.call(SCRIPT_PATH + SCRIPT_NAME, shell=True)
    except Exception:
        pass

# Use to test the function.- PASSED
# run_script()