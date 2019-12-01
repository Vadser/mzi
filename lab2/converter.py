class Converter:
  
    @classmethod
    def to_bin(cls, data):
        array = list()
        for char in data:
            binval = cls.binvalue(char, 8)  # Get the char value on one byte
            array.extend([int(x) for x in list(binval)])
        return array

    @classmethod
    def binvalue(cls, val, bitsize):  # Return the binary value as a string of the given size
        binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
        while len(binval) < bitsize:
            binval = "0" + binval
        return binval

    @classmethod
    def to_string(cls, data):
        chars = []
        for i in range(len(data) // 8):
            byte = data[i * 8:(i + 1) * 8]
            byte_str = ''.join(map(str, byte))
            chars.append(chr(int(byte_str, 2)))
        return ''.join(chars)

    @classmethod
    def to_int(cls, value):
        return int(''.join(map(str, value)), 2)

    @classmethod
    def int_to_bits(cls, n, bits_count):
        bits = []
        for digit in bin(n)[2:]:
            bits.append(int(digit))
        while len(bits) < bits_count:
            bits.insert(0, 0)
        return bits
