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
        try:
            no_file = "root.gits file not found"
            with open(PWD_PATH + "error.txt", "w") as f:
                f.write(no_file)
        except Exception:
            pass


