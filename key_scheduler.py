from config import Config

class KeyScheduler:
    KEY_LENGTH = Config.KEY_LENGTH.value
    BITS_PER_BYTE = Config.BITS_PER_BYTE.value
    ROUNDS = Config.ROUNDS.value
    
    @staticmethod
    def transform_key(key: str):
        # trim leading and trailing whitespace
        key = key.strip()

        # pad with whitespace
        if len(key) < KeyScheduler.KEY_LENGTH // KeyScheduler.BITS_PER_BYTE:
            key = key.ljust(KeyScheduler.KEY_LENGTH // KeyScheduler.BITS_PER_BYTE)
        
        # convert to binary string
        return ''.join([bin(ord(char))[2:].zfill(KeyScheduler.BITS_PER_BYTE) for char in key])

    @staticmethod
    def get_round_keys(key: str):
        transformed_key = KeyScheduler.transform_key(key)
        round_keys = []
        
        for round in range(KeyScheduler.ROUNDS):
            round_key = KeyScheduler.left_shift(transformed_key, round)
            round_keys.append(round_key)
        
        return round_keys

    @staticmethod
    def left_shift(key: str, shift: int):
        shifted_key = bin(int(key, 2) << shift)[2:].zfill(KeyScheduler.KEY_LENGTH)

        if len(shifted_key) > KeyScheduler.KEY_LENGTH:
            shifted_key = shifted_key[-KeyScheduler.KEY_LENGTH:]
        elif len(shifted_key) < KeyScheduler.KEY_LENGTH:
            shifted_key = shifted_key.zfill(KeyScheduler.KEY_LENGTH)
        
        return shifted_key
        