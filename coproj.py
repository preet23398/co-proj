
def In():
    with open("input.txt", "r") as file:
        lines = file.readlines()
        b=lines
        #b=["lui a1,2048"]
    for line in lines:
        a=line.split(" ")
    return a,b
a,lines=In()


def decimal_to_binary(decimal,num_bits):
        decimal = int(decimal)
        if decimal >= 0:
            binary = bin(decimal)[2:].zfill(num_bits)
        else:
            positive_binary = bin(abs(decimal))[2:].zfill(num_bits)
            inverted = ''.join('1' if bit == '0' else '0' for bit in positive_binary)
            binary = bin(int(inverted, 2) + 1)[2:].zfill(num_bits)
        return binary
def U_type(instruction):
    temp=a[1].split(',')
    rd = registers.get(temp[0])
    opcode=opcodemap.get(a[0])
    imm = int(temp[1])
    immbinary = decimal_to_binary(imm, 20)
    value =   immbinary[-1::-1] + rd +opcode
    return value

def assembleinstruction(instruction):
    mnemonic = a[0]
    opcode = opcodemap.get(mnemonic)
    temp=a[1].split(",")

    rs1, rs2 = registers.get(temp[0]), registers.get(temp[1])
    imm = int(temp[2])
        
    function = functionmap.get(mnemonic)        
    immbinary = decimal_to_binary(imm, 12)
    imm_high = immbinary[0] + immbinary[2:8]
    imm_low = immbinary[8:] 
    binaryinstruction =     imm_high+rs2+rs1+'0'  +function+ imm_low + opcode
    return binaryinstruction




def Itype(instruction):

    instructionList1 = instruction.split()
    instructionList = instructionList1[1]
    instructionList2 = instructionList.split(',')

    whichInstruction = a[0]

    if whichInstruction == 'lw':
        opcode = opcodeList[0]

        destinationReg = instructionList2[0]
        codeOfdestinationReg = registers.get(destinationReg)

        function = '010'

        immediateList = (instructionList2[1]).split('(')
        immediate = immediateList[0]
        immediate_val = decimal_to_binary(immediate,12)

        immediateList2=immediateList[1]
        sourceReg = immediateList2[0:2]
        sourceRegvalue = registers.get(sourceReg)

    elif whichInstruction == 'addi':
        opcode = opcodeList[1]

        destinationReg = instructionList2[0]
        codeOfdestinationReg = registers.get(destinationReg)

        function = '000'

        immediate_val = decimal_to_binary(instructionList2[2],12)

        sourceRegvalue = registers.get(instructionList2[1])

    elif whichInstruction == 'sltiu':
        opcode = opcodeList[2]

        destinationReg = instructionList2[0]
        codeOfdestinationReg = registers.get(destinationReg)

        function = '011'

        immediate_val = decimal_to_binary(instructionList2[2],12)

        sourceRegvalue = registers.get(instructionList2[1])

    elif whichInstruction == 'jalr':
        opcode = opcodeList[3]

        destinationReg = instructionList2[0]
        codeOfdestinationReg = registers.get(destinationReg)

        function = '000'

        sourceRegvalue = registers.get(instructionList2[1])

        immediate_val = decimal_to_binary(instructionList2[2],12)

    else:
        print('no such i-type instruction exists')

    finalList.append(immediate_val)
    finalList.append(sourceRegvalue)
    finalList.append(function)
    finalList.append(codeOfdestinationReg)
    finalList.append(opcode)
    temp=''
    for i in finalList:
        temp+=i
    with open("output.txt", "w") as output_file:
        
            output_file.write(temp)

def Stype(instruction):

    instructionList1 = instruction.split()
    instructionList = instructionList1[1]
    instructionList2 = instructionList.split(',')


    opcode = opcodeList[4]

    destinationReg = instructionList2[0]
    codeOfdestinationReg = registers.get(destinationReg)

    immediateList = (instructionList2[1]).split('(')
    immediate = immediateList[0]
    immediate_val = decimal_to_binary(immediate,12)

    immediate_val1 = immediate_val[0:7]
    immediate_val2 = immediate_val[7:]

    function = '010'

    immediateList2=immediateList[1]
    sourceReg = immediateList2[0:2]
    sourceRegvalue = registers.get(sourceReg)

    finalList.append(immediate_val1)
    finalList.append(codeOfdestinationReg)
    finalList.append(sourceRegvalue)
    finalList.append(function)
    finalList.append(immediate_val2)
    finalList.append(opcode)
    temp=''
    for i in finalList:
        temp+=i
    with open("output.txt", "w") as output_file:
        
            output_file.write(temp)
    


if a[0]== 'add' or a[0]== 'sub' or a[0]== 'sll' or a[0]== 'slt' or a[0] == 'sltu' or a[0]== 'xor' or a[0]== 'srl' or a[0]== 'and'  or a[0]== 'or':
    all_lines_numbers = []  
    replacements = {
        "add": "0110011",
        "sub": "0110011",
        "sll": "0010011",
        "slt": "0110011",
        "sltu": "0110011",
        "xor": "0110011",
        "srl": "0110011",
        "or": "0110011",
        "and": "0110011",
        "zero": "00000",
        "ra": "00001",
        "sp": "00010",
        "gp": "00011",
        "tp": "00100",
        "t0": "00101",
        "t1": "00110",
        "t2": "00111",
        "s0": "01000",
        "fp": "01000",
        "s1": "01001",
        "a0": "01010",
        "a1": "01011",
        "a2": "01100",
        "a3": "01101",
        "a4": "01110",
        "a5": "01111",
        "a6": "10000",
        "a7": "10001",
        "s2": "10010",
        "s3": "10011",
        "s4": "10100",
        "s5": "10101",
        "s6": "10110",
        "s7": "10111",
        "s8": "11000",
        "s9": "11001",
        "s10": "11010",
        "s11": "11011",
        "t3": "11100",
        "t4": "11101",
        "t5": "11110",
        "t6": "11111",
        "zero,": "00000",
        "ra,": "00001",
        "sp,": "00010",
        "gp,": "00011",
        "tp,": "00100",
        "t0,": "00101",
        "t1,": "00110",
        "t2,": "00111",
        "s0,": "01000",
        "fp,": "01000",
        "s1,": "01001",
        "a0,": "01010",
        "a1,": "01011",
        "a2,": "01100",
        "a3,": "01101",
        "a4,": "01110",
        "a5,": "01111",
        "a6,": "10000",
        "a7,": "10001",
        "s2,": "10010",
        "s3,": "10011",
        "s4,": "10100",
        "s5,": "10101",
        "s6,": "10110",
        "s7,": "10111",
        "s8,": "11000",
        "s9,": "11001",
        "s10,": "11010",
        "s11,": "11011",
        "t3,": "11100",
        "t4,": "11101",
        "t5,": "11110",
        "t6,": "11111",
    }
    for line in lines:
            line = line.strip()  # Remove leading/trailing whitespaces
            if line.lower() == 'done':
                break

            # Split the line into words
            words = line.split()
            
            # Initialize the list to store numbers for this line
            line_numbers = []

            # Process each word in the line
            for i, word in enumerate(words):
                if i == 0:  # First word
                    line_numbers.append(replacements.get(word.lower(), word))
                else:  # Subsequent words separated by commas
                    for w in word.split(','):
                        line_numbers.append(replacements.get(w.lower(), w))

            # Check if "add" is present and add "000" after the second word and "0000000" at the end
            if "add" in words:
                idx = line_numbers.index("0110011")
                if idx + 2 < len(line_numbers):
                    line_numbers.insert(idx + 2, "000")
                line_numbers.append("0000000")
            if "sub" in words:
                idx = line_numbers.index("0110011")
                if idx + 2 < len(line_numbers):
                    line_numbers.insert(idx + 2, "000")
                line_numbers.append("0100000")
            if "sll" in words:
                idx = line_numbers.index("0110011")
                if idx + 2 < len(line_numbers):
                    line_numbers.insert(idx + 2, "001")
                line_numbers.append("0000000") 
            if "slt" in words:
                idx = line_numbers.index("0110011")
                if idx + 2 < len(line_numbers):
                    line_numbers.insert(idx + 2, "010")
                line_numbers.append("0000000")  
            if "sltu" in words:
                idx = line_numbers.index("0110011")
                if idx + 2 < len(line_numbers):
                    line_numbers.insert(idx + 2, "011")
                line_numbers.append("0000000")    
            if "xor" in words:
                idx = line_numbers.index("0110011")
                if idx + 2 < len(line_numbers):
                    line_numbers.insert(idx + 2, "100")
                line_numbers.append("0000000")      
            if "srl" in words:
                idx = line_numbers.index("0110011")
                if idx + 2 < len(line_numbers):
                    line_numbers.insert(idx + 2, "101")
                line_numbers.append("0000000")      
            if "or" in words:
                idx = line_numbers.index("0110011")
                if idx + 2 < len(line_numbers):
                    line_numbers.insert(idx + 2, "110")
                line_numbers.append("0000000")      
            if "and" in words:
                idx = line_numbers.index("0110011")
                if idx + 2 < len(line_numbers):
                    line_numbers.insert(idx + 2, "111")
                line_numbers.append("0000000")      

            # Concatenate the numbers for this line into a single string and add to the list
            all_lines_numbers.append("".join(line_numbers))
    final= ("".join(line_numbers[::-1]))
    with open("output.txt", "w") as output_file:
        
            output_file.write(final + "\n")


elif a[0]== 'sw':
    opcodeList = ['0000011', '0010011', '0010011', '1100111','0100011']
    registers = {'ra':'00001', 'sp':'00010', 'gp':'00011', 'tp':'00100', 't0':'00101', 't1':'00110', 't2':'00111', 't3':'11100', 't4':'11101', 't5':'11110', 't6':'11111', 's0':'01000', 's1':'01001','s2':'10010', 's3':'10011', 's4':'10100', 's5' : '10101', 's6':'10110', 's7':'10111', 's8':'11000', 's9':'11001', 's10':'11010', 's11':'11011', 'fp':'01000', 'a0':'01010', 'a1':'01011', 'a2':'01100', 'a3':'01101', 'a4':'01110', 'a5':'01111', 'a6':'10000', 'a7':'10001'}
    finalList = []
    instruction = lines[0].strip()
    instructionList=instruction.split()
    def decimal_to_binary(decimal,num_bits):
        decimal = int(decimal)
        if decimal >= 0:
            binary = bin(decimal)[2:].zfill(num_bits)
        else:
            positive_binary = bin(abs(decimal))[2:].zfill(num_bits)
            inverted = ''.join('1' if bit == '0' else '0' for bit in positive_binary)
            binary = bin(int(inverted, 2) + 1)[2:].zfill(num_bits)
        return binary
    Stype(instruction)
    print(end='\n')
elif a[0]=="lw" or a[0]=="addi" or a[0]=="sltiu" or a[0]=="jalr":
    opcodeList = ['0000011', '0010011', '0010011', '1100111','0100011']
    registers = {'ra':'00001', 'sp':'00010', 'gp':'00011', 'tp':'00100', 't0':'00101', 't1':'00110', 't2':'00111', 't3':'11100', 't4':'11101', 't5':'11110', 't6':'11111', 's0':'01000', 's2':'10010', 's3':'10011', 's4':'10100', 's5' : '10101', 's6':'10110', 's7':'10111', 's8':'11000', 's9':'11001', 's10':'11010', 's11':'11011', 'fp':'01000', 'a0':'01010', 'a1':'01011', 'a2':'01100', 'a3':'01101', 'a4':'01110', 'a5':'01111', 'a6':'10000', 'a7':'10001'}
    finalList = []
    instruction = lines[0].strip()
    instructionList=instruction.split()
    def decimal_to_binary(decimal,num_bits):
        decimal = int(decimal)
        if decimal >= 0:
            binary = bin(decimal)[2:].zfill(num_bits)
        else:
            positive_binary = bin(abs(decimal))[2:].zfill(num_bits)
            inverted = ''.join('1' if bit == '0' else '0' for bit in positive_binary)
            binary = bin(int(inverted, 2) + 1)[2:].zfill(num_bits)
        return binary
    Itype(instruction)
    print(end='\n')

elif a[0]=="beq" or a[0]=="bne" or a[0]=="blt" or a[0]=="bge" or a[0]=="bltu" or a[0]=="bgeu":
    registers = {'ra':'00001', 'sp':'00010', 'gp':'00011', 'tp':'00100', 't0':'00101', 't1':'00110', 't2':'00111', 't3':'11100', 't4':'11101', 't5':'11110', 't6':'11111', 's0':'01000', 's1':'01001','s2':'10010', 's3':'10011', 's4':'10100', 's5' : '10101', 's6':'10110', 's7':'10111', 's8':'11000', 's9':'11001', 's10':'11010', 's11':'11011', 'fp':'01000', 'a0':'01010', 'a1':'01011', 'a2':'01100', 'a3':'01101', 'a4':'01110', 'a5':'01111', 'a6':'10000', 'a7':'10001'}
    opcodemap = {
    "beq": "1100011",
    "bne": "1100011",
    "blt": "1100011",
    "bge": "1100011",
    "bltu": "1100011",
    "bgeu": "1100011",
    "auipc": "0010111",
    "lui": "0110111"
    }

    functionmap = {
        "beq": "000",
        "bne": "001",
        "blt": "100",
        "bge": "101",
        "bltu": "110",
        "bgeu": "111"
    }
    line = lines[0].strip()

    finalvalue=assembleinstruction(line)
    with open("output.txt", 'w') as file:
        for binaryinstr in finalvalue:
            file.write(binaryinstr)
elif a[0]=="lui" or a[0]=="aiupc" :
    registers = {'ra':'00001', 'sp':'00010', 'gp':'00011', 'tp':'00100', 't0':'00101', 't1':'00110', 't2':'00111', 't3':'11100', 't4':'11101', 't5':'11110', 't6':'11111', 's0':'01000', 's1':'01001','s2':'10010', 's3':'10011', 's4':'10100', 's5' : '10101', 's6':'10110', 's7':'10111', 's8':'11000', 's9':'11001', 's10':'11010', 's11':'11011', 'fp':'01000', 'a0':'01010', 'a1':'01011', 'a2':'01100', 'a3':'01101', 'a4':'01110', 'a5':'01111', 'a6':'10000', 'a7':'10001'}
    opcodemap = {
    "beq": "1100011",
    "bne": "1100011",
    "blt": "1100011",
    "bge": "1100011",
    "bltu": "1100011",
    "bgeu": "1100011",
    "auipc": "0010111",
    "lui": "0110111"
    }

    functionmap = {
        "beq": "000",
        "bne": "001",
        "blt": "100",
        "bge": "101",
        "bltu": "110",
        "bgeu": "111"
    }
    line = lines[0].strip()
    finalvalue=U_type(line)
    with open("output.txt", 'w') as file:
        for binaryinstr in finalvalue:
            file.write(binaryinstr)
elif a[0]=='jal':

    registers = {'ra':'00001', 'sp':'00010', 'gp':'00011', 'tp':'00100', 't0':'00101', 't1':'00110', 't2':'00111', 't3':'11100', 't4':'11101', 't5':'11110', 't6':'11111', 's0':'01000', 's1':'01001','s2':'10010', 's3':'10011', 's4':'10100', 's5' : '10101', 's6':'10110', 's7':'10111', 's8':'11000', 's9':'11001', 's10':'11010', 's11':'11011', 'fp':'01000', 'a0':'01010', 'a1':'01011', 'a2':'01100', 'a3':'01101', 'a4':'01110', 'a5':'01111', 'a6':'10000', 'a7':'10001'}
    temp=a[1].split(',')
    imm = decimal_to_binary(temp[1],21)
    value = imm[0] + imm[10:20] + imm[9]+ imm[1:9] + registers.get(temp[0]) + "1101111"
    with open("output.txt", 'w') as file:
        file.write(value)
    
