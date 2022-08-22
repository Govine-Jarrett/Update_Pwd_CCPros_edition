#!/usr/bin/python3
# Author: Govine I.T Solutions
# Date: 20 August 2022
# Description: This is use to run the batch file.
import os
from subprocess import call
from readRootGits import get_stored_pwd 
from logOff import log_off


username = os.getlogin()
pwd = get_stored_pwd()

def run_script() -> None:
    """
    This function runs command to change the admin 
    password, then logs off the user.
    """

    try:
        check_in_pwd_changed = call(["net", "user", username, pwd])
        
        # check if the password is changed or not.
        if check_in_pwd_changed == 0:
            # Sign out the user.
            log_off()

    except Exception as e:
        # TODO: Log the error properly.
        with open("run_script_error.txt", "w") as f:
            f.write(str(e))
        

# Use to test the function.- PASSED
# run_script()