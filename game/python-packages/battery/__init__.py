"""
This module provides functions to check information for the battery and
the AC Line for supported systems.
"""

# known issues/help needed:
# Running through wine makes it impossible to detect the battery
# The Darwin linux distro conflicts with the OSX battery detection
# The battery doesn't get properly detected on some linux distros
# Testing on linux distros, like seriously, a lot of testing 

import platform

from . import windows, linux, misc

"""
List of functions to check the battery level.
"""
BATTERY_LEVEL_FUNCTIONS = {
    'Windows': windows.get_level,
    'Linux': linux.get_level,
    '*': misc.get_level,
}

"""
List of functions to check if the battery is present.
"""
BATTERY_CHECK_FUNCTIONS = {
    'Windows': windows.is_battery_present,
    'Linux': linux.is_battery_present,
    '*': misc.is_battery_present,
}

"""
List of functions to check if the system is charging.
"""
AC_LINE_CHECK_FUNCTIONS = {
    'Windows': windows.is_charging,
    'Linux': linux.is_charging,
    '*': misc.is_charging,
}

_system = platform.system()


def _run_function_by_system(funcdict):
    """
    Executes a function based on the system running.

    The '*' will be used for others, usually misc module's functions.

    Raises NotImplemetedError if the system is unsupported.

    :param funcdict: Dictionary of functions by system
    """
    if _system in BATTERY_LEVEL_FUNCTIONS:
        func = funcdict[_system]
    elif misc.can_check():
        func = funcdict['*']
    else:
        return None

    return func()


def get_level():
    """
    Return the system battery level, otherwise None if the system
    doesn't have any batteries.
    """
    try:
        return _run_function_by_system(BATTERY_LEVEL_FUNCTIONS)
    except:
        return None


def is_battery_present():
    """
    Check if the system has a battery present.
    """
    try:
        return _run_function_by_system(BATTERY_CHECK_FUNCTIONS)
    except:
        return False


def is_charging():
    """
    Check if the system is charging.
    """
    try:
        return _run_function_by_system(AC_LINE_CHECK_FUNCTIONS)
    except:
        return False


def get_supported_systems():
    """
    Returns a list of supported systems.
    """
    systems = [x for x in BATTERY_LEVEL_FUNCTIONS if x != '*']
    systems += misc.get_supported_systems()

    return systems


def is_supported():
    """
    Check if this system is supported.
    """
    return False
#    return _system in get_supported_systems()
