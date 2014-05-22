#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import re

from sasm.instructions import Label, Option
from sasm.instructions import LUT as INST_LUT


class Assembler(object):
    def __init__(self):
        self.counter = 0
        self.debug_counter = 0
        self.instructions = []
        self.labels = {}
        self.options = {
            'address_radix': 'HEX',
            'data_radix': 'HEX',
            'depth': 4096
        }
        re_inst = '([a-zA-Z_][a-zA-Z_0-9]*)\(([a-zA-Z_0-9\-\ ,]*)\)'
        self.re_inst = re.compile(re_inst)

    def _add_instruction(self, line):
        self.debug_counter += 1

        # 行前後の空白を削除
        line = line.strip()
        # 空行とコメントのみの行を削除
        if (line == '') or (line[0] == ';'):
            return

        # 命令の形にマッチしているかチェック
        match = self.re_inst.match(line)

        if match is None:
            raise SyntaxError('Line: {0}, {1}'.format(self.debug_counter, line))

        groups = match.groups()
        # 引数がない場合は空文字列を設定する
        if len(groups) == 1:
            groups = tuple(groups, '')
        op = groups[0].lower()
        args = tuple(groups[1].lower().replace(' ', '').split(','))

        if op in INST_LUT:
            self.instructions.append(INST_LUT[op](args))
            self.counter += 1
        elif op == 'label':
            label = Label(args)
            label.address = self.counter
            self.labels[label.name] = label
        elif op == 'option':
            option = Option(args)
            self.options[option.name] = option.value
        else:
            raise LookupError('Instruction is not implemented: %s' % op)

    def load(self, data):
        self.counter = 0
        self.debug_counter = 0
        for line in data.split('\n'):
            self._add_instruction(line)
        self.options['address_radix'] = self.options['address_radix'].upper()
        self.options['data_radix'] = self.options['data_radix'].upper()
        return self

    def _format_instruction(self, addr, inst):
        result = '\t '
        if self.options['address_radix'] == 'BIN':
            result += '{0:012b}'.format(addr)
        else:
            result += '{0:03x}'.format(addr)
        result += ' : '
        if self.options['data_radix'] == 'BIN':
            result += '{0:016b}'.format(inst)
        else:
            result += '{0:04x}'.format(inst)
        result += ';\n'
        return result

    def compile(self):
        result = '-- SASM generated Memory Initialization File (.mif)\n\n'
        result += 'WIDTH=16;\n'
        result += 'DEPTH=%s;\n' % self.options['depth']
        result += 'ADDRESS_RADIX=%s;\n' % self.options['address_radix']
        result += 'DATA_RADIX=%s;\n\n' % self.options['data_radix']
        result += 'CONTENT BEGIN\n'
        self.counter = 0
        for inst in self.instructions:
            result += self._format_instruction(self.counter, inst.compile(self))
            self.counter += 1
        for i in range(self.counter, int(self.options['depth'])):
            result += self._format_instruction(i, 0)
        result += 'END;'
        return result

