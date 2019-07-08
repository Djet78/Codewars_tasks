import re


class BadScriptError(Exception):
    pass


class AssemblerInterpreter:

    program = ''
    registers = {}
    compared_vals = ()
    output = ''
    depth = 0
    stop_exec = False

    operands_re = re.compile(r"'.+?'|\w+")

    func_parser_re = re.compile(r"""(?xsm)           # VERBOSE and DOTALL flags
                                    (^\w+?):         # Group 1: function (label) name
                                    (.*?(?=^\s*$))   # Group 2: function (label) body""")


    func_re = re.compile(r"""(?xsm)                  # VERBOSE and DOTALL flags 
                             (^\w+?:                 # function (label) name
                             .*?(?=^\s*$))           # function (label) body""")

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

    def _get_operands(self, line):
        return self.operands_re.findall(line)

    def _process_instruction(self, line):
        instruction = line.split(maxsplit=1)
        if len(instruction) == 2:
            operator, operands = instruction[0], self._get_operands(instruction[1])
        else:
            operator, operands = instruction[0], []
        return operator, operands

    def _is_stop_exec(self):
        if self.depth == 0:
            self.stop_exec = False
        return self.stop_exec

    def _validate_script(self, program):
        required_last_instructions = ('ret', 'end', 'jmp', 'jne', 'je', 'jge', 'jq', 'jle', 'jl', 'call')
        last_instruction = program[-1].split(maxsplit=1)[0]
        if last_instruction not in required_last_instructions:
            raise BadScriptError('Bad script!')

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
        for func in self.func_parser_re.findall(self.program):
            func_name = func[0]
            func_body = func[1]
            self.registers[func_name] = self.get_instructions_list(func_body)

    def _remove_function_declarations(self):
        self.program = self.func_re.sub('', self.program)

    def get_instructions_list(self, program):
        return [line.strip() for line in program.splitlines() if line.strip()]

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

    def mov(self, x, y):
        self.registers[x] = self._get_operand_num_value(y)

    def call(self, lbl):
        program = self.registers[lbl]

        self.depth += 1

        self.run_script(program)

        self.depth -= 1

    def ret(self, *args):
        self.stop_exec = True

    def end(self, *args):
        pass

    def cmp(self, x, y):
        self.compared_vals = (self._get_operand_num_value(x), self._get_operand_num_value(y))

    def jmp(self, lbl):
        self.call(lbl)

    def msg(self, *args):
        self.output = ''.join(self._get_operand_str_value(arg) for arg in args)

    # ---------------------------------------
    # ---------------- Main -----------------

    def exec(self, program):
        self._set_up(program)

        self._process_program()

        try:
            self.run_script()
        except BadScriptError:
            self._tear_down()
            return -1

        program_res = self.output

        self._tear_down()

        return program_res or -1

    def run_script(self, program=None):
        program = program or self.program

        self._validate_script(program)

        for instruction in program:

            if self._is_stop_exec():
                break

            operator, operands = self._process_instruction(instruction)
            getattr(AssemblerInterpreter, operator)(self, *operands)


prog1 = '''
mov   a, 2            ; value1
mov   b, 10           ; value2
mov   c, a            ; temp1
mov   d, b            ; temp2
call  proc_func
call  print
end

proc_func:
    cmp   d, 1
    je    continue
    mul   c, a
    dec   d
    call  proc_func

continue:
    ret

print:
    msg a, '^', b, ' = ', c
    ret
'''

assembler_interpreter = AssemblerInterpreter().exec
print(assembler_interpreter(prog1))
