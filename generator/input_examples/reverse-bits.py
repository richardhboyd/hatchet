bit_reverse_table = [0] * 256 

def reverse_bits(n):
    result = (
        bit_reverse_table[n & 0xff] |
        bit_reverse_table[(n >> 8) & 0xff] << 8 |
        bit_reverse_table[(n >> 16) & 0xff] << 16 |
        bit_reverse_table[(n >> 24) & 0xff] << 24
    )
    return result

# Populate the table
for i in range(256):
    bit_reverse_table[i] = int("{0:08b}".format(i)[::-1], 2)
