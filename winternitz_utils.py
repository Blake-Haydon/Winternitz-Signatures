from hashlib import sha3_256


def hash_chain(n: int, x: bytes) -> bytes:
    """Hashes a value n times using SHA3-256, h(h(h(...h(x)...)))"""
    for _ in range(n):
        x = sha3_256(x).digest()

    return x


def hash_message(message: str) -> bytes:
    """Hashes a message string using SHA3-256"""
    return sha3_256(message.encode()).digest()


def bytes_to_binary(b: bytes) -> list[int]:
    """Converts a byte string (`b`) to a list of bits"""
    output = []
    for i in range(len(b)):
        for j in range(8):
            bit_mask = 0b10000000 >> j
            bit = int(b[i] & bit_mask != 0)  # either 0 or 1
            output.append(bit)

    return output


def binary_to_int(x: list[int]) -> int:
    """Converts a list of bits to an integer"""
    return sum([x[i] * (2 ** (len(x) - i - 1)) for i in range(len(x))])


def split_into_n_chunks(x: bytes, n_bits: int) -> list[int]:
    """Splits a byte string into `n` chunks of equal length (`n_bits` bits each)"""
    assert n_bits > 0, "Cannot split into chunks of size 0 or negative"
    assert 8 * len(x) % n_bits == 0, "Cannot split evenly into chunks of size `n_bits`"

    # Convert to bits and then split into integer chunks
    bits = bytes_to_binary(x)
    chunks = [bits[i : i + n_bits] for i in range(0, len(bits), n_bits)]
    return list(map(binary_to_int, chunks))
