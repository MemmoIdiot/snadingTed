from re import match

from win32gui import (EnumWindows, FindWindow, GetWindowText,
                      SetForegroundWindow)


class WindowFinder:
    """Class to find and make focus on a particular Native OS dialog/Window """

    def __init__(self):
        self.__handle = None

    def find_window(self, class_name, window_name=None):
        """Pass a window class name & window name directly if known to get the window """
        self.__handle = FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        '''Call back func which checks each open window and matches the name of window using reg ex'''
        if match(wildcard, str(GetWindowText(hwnd))) != None:
            self.__handle = hwnd

    def find_window_wildcard(self, wildcard):
        """ This function takes a string as input and calls EnumWindows to enumerate through all open windows """
        self.__handle = None
        EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """Get the focus on the desired open window"""
        SetForegroundWindow(self.__handle)
