# Author: Govine I.T Solutions
# Date: 20 August 2022
# Description: This script is used to create and save the new password.

PWD_PATH = "res/data/"


def take_and_save_pwd(password: str) -> None:
    """
    This function is used to save the password in .gits file called root.
    """
    try:
        with open(PWD_PATH + "root.gits", "w") as f:
            f.write(password)
    except Exception as e:
        with open("error.txt", "w") as f:
            f.write(str(e))

# Use to test the function.
# take_and_save_pwd("12345")