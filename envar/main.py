from os import environ
from subprocess import getstatusoutput, CalledProcessError

__all__ = ["all", "path", "read"]


def getall():
    try:
        envs = environ
        out = []
        for var, val in envs.items():
            out.insert(0, f"{var}: {val}")
        return out
    except Exception as e:
        print(f"Error getting all environment variables: {e}")
        return []


all = getall()


def getpath():
    try:
        path = environ.get("PATH").split(";")
        out = []
        for i in path:
            out.insert(0, i)
        return out
    except Exception as e:
        print(f"Error getting PATH environment variables: {e}")
        return []


path = getpath()


def read(name: str):
    try:
        return environ.get(name, "")
    except Exception as e:
        print(f"Unexpected error: {e}")
        return ""