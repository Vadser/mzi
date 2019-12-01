from converter import Converter

class Operation:
  
    @classmethod
    def plus_mod_32(cls, a, b):
        int_a = Converter.to_int(a)
        int_b = Converter.to_int(b)
        int_result = (int_a + int_b) % (2 ** 32)
        result = Converter.int_to_bits(int_result, 32)
        return result

    @classmethod
    def minus_mod_32(cls, a, b):
        int_a = Converter.to_int(a)
        int_b = Converter.to_int(b)
        int_result = (int_a - int_b) % (2 ** 32)
        result = Converter.int_to_bits(int_result, 32)
        return result

    @classmethod
    def bit_xor(cls, arr1, arr2):
        bit_s = []
        for index, item in enumerate(arr1):
            bit_s.append(arr1[index] ^ arr2[index])
        return bit_s
