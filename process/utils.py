import ctypes
from enum import Enum

from process.interfaces import ComplexProcessHandle, SimpleProcessHandle


class Architecture(Enum):
    x86 = 0
    x64 = 1
    unknown = 2

def ensure_complex(process: SimpleProcessHandle):
    if not isinstance(process, ComplexProcessHandle):
        raise Exception("Process is not complex")

    return process


def get_architecture():
    if ctypes.sizeof(ctypes.c_void_p) == 4:
        return Architecture.x86
    elif ctypes.sizeof(ctypes.c_void_p) == 8:
        return Architecture.x64
    else:
        return Architecture.unknown


def choose(value_x86, value_x64):
    if get_architecture() == Architecture.x86:
        return value_x86
    elif get_architecture() == Architecture.x64:
        return value_x64
    else:
        raise Exception("Unknown architecture")
