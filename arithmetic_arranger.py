# This entrypoint file to be used in development. Start by reading README.md
# arithmetic_arranger.py
# freeCodeCamp rslt Project 01
# Gabriel Milicu

# define the homework (hw)
hw = ["1 + 8", "56 - 64",  "9734 + 621", "159 + 42", "1 - 2"]
results=True
#results=False

# define the function
def arithmetic_arranger(hw, results):

# max 5 problems check
  if len(hw) > 5:
    return 'Error: Too many problems.'

# define the lists for the new arrange on 4 lines
  line1 = []
  line2 = []
  line3 = []
  line4 = []

# define the result string to be displayed with 4 spaces between problems
  space = ' ' * 4

# loop going through each problem
# split the entry into problems and each problem into 2 operands: operand1 = first operand and op_operand2 = operator + operand2
  for ope in hw:
    operand1 = '  ' + ope.split()[0]
    op_operand2 = ope.split(' ', 1)[1]

#  max 4 digits check
    if len(ope.split()[0]) > 4 or len(ope.split()[2]) > 4:
      return "Error: Numbers cannot be more than four digits."

#  only '+' or '-' operators check
    if op_operand2[0] != '+' and op_operand2[0] != '-':
      return "Error: Operator must be '+' or '-'."

#  numbers by only digits check
    if operand1.lstrip().isdigit() != True or op_operand2[2:].isdigit() != True:
      return "Error: Numbers must only contain digits."

# operands arrange at the right width
    d1 = len(operand1)- len(op_operand2)
    d2 = len(op_operand2) - len(operand1)
    if d1 > 0:
      op_operand2 = op_operand2[0] + ' ' * (d1 + 1) + op_operand2[2:]
    elif d2 > 0:
      operand1 = ' ' * d2 + operand1

# identify add or substract operation and calculate the operation result
    if op_operand2[0] == '+':
      rslt = int(operand1) + int(op_operand2[2:])
    else:
      rslt = int(operand1) - int(op_operand2[2:])

# process  the result to mach the rules
    rslt_str = str(rslt)
    length_rslt = len(rslt_str)
    rslt_str = ' ' * 2 + rslt_str
    max_width = max([len(operand1.lstrip()), len(op_operand2[1:].lstrip())])

    if max_width > length_rslt:
      rslt_str = ' ' * (max_width - length_rslt) + rslt_str
    elif max_width < length_rslt:
      rslt_str = rslt_str[1:]

# final arrangement of the operations results on 4 lines
    line1.append(operand1)
    line2.append(op_operand2)
    line3.append('-' * len(op_operand2))
    line4.append(rslt_str)

    g_line1 = space.join(line1)
    g_line2 = space.join(line2)
    g_line3 = space.join(line3)
    g_line4 = space.join(line4)

# function return
  if results is True:
    return g_line1 + ('\n') + g_line2 + ('\n') + g_line3 + ('\n') + g_line4
  else:
    return g_line1 + ('\n') + g_line2 + ('\n') + g_line3
# results True / False check

final=arithmetic_arranger(hw, results)
print(final)