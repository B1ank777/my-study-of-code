import difflib


class AssemblyInterpreter:
    def __init__(self):
        self.registers = {f'r{i}': 0 for i in range(32)}  # 32个寄存器
        self.memory = [0] * 1024  # 简化：1K大小的内存
        self.pc = 0
        self.program = []
        self.labels = {}

        # 定义所有支持的指令操作符
        self.valid_ops = {
            'jal', 'jalr', 'beq', 'lui', 'lb', 'lw', 'sb', 'sw', 'add', 'sub', 'and', 'or',
            'addi', 'subi', 'la', 'bge', 'j'
        }

    def sext(self, imm):
        # 符号扩展，假设立即数为16位
        imm = int(imm)
        return imm if imm >= 0 else imm + (1 << 16)

    def load_program(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        self.program = [line.strip() for line in lines if line.strip() and not line.strip().startswith("//")]
        self._parse_labels()

    def _parse_labels(self):
        """解析程序中的标签"""
        for index, line in enumerate(self.program):
            if ':' in line:
                label = line.split(':')[0]
                if label in self.labels:
                    raise ValueError(f"标签 {label} 重定义")
                self.labels[label] = index
                self.program[index] = line.split(':')[1].strip()

    def run(self):
        while self.pc < len(self.program):
            instr = self.program[self.pc]
            try:
                self.execute(instr)
            except Exception as e:
                print(f"错误：在地址 {self.pc} 处，指令 '{instr}' 执行失败。{str(e)}")
                break

    def get_value(self, val):
        """获取值，确保是有效的寄存器或立即数"""
        if val in self.registers:
            return self.registers[val]
        try:
            return int(val)
        except ValueError:
            raise ValueError(f"无效的操作数：{val}")

    def execute(self, instr):
        tokens = instr.replace(",", "").split()
        if not tokens:
            raise ValueError(f"空指令或格式错误：'{instr}'")

        op = tokens[0]
        # 检查拼写错误
        if op not in self.valid_ops:
            # 使用 difflib.get_close_matches 检查拼写错误，获取最接近的指令
            suggestions = difflib.get_close_matches(op, self.valid_ops, n=1, cutoff=0.8)
            suggestion_msg = f"，建议使用指令：{suggestions[0]}" if suggestions else ""
            raise ValueError(f"拼写错误：未知操作符 '{op}'{suggestion_msg}")

        if op == 'jal':
            if len(tokens) != 3:
                raise ValueError(f"指令格式错误：'{instr}'")
            rd, imm = tokens[1], tokens[2]
            if rd != 'r1':
                raise ValueError(f"jal 指令中 rd 必须为 r1，发现 {rd}")
            self.registers[rd] = self.pc + 2
            self.pc += self.sext(imm)
        elif op == 'jalr':
            if len(tokens) != 4:
                raise ValueError(f"指令格式错误：'{instr}'")
            rd, rs1, imm = tokens[1], tokens[2], tokens[3]
            if rd not in self.registers or rs1 not in self.registers:
                raise ValueError(f"无效寄存器：'{rd}' 或 '{rs1}'")
            self.registers[rd] = self.pc + 2
            self.pc = self.registers[rs1] + self.sext(imm)
        elif op == 'beq':
            if len(tokens) != 4:
                raise ValueError(f"指令格式错误：'{instr}'")
            rs1, rs2, offset = tokens[1], tokens[2], tokens[3]
            if rs1 not in self.registers or rs2 not in self.registers:
                raise ValueError(f"无效寄存器：'{rs1}' 或 '{rs2}'")
            if self.registers[rs1] == self.registers[rs2]:
                self.pc += self.sext(offset)
            else:
                self.pc += 2
        elif op == 'lui':
            if len(tokens) != 3:
                raise ValueError(f"指令格式错误：'{instr}'")
            rd, imm = tokens[1], tokens[2]
            if rd not in self.registers:
                raise ValueError(f"无效寄存器：'{rd}'")
            self.registers[rd] = self.sext(imm) << 8
        elif op == 'lb':
            if len(tokens) != 3:
                raise ValueError(f"指令格式错误：'{instr}'")
            rd, offset_rs1 = tokens[1], tokens[2]
            offset, rs1 = offset_rs1.replace(")", "").split("(")
            addr = self.registers[rs1] + self.sext(offset)
            if addr < 0 or addr >= len(self.memory):
                raise ValueError(f"内存访问越界：地址 {addr}")
            self.registers[rd] = self.memory[addr] & 0xFF
        elif op == 'lw':
            if len(tokens) != 3:
                raise ValueError(f"指令格式错误：'{instr}'")
            rd, offset_rs1 = tokens[1], tokens[2]
            offset, rs1 = offset_rs1.replace(")", "").split("(")
            addr = self.registers[rs1] + self.sext(offset)
            if addr < 0 or addr >= len(self.memory):
                raise ValueError(f"内存访问越界：地址 {addr}")
            self.registers[rd] = self.memory[addr]
        elif op == 'sb':
            if len(tokens) != 3:
                raise ValueError(f"指令格式错误：'{instr}'")
            rs2, offset_rs1 = tokens[1], tokens[2]
            offset, rs1 = offset_rs1.replace(")", "").split("(")
            addr = self.registers[rs1] + self.sext(offset)
            if addr < 0 or addr >= len(self.memory):
                raise ValueError(f"内存访问越界：地址 {addr}")
            self.memory[addr] = self.registers[rs2] & 0xFF
        elif op == 'sw':
            if len(tokens) != 3:
                raise ValueError(f"指令格式错误：'{instr}'")
            rs2, offset_rs1 = tokens[1], tokens[2]
            offset, rs1 = offset_rs1.replace(")", "").split("(")
            addr = self.registers[rs1] + self.sext(offset)
            if addr < 0 or addr >= len(self.memory):
                raise ValueError(f"内存访问越界：地址 {addr}")
            self.memory[addr] = self.registers[rs2]
        elif op in {'add', 'sub', 'and', 'or'}:
            if len(tokens) != 4:
                raise ValueError(f"指令格式错误：'{instr}'")
            rd, rs1, rs2 = tokens[1], tokens[2], tokens[3]
            if rd not in self.registers or rs1 not in self.registers or rs2 not in self.registers:
                raise ValueError(f"无效寄存器：'{rd}', '{rs1}' 或 '{rs2}'")
            if op == 'add':
                self.registers[rd] = self.registers[rs1] + self.registers[rs2]
            elif op == 'sub':
                self.registers[rd] = self.registers[rs1] - self.registers[rs2]
            elif op == 'and':
                self.registers[rd] = self.registers[rs1] & self.registers[rs2]
            elif op == 'or':
                self.registers[rd] = self.registers[rs1] | self.registers[rs2]
        elif op in {'addi', 'subi'}:
            if len(tokens) != 4:
                raise ValueError(f"指令格式错误：'{instr}'")
            rd, rs1, imm = tokens[1], tokens[2], self.sext(tokens[3])
            if rd not in self.registers or rs1 not in self.registers:
                raise ValueError(f"无效寄存器：'{rd}' 或 '{rs1}'")
            if op == 'addi':
                self.registers[rd] = self.registers[rs1] + imm
            else:
                self.registers[rd] = self.registers[rs1] - imm
        elif op == 'la':
            if len(tokens) != 3:
                raise ValueError(f"指令格式错误：'{instr}'")
            rd, array_size = tokens[1], int(tokens[2])
            self.execute(f"lui t1, 0x10")
            self.execute(f"addi t1, t1, {array_size}")
            self.execute(f"lb {rd}, 0(t1)")
        elif op == 'bge':
            if len(tokens) != 4:
                raise ValueError(f"指令格式错误：'{instr}'")
            rs1, rs2, label = tokens[1], tokens[2], tokens[3]
            if rs1 not in self.registers or rs2 not in self.registers:
                raise ValueError(f"无效寄存器：'{rs1}' 或 '{rs2}'")
            if label not in self.labels:
                raise ValueError(f"未知标签：'{label}'")
            if self.registers[rs1] >= self.registers[rs2]:
                self.pc = self.labels[label]
            else:
                self.pc += 2
        elif op == 'j':
            if len(tokens) != 2:
                raise ValueError(f"指令格式错误：'{instr}'")
            label = tokens[1]
            if label not in self.labels:
                raise ValueError(f"未知标签：'{label}'")
            self.pc = self.labels[label]
        else:
            raise ValueError(f"未知指令：{op}")

        self.pc += 2  # 默认下一条指令步长为2

    def dump(self):
        print("寄存器：")
        for k, v in self.registers.items():
            print(f"{k}: {v}")


interpreter = AssemblyInterpreter()
interpreter.load_program("program.txt")
interpreter.run()
interpreter.dump()
