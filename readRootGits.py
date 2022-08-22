# Author: Govine I.T Solutions
# Date: 20 August 2022
# Description: This script get the stored password from .gits file called root.
from createPwd import PWD_PATH
import os


def get_stored_pwd() -> str:
    """
    This function is used to get the stored password from .gits file called root.
    """
    # Check if the file exists
    if os.path.exists(PWD_PATH + "root.gits"):
        with open(PWD_PATH + "root.gits", "r") as f:
            password = f.read()
        return password
    else:
        # Return default password if root.gits not found
        return "Password123"


# use to test the function.- PASSED
# print(get_stored_pwd())