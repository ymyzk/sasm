#!/usr/bin/env python
# -*- coding: utf-8 -*-


import unittest

from sasm.assembler import Assembler
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


class TestLd(unittest.TestCase):
    def test_compile(self):
        inst = Ld(['r3', '-1', 'r4'])
        self.assertEqual(0b0001110011111111, inst.compile(None))


class TestSt(unittest.TestCase):
    def test_compile(self):
        inst = St(['r3', '-3', 'r4'])
        self.assertEqual(0b0101110011111101, inst.compile(None))


class TestLi(unittest.TestCase):
    def test_compile(self):
        inst = Li(['r3', '13'])
        self.assertEqual(0b1000001100001101, inst.compile(None))
        inst = Li(['r3', '-3'])
        self.assertEqual(0b1000001111111101, inst.compile(None))


class TestAddi(unittest.TestCase):
    def test_compile(self):
        inst = Addi(['r3', '13'])
        self.assertEqual(0b1000101100001101, inst.compile(None))
        inst = Addi(['r3', '-3'])
        self.assertEqual(0b1000101111111101, inst.compile(None))


class TestB(unittest.TestCase):
    def test_compile(self):
        label = Label(['name'])
        label.address = 10
        inst = B(['name'])
        assembler = Assembler()
        assembler.labels['name'] = label
        assembler.counter = 7
        self.assertEqual(0b1010000000000010, inst.compile(assembler))


class TestBe(unittest.TestCase):
    def test_compile(self):
        label = Label(['name'])
        label.address = 10
        inst = Be(['name'])
        assembler = Assembler()
        assembler.labels['name'] = label
        assembler.counter = 13
        self.assertEqual(0b1011100011111100, inst.compile(assembler))


class TestBlt(unittest.TestCase):
    def test_compile(self):
        label = Label(['name'])
        label.address = 10
        inst = Blt(['name'])
        assembler = Assembler()
        assembler.labels['name'] = label
        assembler.counter = 13
        self.assertEqual(0b1011100111111100, inst.compile(assembler))


class TestBle(unittest.TestCase):
    def test_compile(self):
        label = Label(['name'])
        label.address = 10
        inst = Ble(['name'])
        assembler = Assembler()
        assembler.labels['name'] = label
        assembler.counter = 13
        self.assertEqual(0b1011101011111100, inst.compile(assembler))


class TestBne(unittest.TestCase):
    def test_compile(self):
        label = Label(['name'])
        label.address = 10
        inst = Bne(['name'])
        assembler = Assembler()
        assembler.labels['name'] = label
        assembler.counter = 13
        self.assertEqual(0b1011101111111100, inst.compile(assembler))
