from config import Config
from key_scheduler import KeyScheduler
from math import ceil
import base64

class SauES:
    def __init__(self, key: str) -> None:
        self.KEY_LENGTH = Config.KEY_LENGTH.value
        self.IV_LENGTH = Config.IV_LENGTH.value
        self.BITS_PER_BYTE = Config.BITS_PER_BYTE.value
        self.ROUNDS = Config.ROUNDS.value
        self.block_size = self.IV_LENGTH // self.BITS_PER_BYTE
        self.round_keys = KeyScheduler.get_round_keys(key)
    
    def apply_XOR(self, char1: str, char2: str)-> str:
        return str(int(char1) ^ int(char2))

    def encrypt(self, plain_text: str) -> str:
        transformed_plain_text = self.transform_plain_text(plain_text)
        
        cypher_text = []

        for i in range(0, len(transformed_plain_text), self.IV_LENGTH):
            block = transformed_plain_text[i: i + self.IV_LENGTH]
            encrypted_block = self.encrypt_block(block)

            cypher_text.append(encrypted_block) 
        
        # convert to string
        cypher_text = ''.join(cypher_text)
        cypher_text = self.encode_to_base64(cypher_text)

        return cypher_text
    
    def encrypt_block(self, block: str) -> str:
        encrypted_block = [bit for bit in block]

        for round in range(self.ROUNDS):
            round_key = self.round_keys[round]
            for bit in range(self.IV_LENGTH):
                encrypted_block[bit] = self.apply_XOR(encrypted_block[bit], round_key[bit])

        return ''.join(encrypted_block)
    
    def decrypt(self, cypher_text: str) -> str:
        transformed_cypher_text = self.decode_from_base64(cypher_text)
        plain_text = []

        for i in range(0, len(transformed_cypher_text), self.IV_LENGTH):
            block = transformed_cypher_text[i: i + self.IV_LENGTH]
            decrypted_block = self.decrypt_block(block)

            plain_text.append(decrypted_block)

        # convert to string
        plain_text = ''.join(plain_text)
        plain_text = self.transform_to_string(plain_text)

        return plain_text

    def decrypt_block(self, block: str) -> str:
        decrypted_block = [bit for bit in block]

        reversed_round_keys = list(reversed(self.round_keys))

        for round in range(self.ROUNDS):
            round_key = reversed_round_keys[round]
            
            for bit in range(self.IV_LENGTH):
                decrypted_block[bit] = self.apply_XOR(decrypted_block[bit], round_key[bit])

        return ''.join(decrypted_block)
    
    def transform_plain_text(self, plain_text: str) -> str:
        # trim leading and trailing whitespace
        plain_text = plain_text.strip()

        # pad with whitespace if plain_text is too short or not a multiple of IV_LENGTH
        if len(plain_text) % self.block_size != 0:
            needed_blocks = ceil(len(plain_text) / (self.IV_LENGTH // self.BITS_PER_BYTE))
            plain_text = plain_text.ljust(needed_blocks * self.block_size)
        
        # convert to binary string
        plain_text = ''.join([bin(ord(char))[2:].zfill(self.BITS_PER_BYTE) for char in plain_text])

        return plain_text

    def transform_to_string(self, binary_string: str) -> str:
        return ''.join([chr(int(binary_string[i: i + self.BITS_PER_BYTE], 2)) for i in range(0, len(binary_string), self.BITS_PER_BYTE)])
    
    # change to base64
    def encode_to_base64(self, text: str, encoding='utf-8') -> str:
        return base64.b64encode(text.encode(encoding)).decode(encoding)

    # change to string
    def decode_from_base64(self, text: str, encoding='utf-8') -> str:
        return base64.b64decode(text.encode(encoding)).decode(encoding)