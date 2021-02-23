with open('program','r') as fp:
  program = fp.read()
program = list(program)
loc = 0
ptr = 0
while loc < len(program):
  op = program[loc]
  if op=='1':
    if program[ptr] == '0':
      loc=ptr
  elif op == '2':
    x=program[ptr]
    try:
      x = str(int(x)+1)
      if x == '10': x=0
    except ValueError:
      x=ord(program[ptr])
      x=chr(x+1)
    program[ptr] = x
  elif op == '3':
    x = program[ptr]
    try:
      x = str(int(x)-1)
      if x == '-1': x=9
    except ValueError:
      x = ord(program[ptr])
      x = chr(x-1)
    program[ptr] = x
  elif op == '4':
    print(program[ptr],end='')
  elif op == '5':
    loc = len(program)+1
  elif op == '6':
    ptr = loc
  elif op == '7':
    program[ptr] = input('\n> ')[0]
  elif op == '8': 
    ptr -= 1
  elif op == '9':
    temp=ptr
    ptr=loc
    loc=temp
  loc += 1
  print('\n>',loc,ptr)
