#!/usr/bin/python3
# Author: Govine I.T Solutions
# Date: 20 August 2022
# Description: This is use to run the batch file.
from createBatchScrip import create_batch_script as create_script
import subprocess
from createBatchScrip import SCRIPT_PATH, SCRIPT_NAME

# Call the create_batch_script function each time the script is run.
create_script()

# Launch the batch script.
# subprocess.call(SCRIPT_PATH + SCRIPT_NAME, shell=True)