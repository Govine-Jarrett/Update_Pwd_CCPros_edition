# Author: Govine G. Jarrett
# Created: 21 August 2022
# Description: Logs off the user
from subprocess import call


def log_off() -> None:
    """
    Logs off the user
    """
    call(["shutdown", "-l"])


# Used to test the function - PASSED
# log_off()