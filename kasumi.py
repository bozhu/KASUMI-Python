#!/usr/bin/env python

def _bitlen(x):
    assert x > 0
    return len(bin(x)) - 2


class Kasumi:
    def __init__(self):
        self.key_KL1 = [None] * 9
        self.key_KL2 = [None] * 9
        self.key_KO1 = [None] * 9
        self.key_KO2 = [None] * 9
        self.key_KO3 = [None] * 9
        self.key_KI1 = [None] * 9
        self.key_KI2 = [None] * 9


    def set_key(self, master_key):
        pass


    def fun_FI():
        pass


    def fun_FO():
        pass


    def fun_FL():
        pass


    def fun_f(input, round_i):
        pass


    def enc_1r(in_left, in_right, round_i):
        pass


    def dec_1r(in_left, in_right, round_i):
        pass


    def enc(self, plaintext):
        assert _bitlen(plaintext) <= 64
        left  = plaintext >> 32
        right = plaintext & 0xFFFFFFFF
        for i in range(1, 9):
            left, right = self.enc_1r(left, right, i)
        return (left << 32) | right

    def dec(self, ciphertext):
        assert _bitlen(ciphertext) <= 64
        left  = ciphertext >> 32
        right = ciphertext & 0xFFFFFFFF
        for i in range(8, 0, -1):
            left, right = self.enc_1r(left, right, i)
        return (left << 32) | right


if __name__ == '__main__':
    print _bitlen(2), _bitlen(4)
