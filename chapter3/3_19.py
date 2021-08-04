from itertools import permutations
# N : num of sequence

def add (p_x, p_y): return p_x + p_y

def subtract (p_x, p_y): return p_x - p_y
  
def multiply (p_x, p_y): return p_x * p_y

def devide (p_x, p_y): return p_x / p_y

def get_input_data ():
  return int(input()), input().split(), input().split()

def getOprList ( opr ):
  tmp_list = []
  for idx, op in enumerate(opr):
    tmp_list += [idx for i in range(int(op))]
  return list(permutations(tmp_list, len(tmp_list)))

def start ():
  num_of_seq, seq, operators = get_input_data()
  global result
  opr_lists = getOprList(operators)
  for idx, value in enumerate(seq):
    v = int(value)
    if(idx > 0):
      for i, opr_list in enumerate(opr_lists):
        print(opr_list)
        for j, opr in enumerate(list(opr_list)):
          print(opr)
          if(opr == 0): result = add(v, result)
          elif (opr == 1): result = subtract(v, result)
          elif (opr == 2): result = multiply(v, result)
          elif (opr == 3): result = devide(v, result)
        print(">>"+str(result))
    result = v
  print(result)


start()