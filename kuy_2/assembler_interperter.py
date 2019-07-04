import re


class AssemblerInterpreter:

    program = ''
    registers = {}
    instruction_n = 0
    compared_vals = ()
    output = ''

    func_parser_re = re.compile(r"""(?xs)                 # VERBOSE and DOTALL flags
                                    (\w+?):               # Group 1: function (label) name
                                    (?:(.+?ret))   # Group 2: function (label) body""")

    func_re = re.compile(r"""(?xs)                 # VERBOSE and DOTALL flags 
                             (\w+:                 # function (label) name
                             (?:.+?)(?=ret)ret)    # function (label) body""")

    comments_re = re.compile(r'(?m)(;.*)')
    main_workflow_re = re.compile(r'(?s)^(.*)(?=end)')

    # ---------------------------------------
    # ---------- Helper functions -----------
    # ---------------------------------------

    def _set_up(self, program):
        self.program = program

    def _tear_down(self):
        self.program = ''
        self.registers = {}
        self.instruction_n = 0
        self.compared_vals = ()
        self.output = ''

    def _get_operand_num_value(self, x):
        if x.lstrip('-').isdigit():
            return int(x)
        return self.registers.get(x)

    def _get_operand_str_value(self, x):
        return str(self.registers.get(x, x.strip("'")))

    def _process_instruction(self, line):
        operator, operands = line.split(maxsplit=1)
        operands = operands.split(', ')
        return operator, operands

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
    # ------- Conditional operators ---------

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

    def mov(self, x, y):
        self.registers[x] = self._get_operand_num_value(y)

    def call(self, lbl):
        program = self.registers[lbl]

        self.run_script(program)

    def cmp(self, x, y):
        self.compared_vals = (self._get_operand_num_value(x), self._get_operand_num_value(y))

    def jmp(self, lbl):
        self.call(lbl)

    def msg(self, *args):
        self.output = ''.join(self._get_operand_str_value(arg) for arg in args)

    # ---------------------------------------
    # -------- Program preprocessing --------

    def process_program(self):
        self.remove_comments()
        self.load_functions()
        self.remove_function_declarations()
        self.program = self.get_instructions_list(self.program)

    def remove_comments(self):
        self.program = self.comments_re.sub('', self.program)

    def load_functions(self):
        for func in self.func_parser_re.findall(self.program):
            func_name = func[0]
            func_body = func[1]
            self.registers[func_name] = self.get_instructions_list(func_body)

    def remove_function_declarations(self):
        self.program = self.func_re.sub('', self.program)

    def get_instructions_list(self, program):
        return [line.strip() for line in program.splitlines() if line.strip()]

    # ---------------------------------------
    # ---------------- Main -----------------

    def run(self, program):
        self._set_up(program)

        self.process_program()

        print(self.program)
        print(self.registers)
        if self.program[-1] == 'end':
            self.run_script()
        program_res = self.output

        self._tear_down()

        return program_res or -1

    def run_script(self, program=None):
        program = program or self.program

        for instruction in program[:-1]:
            operator, operands = self._process_instruction(instruction)
            getattr(AssemblerInterpreter, operator)(self, *operands)


prog = '''
mov   a, 8            ; value
mov   b, 0            ; next
mov   c, 0            ; counter
mov   d, 0            ; first
mov   e, 1            ; second
call  proc_fib
call  print
end

proc_fib:
    cmp   c, 2
    jl    func_0
    mov   b, d
    add   b, e
    mov   d, e
    mov   e, b
    inc   c
    cmp   c, a
    jle   proc_fib
    ret

func_0:
    mov   b, c
    inc   c
    jmp   proc_fib

print:
    msg   'Term ', a, ' of Fibonacci series is: ', b        ; output text
    ret
'''

assembler_interpreter = AssemblerInterpreter().run
print(assembler_interpreter(prog))
