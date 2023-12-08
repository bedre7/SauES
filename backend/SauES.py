from config import Config
from key_scheduler import KeyScheduler
from math import ceil
import base64

class SauES:
    def __init__(self, key: str) -> None:
        self.KEY_LENGTH = Config.KEY_LENGTH
        self.IV_LENGTH = Config.IV_LENGTH
        self.BITS_PER_BYTE = Config.BITS_PER_BYTE
        self.ROUNDS = Config.ROUNDS
        self.SUBSTITUTION_TABLES = Config.SUBSTITUTION_TABLES
        self.INVERSE_SUBSTITUTION_TABLES = Config.INVERSE_SUBSTITUTION_TABLES
        self.block_size = self.IV_LENGTH // self.BITS_PER_BYTE
        self.round_keys = KeyScheduler.get_round_keys(key)
    
    def apply_XOR(self, char1: str, char2: str)-> str:
        return str(int(char1) ^ int(char2))

    def apply_substitution(self, block: str, substitution_table: list) -> str:
        return [block[substitution_table[i]] for i in range(len(block))]
    
    def encrypt(self, plain_text: str) -> str:
        binary_plain_text = self.convert_to_binary_string(plain_text)
        
        binary_cypher_text = []

        for i in range(0, len(binary_plain_text), self.IV_LENGTH):
            block = binary_plain_text[i: i + self.IV_LENGTH]
            encrypted_block = self.encrypt_block(block)

            binary_cypher_text.append(encrypted_block) 
        
        # convert to base64 string -> to avoid any encoding issues with ASCII
        cypher_text = self.encode_to_base64(''.join(binary_cypher_text))

        return cypher_text
    
    def encrypt_block(self, block: str) -> str:
        encrypted_block = [bit for bit in block]

        for round in range(self.ROUNDS):
            round_key = self.round_keys[round]
            
            # apply substitution table -> S-Box
            encrypted_block = self.apply_substitution(encrypted_block, self.SUBSTITUTION_TABLES[round])

            for bit in range(self.IV_LENGTH):
                encrypted_block[bit] = self.apply_XOR(encrypted_block[bit], round_key[bit])


        return ''.join(encrypted_block)
    
    def decrypt(self, cypher_text: str) -> str:
        binary_cypher_text = self.decode_from_base64(cypher_text)
        binary_plain_text = []

        for i in range(0, len(binary_cypher_text), self.IV_LENGTH):
            block = binary_cypher_text[i: i + self.IV_LENGTH]
            decrypted_block = self.decrypt_block(block)

            binary_plain_text.append(decrypted_block)

        # convert to plain text from binary format
        plain_text = self.transform_to_string(''.join(binary_plain_text))

        return plain_text

    def decrypt_block(self, block: str) -> str:
        decrypted_block = [bit for bit in block]

        reversed_round_keys = list(reversed(self.round_keys))

        for round in range(self.ROUNDS):
            round_key = reversed_round_keys[round]

            for bit in range(self.IV_LENGTH):
                decrypted_block[bit] = self.apply_XOR(decrypted_block[bit], round_key[bit])
            
            """ 
            we need to apply the inverse substitution table in reverse order
            and most importantly, only after applying the XOR operation in contrast to the encryption process
            """             
            decrypted_block = self.apply_substitution(decrypted_block, self.INVERSE_SUBSTITUTION_TABLES[round])


        return ''.join(decrypted_block)
    
    def convert_to_binary_string(self, plain_text: str) -> str:
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