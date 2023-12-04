# make this enum instead
from enum import Enum

class Config(Enum):
    KEY_LENGTH = 32
    IV_LENGTH = 32
    ROUNDS = 1
    BITS_PER_BYTE = 8