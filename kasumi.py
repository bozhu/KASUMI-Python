#!/usr/bin/env python

def _bitlen(x):
    assert x > 0
    return len(bin(x)) - 2


def _rol16(x, s):
    assert _bitlen(x) <= 16
    return ((x << s) & 0xFFFF) | (x >> (16 - s))


def _mod(x):
    return ((x - 1) % 8) + 1


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
        key       = [None] * 9
        key_prime = [None] * 9

        master_key_prime = master_key ^ 0x0123456789ABCDEFFEDCBA9876543210
        for i in range(1, 9):
            key[i]       = (master_key       >> (16 * (8 - i))) & 0xFFFF
            key_prime[i] = (master_key_prime >> (16 * (8 - i))) & 0xFFFF

        for i in range(1, 9):
            self.key_KL1[i] = _rol16(key[_mod(i + 0)], 1)
            self.key_KL2[i] =  key_prime[_mod(i + 2)]
            self.key_KO1[i] = _rol16(key[_mod(i + 1)], 5)
            self.key_KO2[i] = _rol16(key[_mod(i + 5)], 8)
            self.key_KO3[i] = _rol16(key[_mod(i + 6)], 13)
            self.key_KI1[i] =  key_prime[_mod(i + 4)]
            self.key_KI2[i] =  key_prime[_mod(i + 3)]
            self.key_KI3[i] =  key_prime[_mod(i + 7)]


    def fun_FI(self, ):
        pass


    def fun_FO(self):
        pass


    def fun_FL(self, ):
        pass


    def fun_f(self, input, round_i):
        assert _bitlen(input)  <= 32
        assert round_i >= 1 and round_i <= 8
        if round_i % 2 == 1:
            state  = self.fun_FL(input, round_i)
            output = self.fun_FO(state, round_i)
        else:
            state  = self.fun_FO(input, round_i)
            output = self.fun_FL(state, round_i)
        return output


    def enc_1r(self, in_left, in_right, round_i):
        assert _bitlen(in_left)  <= 32
        assert _bitlen(in_right) <= 32
        assert round_i >= 1 and round_i <= 8
        out_right = in_left # note this is different from normal Feistel
        out_left  = self.fun_f(in_left, round_i) ^ in_right
        return out_left, out_right


    def dec_1r(self, in_left, in_right, round_i):
        assert _bitlen(in_left)  <= 32
        assert _bitlen(in_right) <= 32
        assert round_i >= 1 and round_i <= 8
        out_left  = in_right
        out_right = self.fun_f(in_right, round_i) ^ in_left
        return out_left, out_right


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
