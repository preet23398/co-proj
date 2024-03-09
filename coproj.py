opcodeList = ['0000011', '0010011', '0010011', '1100111','0100011']
registers = {'ra':'00001', 'sp':'00010', 'gp':'00011', 'tp':'00100', 't0':'00101', 't1':'00110', 't2':'00111', 't6':'11111', 's0':'01000', 's5' : '10101','fp':'01000', 's1':'01001', 'a0':'01010', 'a1':'01011', 'a2':'01100', 'a3':'01101', 'a4':'01110', 'a5':'01111', 'a6':'10000', 'a7':'10001', 't3':'11100', 't4':'11101', 't5':'11110', 't6':'11111'}
finalList = []

def decimal_to_binary(decimal,num_bits):
    decimal = int(decimal)
    if decimal >= 0:
        binary = bin(decimal)[2:].zfill(num_bits)
    else:
        positive_binary = bin(abs(decimal))[2:].zfill(num_bits)
        inverted = ''.join('1' if bit == '0' else '0' for bit in positive_binary)
        binary = bin(int(inverted, 2) + 1)[2:].zfill(num_bits)
    return binary

def Itype(instruction):

    instructionList1 = instruction.split()
    instructionList = instructionList1[1]
    instructionList2 = instructionList.split(',')

    whichInstruction = instructionList1[0]

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
    for i in finalList:
        print(i, end='')

def Stype(instruction):

    instructionList1 = instruction.split()
    instructionList = instructionList1[1]
    instructionList2 = instructionList.split(',')

    whichInstruction = instructionList1[0]

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
    for i in finalList:
        print(i, end='')



instruction = 'jalr ra,a5,-07'
instructionList = instruction.split()
whichInstruction = instructionList[0]


if whichInstruction == 'sw':
    Stype(instruction)
elif whichInstruction == 'lw' or whichInstruction == 'addi' or whichInstruction == 'sltiu' or whichInstruction == 'jalr':
    Itype(instruction)
else:
    print('no such instruction exists')
