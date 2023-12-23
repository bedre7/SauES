class Config:
    KEY_LENGTH = 48
    BLOCK_LNEGTH = 48
    ROUNDS = 6
    BITS_PER_BYTE = 8
    # generate these tables randomly 
    KEY_PERMUTATION_TABLE = [
        32, 12, 34, 47, 23, 20, 36, 43,
        28, 46, 26, 13, 8, 7, 6, 38,
        18, 1, 29, 14, 40, 5, 25, 37,
        41, 44, 33, 22, 11, 27, 31, 15,
        3, 35, 10, 45, 21, 0, 39, 17,
        16, 4, 30, 2, 9, 24, 42, 19
    ]

    SUBSTITUTION_TABLES = [
        [46, 2, 15, 23, 12, 17, 22, 44, 7, 28, 30, 20, 38, 19, 0, 32, 25, 18, 24, 42, 34, 26, 33, 35, 6, 16, 36, 47, 39, 27, 4, 43, 1, 41, 13, 21, 29, 14, 5, 40, 31, 10, 9, 3, 8, 11, 37, 45],
        [27, 3, 33, 37, 9, 2, 25, 15, 12, 38, 28, 34, 1, 36, 41, 18, 44, 26, 23, 32, 30, 47, 19, 8, 20, 42, 45, 7, 11, 6, 13, 39, 4, 17, 10, 14, 21, 40, 5, 22, 16, 31, 43, 0, 35, 29, 46, 24],
        [19, 7, 43, 6, 41, 45, 8, 13, 18, 15, 23, 40, 46, 36, 47, 27, 42, 16, 32, 39, 34, 2, 30, 29, 20, 12, 31, 21, 17, 3, 0, 5, 14, 22, 25, 35, 9, 1, 38, 44, 28, 37, 11, 10, 33, 4, 24, 26],
        [24, 19, 0, 35, 32, 12, 29, 8, 25, 3, 37, 41, 42, 30, 26, 47, 23, 34, 2, 40, 44, 15, 21, 33, 11, 13, 45, 28, 7, 5, 39, 14, 9, 43, 10, 6, 4, 46, 36, 16, 31, 38, 17, 22, 20, 27, 1, 18],
        [0, 7, 1, 9, 35, 30, 39, 29, 46, 21, 16, 6, 18, 38, 28, 34, 11, 47, 27, 25, 14, 15, 32, 37, 23, 31, 3, 17, 33, 20, 4, 24, 36, 10, 43, 41, 26, 2, 45, 22, 19, 5, 40, 12, 44, 42, 13, 8],
        [36, 42, 44, 38, 17, 29, 37, 6, 34, 18, 3, 24, 16, 5, 32, 26, 2, 12, 15, 40, 25, 7, 45, 19, 14, 35, 28, 13, 41, 39, 27, 9, 30, 20, 33, 22, 46, 31, 23, 43, 4, 10, 1, 11, 0, 47, 8, 21],
    ]

    @staticmethod
    def generate_inverse_permutation_tables(data_permutation_tables):
        inverse_permutation_tables = []
        for table in data_permutation_tables:
            inverse_table = [0] * len(table)
            for i in range(len(table)):
                inverse_table[table[i]] = i
            inverse_permutation_tables.append(inverse_table)
        return list(reversed(inverse_permutation_tables))

    INVERSE_SUBSTITUTION_TABLES = generate_inverse_permutation_tables(SUBSTITUTION_TABLES)