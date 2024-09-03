from .main import all, path, read
from . import info
from . import manage

__all__ = ["all", "path", "read", "getdir", "info", "manage"]


class getdir:
    @staticmethod
    def appdata() -> str:
        try:
            return read("APPDATA")
        except Exception as e:
            print(f"Error reading APPDATA: {e}")
            return ""

    @staticmethod
    def temp(user: bool = True) -> str:
        try:
            if user:
                return f"{read('USERPROFILE')}\\AppData\\Local\\Temp"
            else:
                return f"{read('SystemRoot')}\\Temp"
        except Exception as e:
            print(f"Error reading Temp directory: {e}")
            return ""

    @staticmethod
    def windir() -> str:
        try:
            return read("SystemRoot")
        except Exception as e:
            print(f"Error reading SystemRoot: {e}")
            return ""

    @staticmethod
    def onedrive() -> str:
        try:
            return f"{read('USERPROFILE')}\\OneDrive"
        except Exception as e:
            print(f"Error reading OneDrive directory: {e}")
            return ""