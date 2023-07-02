"""
https://www.codewars.com/kata/58e61f3d8ff24f774400002c

We want to create an interpreter of assembler which will support the following instructions:

mov x, y - copy y (either an integer or the value of a register) into register x.
inc x - increase the content of register x by one.
dec x - decrease the content of register x by one.
add x, y - add the content of the register x with y (either an integer or the value of a register) and
           stores the result in x (i.e. register[x] += y).
sub x, y - subtract y (either an integer or the value of a register) from the register x and stores the result
           in x (i.e. register[x] -= y).
mul x, y - same with multiply (i.e. register[x] *= y).
div x, y - same with integer division (i.e. register[x] /= y).
label: - define a label position (label = identifier + ":", an identifier being a string that does not match
         any other command). Jump commands and call are aimed to these labels positions in the program.
jmp lbl - jumps to to the label lbl.
cmp x, y - compares x (either an integer or the value of a register) and y (either an integer or the value of
           a register). The result is used in the conditional jumps (jne, je, jge, jg, jle and jl)
jne lbl - jump to the label lbl if the values of the previous cmp command were not equal.
je lbl - jump to the label lbl if the values of the previous cmp command were equal.
jge lbl - jump to the label lbl if x was greater or equal than y in the previous cmp command.
jg lbl - jump to the label lbl if x was greater than y in the previous cmp command.
jle lbl - jump to the label lbl if x was less or equal than y in the previous cmp command.
jl lbl - jump to the label lbl if x was less than y in the previous cmp command.
call lbl - call to the subroutine identified by lbl. When a ret is found in a subroutine, the instruction pointer
           should return to the instruction next to this call command.
ret - when a ret is found in a subroutine, the instruction pointer should return to the instruction that called the
      current function.
msg 'Register: ', x - this instruction stores the output of the program. It may contain text strings
                      (delimited by single quotes) and registers. The number of arguments isn't limited and will
                      vary, depending on the program.
end - this instruction indicates that the program ends correctly, so the stored output is returned (if the program
      terminates without this instruction it should return the default output: see below).
; comment - comments should not be taken in consideration during the execution of the program.

Output format:
The normal output format is a string (returned with the end command).

If the program does finish itself without using an end instruction, the default return value is:

-1 (as an integer)

Input format:
The function/method will take as input a multiline string of instructions, delimited with EOL characters.
Please, note that the instructions may also have indentation for readability purposes.
"""
import re
import unittest


class BadScriptError(Exception):
    pass


class AssemblerInterpreter:

    comments_re = re.compile(r'(?m)(;.*)')

    func_def_re = re.compile(r"""(?xsm)            # Matches function name and body
                                  (^\w+?):         # Group 1: function (label) name
                                  (.*?(?=^\s*$))   # Group 2: function (label) body""")

    func_re = re.compile(r"""(?xsm)                # Match whole func def
                             (^\w+?:               # function (label) name
                             .*?(?=^\s*$))         # function (label) body""")

    operands_re = re.compile(r"'.+?'|\w+")

    def __init__(self, program):
        self.program = program
        self.registers = {}
        self.compared_vals = ()
        self.output = ''
        self.depth = 0
        self.stop_exec = False

    # ---------------------------------------
    # ---------- Helper functions -----------
    # ---------------------------------------

    def _get_operand_num_value(self, x):
        if x.lstrip('-').isdigit():
            return int(x)
        return self.registers.get(x)

    def _get_operand_str_value(self, x):
        return str(self.registers.get(x, x.strip("'")))

    def _get_operands(self, line):
        return self.operands_re.findall(line)

    # ---------------------------------------
    # -------- Program preprocessing --------

    def _process_program(self):
        self._remove_comments()
        self._load_functions()
        self._remove_function_declarations()
        self.program = self.get_instructions_list(self.program)

    def _remove_comments(self):
        self.program = self.comments_re.sub('', self.program)

    def _load_functions(self):
        for func_name, func_body in self.func_def_re.findall(self.program):
            self.registers[func_name] = self.get_instructions_list(func_body)

    def _remove_function_declarations(self):
        self.program = self.func_re.sub('', self.program)

    def get_instructions_list(self, program):
        return [line.strip() for line in program.splitlines() if line.strip()]

    # ---------------------------------------
    # ---------- Program processing ---------

    def _process_instruction(self, line):
        instruction = line.split(maxsplit=1)
        if len(instruction) == 2:
            operator, operands = instruction[0], self._get_operands(instruction[1])
        else:
            operator, operands = instruction[0], []
        return operator, operands

    def _validate_script(self, program):
        required_last_instructions = ('ret', 'end', 'jmp', 'jne', 'je', 'jge', 'jq', 'jle', 'jl', 'call')
        last_instruction = program[-1].split(maxsplit=1)[0]
        if last_instruction not in required_last_instructions:
            raise BadScriptError('Bad script!')

    # ---------------------------------------
    # ----------- Math operators ------------

    def inc(self, x):
        self.registers[x] += 1

    def dec(self, x):
        self.registers[x] -= 1

    def add(self, x, y):
        self.registers[x] += self._get_operand_num_value(y)

    def sub(self, x, y):
        self.registers[x] -= self._get_operand_num_value(y)

    def mul(self, x, y):
        self.registers[x] *= self._get_operand_num_value(y)

    def div(self, x, y):
        self.registers[x] //= self._get_operand_num_value(y)

    # ---------------------------------------
    # --------- Conditional calls -----------

    def jne(self, lbl):
        if self.compared_vals[0] != self.compared_vals[1]:
            self.call(lbl)

    def je(self, lbl):
        if self.compared_vals[0] == self.compared_vals[1]:
            self.call(lbl)

    def jge(self, lbl):
        if self.compared_vals[0] >= self.compared_vals[1]:
            self.call(lbl)

    def jg(self, lbl):
        if self.compared_vals[0] > self.compared_vals[1]:
            self.call(lbl)

    def jle(self, lbl):
        if self.compared_vals[0] <= self.compared_vals[1]:
            self.call(lbl)

    def jl(self, lbl):
        if self.compared_vals[0] < self.compared_vals[1]:
            self.call(lbl)

    # ---------------------------------------
    # ----------- Other operators -----------

    def cmp(self, x, y):
        self.compared_vals = (self._get_operand_num_value(x), self._get_operand_num_value(y))

    def call(self, lbl):
        program = self.registers[lbl]

        self.depth += 1

        self.run_script(program)

        self.depth -= 1

    def end(self, *args):
        """ For compatibility with other method calls """
        pass

    def jmp(self, lbl):
        self.call(lbl)

    def mov(self, x, y):
        self.registers[x] = self._get_operand_num_value(y)

    def msg(self, *args):
        self.output = ''.join(self._get_operand_str_value(arg) for arg in args)

    def ret(self, *args):
        self.stop_exec = True

    # ---------------------------------------
    # -------------- Executors --------------

    def _is_stop_exec(self):
        if self.depth == 0:
            self.stop_exec = False
        return self.stop_exec

    def exec(self):
        """ Entry point for whole script execution """
        self._process_program()

        try:
            self.run_script()
        except BadScriptError:
            return -1

        return self.output

    def run_script(self, program=None):
        program = program or self.program

        self._validate_script(program)

        for instruction in program:

            if self._is_stop_exec():
                break

            operator, operands = self._process_instruction(instruction)
            getattr(AssemblerInterpreter, operator)(self, *operands)


def assembler_interpreter(prog):
    interpreter = AssemblerInterpreter(prog)
    res = interpreter.exec()
    return res
