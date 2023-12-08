from config import Config
from typing import List

class KeyScheduler:
    KEY_LENGTH = Config.KEY_LENGTH
    BITS_PER_BYTE = Config.BITS_PER_BYTE
    ROUNDS = Config.ROUNDS
    KEY_PERMUTATION_TABLE = Config.KEY_PERMUTATION_TABLE
    
    @staticmethod
    def transform_key(key: str) -> str:
        # trim leading and trailing whitespace
        key = key.strip()

        if len(key) > KeyScheduler.KEY_LENGTH // KeyScheduler.BITS_PER_BYTE:
            raise ValueError(f'Key must be {KeyScheduler.KEY_LENGTH // KeyScheduler.BITS_PER_BYTE} bytes long')

        # pad with whitespace
        if len(key) < KeyScheduler.KEY_LENGTH // KeyScheduler.BITS_PER_BYTE:
            key = key.ljust(KeyScheduler.KEY_LENGTH // KeyScheduler.BITS_PER_BYTE)
        
        # convert to binary string
        return ''.join([bin(ord(char))[2:].zfill(KeyScheduler.BITS_PER_BYTE) for char in key])

    @staticmethod
    def permute_key(key: str) -> str:
        permuted_key = ''.join([key[index] for index in KeyScheduler.KEY_PERMUTATION_TABLE])
        return permuted_key
    
    @staticmethod
    def get_round_keys(key: str) -> List[str]:
        transformed_key = KeyScheduler.transform_key(key)
        permuted_key = KeyScheduler.permute_key(transformed_key)
        round_keys = []
        
        for round in range(KeyScheduler.ROUNDS):
            round_key = KeyScheduler.left_shift(permuted_key, round)
            round_keys.append(round_key)
        
        return round_keys

    @staticmethod
    def left_shift(key: str, shift: int) -> str:
        shifted_key = bin(int(key, 2) << shift)[2:].zfill(KeyScheduler.KEY_LENGTH)

        if len(shifted_key) > KeyScheduler.KEY_LENGTH:
            shifted_key = shifted_key[-KeyScheduler.KEY_LENGTH:]
        elif len(shifted_key) < KeyScheduler.KEY_LENGTH:
            shifted_key = shifted_key.zfill(KeyScheduler.KEY_LENGTH)
        
        return shifted_key
        