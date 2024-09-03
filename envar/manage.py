import os

__all__ = ["add", "remove"]

def add(name: str, value: str):
    try:
        os.environ[name] = value
    except Exception as e:
        print(f"Unexpected error adding environment variable {name}: {e}")
    return None

def remove(name: str):
    try:
        if name in os.environ:
            del os.environ[name]
        else:
            print(f"Environment variable {name} does not exist.")
    except Exception as e:
        print(f"Unexpected error removing environment variable {name}: {e}")
    return None
