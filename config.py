# make this enum instead
from enum import Enum

class Config(Enum):
    KEY_LENGTH = 32
    IV_LENGTH = 32
    ROUNDS = 16
    BITS_PER_BYTE = 8
    KEY_PERMUTATION_TABLE = [
        15, 6, 19, 20, 28, 11, 27, 16,
        0, 14, 22, 25, 4, 17, 30, 9,
        1, 7, 23, 13, 31, 26, 2, 8,
        18, 12, 29, 5, 21, 10, 3, 24
    ]