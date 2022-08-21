# Author: Govine I.T Solutions
# Date: 20 August 2022
# Description: This is used to create a batch script called changePwd.bat.
import os
from readRootGits import get_stored_pwd as pwd
SCRIPT_PATH = "update_admin_password\\res\\script"
SCRIPT_NAME = "changePwd.bat"



# Get the current username and stored password
username = os.getlogin()
new_pwd = pwd()


def create_batch_script() -> None:
    """
    This function is used to create a batch script called changePwd.bat.
    """
    
    batch_script_data = f"@echo off\nREM This script is used to change the admin password of the system.\nnet user {username} {new_pwd}"
    try:
        with open(SCRIPT_PATH+SCRIPT_NAME, "w") as f:
            f.write(batch_script_data)
    except Exception :
        pass
    # TODO: Log the error.