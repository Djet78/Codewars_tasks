""" Kata: https://www.codewars.com/kata/58e24788e24ddee28e000053 """
"""
We want to create a simple interpreter of assembler which will support the following instructions:

mov x y - copies y (either a constant value or the content of a register) into register x
inc x - increases the content of register x by one
dec x - decreases the content of register x by one
jnz x y - jumps to an instruction y steps away (positive means forward, negative means backward), 
    but only if x (a constant or a register) is not zero
Register names are alphabetical (letters only). Constants are always integers (positive or negative).

Note: the jnz instruction moves relative to itself. For example, an offset of -1 would continue at the previous 
instruction, while an offset of 2 would skip over the next instruction.

The function will take an input list with the sequence of the program instructions and will return a dictionary 
with the contents of the registers.

Also, every inc/dec/jnz on a register will always be followed by a mov on the register first, so you don't need 
to worry about uninitialized registers.


 ``````````````````` Example ``````````````````````
simple_assembler(['mov a 5','inc a','dec a','dec a','jnz a -1','inc a'])

''' visualized:
mov a 5
inc a
dec a
dec a
jnz a -1
inc a
''''

The above code will:

set register a to 5,
increase its value by 1,
decrease its value by 2,
then decrease its value until it is zero (jnz a -1 jumps to the previous instruction if a is not zero)
and then increase its value by 1, leaving register a at 1.

So, the function should return :  {'a': 1}
"""


class Assembler:

    vars = {}
    instruction_n = 0

    # -------------------
    # Helper functions
    # -------------------

    def _get_value(self, x):
        if x.lstrip('-').isdigit():
            return int(x)
        return self.vars.get(x)

    def _process_line(self, line):
        command, *args = line.split()
        command = '_' + command
        return command, args

    def _tear_down(self):
        self.instruction_n = 0
        self.vars = {}

    # -------------------
    # Commands
    # -------------------

    def _mov(self, x, y):
        self.vars[x] = self._get_value(y)
        self.instruction_n += 1

    def _inc(self, x):
        self.vars[x] += 1
        self.instruction_n += 1

    def _dec(self, x):
        self.vars[x] -= 1
        self.instruction_n += 1

    def _jnz(self, x, y):
        if self._get_value(x) != 0:
            self.instruction_n += int(y)
        else:
            self.instruction_n += 1

    def main(self, program):
        while self.instruction_n < len(program):
            line = program[self.instruction_n]
            instruction, args = self._process_line(line)

            # an instruction call
            getattr(Assembler, instruction)(self, *args)

        res = self.vars
        self._tear_down()

        return res


simple_assembler = Assembler().main
