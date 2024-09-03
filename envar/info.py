from .main import read

__all__ = ["PROCESSOR", "os"]

class PROCESSOR:
    @staticmethod
    def ARCHITECTURE() -> str:
        try:
            return read("PROCESSOR_ARCHITECTURE")
        except Exception as e:
            print(f"Error reading PROCESSOR_ARCHITECTURE: {e}")
            return ""

    @staticmethod
    def IDENTIFIER() -> str:
        try:
            return read("PROCESSOR_IDENTIFIER")
        except Exception as e:
            print(f"Error reading PROCESSOR_IDENTIFIER: {e}")
            return ""

    @staticmethod
    def LEVEL() -> str:
        try:
            return read("PROCESSOR_LEVEL")
        except Exception as e:
            print(f"Error reading PROCESSOR_LEVEL: {e}")
            return ""

    @staticmethod
    def REVISION() -> str:
        try:
            return read("PROCESSOR_REVISION")
        except Exception as e:
            print(f"Error reading PROCESSOR_REVISION: {e}")
            return ""

def os() -> str:
    try:
        return read("OS")
    except Exception as e:
        print(f"Error reading OS: {e}")
        return ""
