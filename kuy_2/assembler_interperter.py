import re


class AssemblerInterpreter:

    program = ''
    registers = {}
    compared_vals = ()
    output = ''
    depth = 0
    stop_exec = False

    # preserved_words = ('inc', 'dec', 'add', 'sub', 'mul', 'div', 'jne', 'je', 'jge', 'jg', 'jle', 'jl',
    #                    'mov', 'call', 'cmp', 'jmp', 'msg', 'ret', 'end')
    # func_parser_re = re.compile(r"""(?xsm)                   # VERBOSE and DOTALL flags
    #                                 (^\w+?)(?<!{}):          # Group 1: function (label) name
    #                                 (.*?(?=^\s*$))           # Group 2: function (label) body
    #                                 """.format('|'.join(preserved_words)))

    operands_re = re.compile(r"'.+?'|\w+")

    func_parser_re = re.compile(r"""(?xsm)           # VERBOSE and DOTALL flags
                                    (\w+?):          # Group 1: function (label) name
                                    (.*?(?=^\s*$))   # Group 2: function (label) body""")


    func_re = re.compile(r"""(?xs)                   # VERBOSE and DOTALL flags 
                             (\w+:                   # function (label) name
                             (?:.+?)(?=ret)ret)      # function (label) body""")

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
        self.depth = 0

    def _get_operand_num_value(self, x):
        if x.lstrip('-').isdigit():
            return int(x)
        return self.registers.get(x)

    def _get_operand_str_value(self, x):
        return str(self.registers.get(x, x.strip("'")))

    def _process_instruction(self, line):
        instruction = line.split(maxsplit=1)
        if len(instruction) == 2:
            operator, operands = instruction[0], self.operands_re.findall(instruction[1])
        else:
            operator, operands = instruction[0], []
        return operator, operands

    def _is_stop_exec(self):
        if not self.depth:
            self.stop_exec = False
        return self.stop_exec
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

        self.depth += 1

        self.run_script(program)

        self.depth -= 1

    def ret(self, *args):
        self.stop_exec = True

    def cmp(self, x, y):
        self.compared_vals = (self._get_operand_num_value(x), self._get_operand_num_value(y))

    def jmp(self, lbl):
        self.call(lbl)

    def msg(self, *args):
        self.output = ''.join(self._get_operand_str_value(arg) for arg in args)

    # ---------------------------------------
    # -------- Program preprocessing --------

    def _process_program(self):
        self._remove_comments()
        self._load_functions()
        self._remove_function_declarations()
        self.program = self.get_instructions_list(self.program)

    def _remove_comments(self):
        self.program = self.comments_re.sub('', self.program)
        print(self.program)

    def _load_functions(self):
        for func in self.func_parser_re.findall(self.program):
            func_name = func[0]
            func_body = func[1]
            self.registers[func_name] = self.get_instructions_list(func_body)

    def _remove_function_declarations(self):
        self.program = self.func_re.sub('', self.program)

    def get_instructions_list(self, program):
        return [line.strip() for line in program.splitlines() if line.strip()]

    # ---------------------------------------
    # ---------------- Main -----------------

    def exec(self, program):
        self._set_up(program)

        self._process_program()
        if self.program.pop() == 'end':
            self.run_script()
        program_res = self.output

        self._tear_down()

        return program_res or -1

    def run_script(self, program=None):
        program = program or self.program

        for instruction in program:

            if self._is_stop_exec():
                break

            operator, operands = self._process_instruction(instruction)
            getattr(AssemblerInterpreter, operator)(self, *operands)


prog1 = '''
mov e, 14   ; instruction mov e, 14
mov d, 6   ; instruction mov d, 6
call func
msg 'Random result: ', c
end

func:
	cmp e, d
	jl exit
	mov c, e
	mul c, d
	ret
; Do nothing
exit:
	msg 'Do nothing'
'''

prog2 = """
mov u, 2   ; instruction mov u, 2
mov b, 1   ; instruction mov b, 1
call func
msg 'Random result: ', q
end

func:
	cmp u, b
	jg exit
	mov q, u
	div q, b
	ret
; Do nothing
exit:
	msg 'Do nothing'

"""



assembler_interpreter = AssemblerInterpreter().exec
print(assembler_interpreter(prog1))
# print(assembler_interpreter(prog2))

