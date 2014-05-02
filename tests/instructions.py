#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

from sasm.instructions import *


class TestInstruction(unittest.TestCase):
    def test_get_complement(self):
        inst = Instruction()
        self.assertEqual(7, inst._get_complement(7, bits=8))
        self.assertEqual(0b11111111, inst._get_complement(-1, bits=8))

    def test_str_to_int(self):
        inst = Instruction()
        self.assertEqual(0b100, inst._str_to_int('0b100'))
        self.assertEqual(0o100, inst._str_to_int('0o100'))
        self.assertEqual(100, inst._str_to_int('100'))
        self.assertEqual(0x100, inst._str_to_int('0x100'))
        self.assertEqual(253, inst._str_to_int('-3', bits=8))


class TestAdd(unittest.TestCase):
    def test_compile(self):
        inst = Add(['r3', 'r6'])
        self.assertEqual(0b1111001100000000, inst.compile(None))


class TestSub(unittest.TestCase):
    def test_compile(self):
        inst = Sub(['r4', 'r6'])
        self.assertEqual(0b1111010000010000, inst.compile(None))


class TestAnd(unittest.TestCase):
    def test_compile(self):
        inst = And(['r4', 'r7'])
        self.assertEqual(0b1111110000100000, inst.compile(None))


class TestOr(unittest.TestCase):
    def test_compile(self):
        inst = Or(['r2', 'r7'])
        self.assertEqual(0b1111101000110000, inst.compile(None))


class TestXor(unittest.TestCase):
    def test_compile(self):
        inst = Xor(['r2', 'r5'])
        self.assertEqual(0b1110101001000000, inst.compile(None))


class TestCmp(unittest.TestCase):
    def test_compile(self):
        inst = Cmp(['r4', 'r5'])
        self.assertEqual(0b1110110001010000, inst.compile(None))


class TestMov(unittest.TestCase):
    def test_compile(self):
        inst = Mov(['r4', 'r1'])
        self.assertEqual(0b1100110001100000, inst.compile(None))


class TestSll(unittest.TestCase):
    def test_compile(self):
        inst = Sll(['r4', '3'])
        self.assertEqual(0b1100010010000011, inst.compile(None))


class TestSlr(unittest.TestCase):
    def test_compile(self):
        inst = Slr(['r7', '5'])
        self.assertEqual(0b1100011110010101, inst.compile(None))


class TestSrl(unittest.TestCase):
    def test_compile(self):
        inst = Srl(['r5', '6'])
        self.assertEqual(0b1100010110100110, inst.compile(None))


class TestSra(unittest.TestCase):
    def test_compile(self):
        inst = Sra(['r2', '3'])
        self.assertEqual(0b1100001010110011, inst.compile(None))


class TestIn(unittest.TestCase):
    def test_compile(self):
        inst = In(['r6'])
        self.assertEqual(0b1100011011000000, inst.compile(None))


class TestOut(unittest.TestCase):
    def test_compile(self):
        inst = Out(['r6'])
        self.assertEqual(0b1111000011010000, inst.compile(None))


class TestHlt(unittest.TestCase):
    def test_compile(self):
        inst = Hlt([])
        self.assertEqual(0b1100000011110000, inst.compile(None))


class TestLi(unittest.TestCase):
    def test_compile(self):
        inst = Li(['r3', '13'])
        self.assertEqual(0b1000001100001101, inst.compile(None))
        inst = Li(['r3', '-3'])
        self.assertEqual(0b1000001111111101, inst.compile(None))
