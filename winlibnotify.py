"""
A 'libnotify' library for use on windows and cygwin for use with Alexey
Vaskovsky's 'notify-send' for Windows.

notify-send can be found here: http://vaskovsky.net/notify-send/
"""

import subprocess

__author__ = "Ryan 'Brent' Taylor"
__email__ = "btaylor@fuzzylogicstudios.com"
__license__ = "Creative Commons Attribution 4.0 International License"

info, important, error = "info", "important", "error"

def notify(title, message, icon=info, timeout=10000, blocking=False):
    """
    Shows native notification messages.

    Args:
        title:      The title to be shown for the message.

        message:    The message contents you want shown.
        
        icon:       The icon to be displayed with the message.  Either 
                    winlibnotify.info, winlibnotify.important or winlibnotify.error.
                    winlibnotify.info is used by default.
        
        timeout:    The time in miliseconds you want the message to be displayed.
                    Default is ten seconds.
        
        blocking:   Specifies if you want this function to block or halt the
                    application until it completes.  Default is False.
    """ 

    func = subprocess.call if blocking else subprocess.Popen
    func(("notify-send", "-i", icon, "-t", str(timeout), title, message))
