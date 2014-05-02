#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


class Instruction(object):
    def __init__(self):
        self._register_lut = {
            'r0': 0,  # General Register 0
            'r1': 1,  # General Register 1
            'r2': 2,  # General Register 2
            'r3': 3,  # General Register 3
            'r4': 4,  # General Register 4
            'r5': 5,  # General Register 5
            'r6': 6,  # General Register 6
            'r7': 7,  # General Register 7
        }

    def _get_register(self, reg):
        if reg in self._register_lut:
            return self._register_lut[reg]
        else:
            raise LookupError('Register is not implemented: %s' % reg)
            return ''

    def _get_complement(self, i, bits=8):
        if i < 0:
            i = abs(i + (1 << bits))
        return i

    def _str_to_int(self, string, bits=8):
        i = 0
        if len(string) < 3:
            i = int(string, 10)
        elif string[0:2] == '0b' or string[0:3] == '-0b':
            i = int(string, 2)
        elif string[0:2] == '0o' or string[0:3] == '-0o':
            i = int(string, 8)
        elif string[0:2] == '0x' or string[0:3] == '-0x':
            i = int(string, 16)
        else:
            i = int(string)

        return self._get_complement(i, bits)


class RInstruction(Instruction):
    def __init__(self):
        Instruction.__init__(self)

        self.instruction = 0xc000

    def compile(self, assembler):
        return self.instruction


class R1Instruction(RInstruction):
    def __init__(self, args):
        RInstruction.__init__(self)

        self.rd = self._get_register(args[0])
        self.rs = self._get_register(args[1])

        self.instruction += (self.rd << 8)
        self.instruction += (self.rs << 11)


class R2Instruction(RInstruction):
    def __init__(self, args):
        RInstruction.__init__(self)

        self.rd = self._get_register(args[0])
        self.d = int(args[1])

        self.instruction += (self.rd << 8)
        self.instruction += self.d


class LSInstruction(Instruction):
    def __init__(self, args):
        Instruction.__init__(self)

        self.ra = self._get_register(args[0])
        self.d = int(args[1])
        self.rb = self._get_register(args[2])

        self.instruction = 0x0000
        self.instruction += self.d
        self.instruction += (self.rb << 8)
        self.instruction += (self.ra << 11)

    def compile(self, assembler):
        return self.instruction


class IBInstruction(Instruction):
    def __init__(self):
        Instruction.__init__(self)
        self.instruction = 0x8000


class BInstruction(Instruction):
    def __init__(self, args):
        Instruction.__init__(self)

        if re.match('[a-zA-Z][a-zA-Z_0-9]*', args[0]) is not None:
            self.d = Label([args[0]])
        else:
            self.d = self._str_to_int(args[0], bits=8)

        self.instruction = 0xb800

    def compile(self, assembler):
        if isinstance(self.d, Label):
            self.d = assembler.labels[self.d.name].address
            self.d -= assembler.counter
            self.d -= 1
            self.d = self._get_complement(self.d, bits=8)
        self.instruction += self.d
        return self.instruction


class Add(R1Instruction):
    def __init__(self, args):
        R1Instruction.__init__(self, args)
        self.instruction += (0b0000 << 4)


class Sub(R1Instruction):
    def __init__(self, args):
        R1Instruction.__init__(self, args)
        self.instruction += (0b0001 << 4)


class And(R1Instruction):
    def __init__(self, args):
        R1Instruction.__init__(self, args)
        self.instruction += (0b0010 << 4)


class Or(R1Instruction):
    def __init__(self, args):
        R1Instruction.__init__(self, args)
        self.instruction += (0b0011 << 4)


class Xor(R1Instruction):
    def __init__(self, args):
        R1Instruction.__init__(self, args)
        self.instruction += (0b0100 << 4)


class Cmp(R1Instruction):
    def __init__(self, args):
        R1Instruction.__init__(self, args)
        self.instruction += (0b0101 << 4)


class Mov(R1Instruction):
    def __init__(self, args):
        R1Instruction.__init__(self, args)
        self.instruction += (0b0110 << 4)


class Sll(R2Instruction):
    def __init__(self, args):
        R2Instruction.__init__(self, args)
        self.instruction += (0b1000 << 4)


class Slr(R2Instruction):
    def __init__(self, args):
        R2Instruction.__init__(self, args)
        self.instruction += (0b1001 << 4)


class Srl(R2Instruction):
    def __init__(self, args):
        R2Instruction.__init__(self, args)
        self.instruction += (0b1010 << 4)


class Sra(R2Instruction):
    def __init__(self, args):
        R2Instruction.__init__(self, args)
        self.instruction += (0b1011 << 4)


class In(RInstruction):
    def __init__(self, args):
        RInstruction.__init__(self)

        self.rd = self._get_register(args[0])
        self.instruction += (self.rd << 8)
        self.instruction += (0b1100 << 4)


class Out(RInstruction):
    def __init__(self, args):
        RInstruction.__init__(self)

        self.rs = self._get_register(args[0])
        self.instruction += (self.rs << 11)
        self.instruction += (0b1101 << 4)


class Hlt(RInstruction):
    def __init__(self, args):
        RInstruction.__init__(self)

        self.instruction += (0b1111 << 4)


class Ld(LSInstruction):
    def __init__(self, args):
        LSInstruction.__init__(self, args)
        self.instruction += (0b00 << 14)


class St(LSInstruction):
    def __init__(self, args):
        LSInstruction.__init__(self, args)
        self.instruction += (0b01 << 14)


class Li(IBInstruction):
    def __init__(self, args):
        IBInstruction.__init__(self)
        self.rb = self._get_register(args[0])
        self.d = self._str_to_int(args[1], bits=8)

        self.instruction += self.d
        self.instruction += (self.rb << 8)
        self.instruction += (0b000 << 11)

    def compile(self, assembler):
        return self.instruction


class B(IBInstruction):
    def __init__(self, args):
        self.instruction = 0x8000

        if re.match('[a-zA-Z][a-zA-Z_0-9]*', args[0]) is not None:
            self.d = Label([args[0]])
        else:
            self.d = self._str_to_int(args[0], bits=8)

        self.instruction += (0b100 << 11)

    def compile(self, assembler):
        if isinstance(self.d, Label):
            self.d = assembler.labels[self.d.name].address
            self.d -= assembler.counter
            self.d -= 1
            self.d = self._get_complement(self.d, bits=8)
        self.instruction += self.d
        return self.instruction


class Be(BInstruction):
    def __init__(self, args):
        BInstruction.__init__(self, args)
        self.instruction += (0b000 << 8)


class Blt(BInstruction):
    def __init__(self, args):
        BInstruction.__init__(self, args)
        self.instruction += (0b001 << 8)


class Ble(BInstruction):
    def __init__(self, args):
        BInstruction.__init__(self, args)
        self.instruction += (0b010 << 8)


class Bne(BInstruction):
    def __init__(self, args):
        BInstruction.__init__(self, args)
        self.instruction += (0b011 << 8)


class Option(object):
    def __init__(self, args):
        self.name = args[0]
        self.value = args[1]


class Label(object):
    def __init__(self, args):
        self.address = 0
        self.name = args[0]

    def __repr__(self):
        return '{0:s}: 0x{1:03x}'.format(self.name, self.address)


LUT = {
    'add': Add,
    'sub': Sub,
    'and': And,
    'or': Or,
    'xor': Xor,
    'cmp': Cmp,
    'mov': Mov,
    'sll': Sll,
    'slr': Slr,
    'srl': Srl,
    'sra': Sra,
    'in': In,
    'out': Out,
    'hlt': Hlt,
    'ld': Ld,
    'st': St,
    'li': Li,
    'b': B,
    'be': Be,
    'blt': Blt,
    'ble': Ble,
    'bne': Bne
}
