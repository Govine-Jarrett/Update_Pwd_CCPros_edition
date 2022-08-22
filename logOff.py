# Author: Govine G. Jarrett
# Created: 21 August 2022
# Description: Logs off the user
from subprocess import run


def log_off() -> None:
    """
    Logs off the user
    """
    run("shutdown -l",shell=True)


# Used to test the function - PASSED
# log_off()