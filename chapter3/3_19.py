from itertools import combinations, permutations
# N : num of sequence

def add (p_x, p_y): return p_x + p_y
def subtract (p_x, p_y): return p_x - p_y  
def multiply (p_x, p_y): return p_x * p_y
def devide (p_x, p_y): return p_x / p_y

def getInputData ():
  return int(input()), input().split(), input().split()

def getOprList ( opr ):
  tmp_list = []
  for idx, op in enumerate(opr):
    tmp_list += [idx for i in range(int(op))]
  return list(permutations(tmp_list, len(tmp_list)))

def run ( new_list : list, result ):
  for j, opr in enumerate(new_list):
    v = int(seq[j + 1])
    # print(result, v)
    if(opr == 0): result = add(result, v)
    elif (opr == 1): result = subtract(result, v)
    elif (opr == 2): result = multiply(result, v)
    elif (opr == 3): result = devide(result, v)
  return result

def start ():
  # global result
  container = []
  opr_lists = getOprList(operators)
  print("-----------------",opr_lists)  # opr_lists: ( + - - * +), ( - + - * +), ( + - - * +)
  for i, opr_list in enumerate(opr_lists):
    # print("-----------------",opr_list) # opr_list: ( + - - * +)
    result = int(seq[0])
    container.append(run(list(opr_list), result))
    # container.append(run(reversed(list(opr_list)), result))
  print(container)
  print(min(container))
  print(max(container))


num_of_seq, seq, operators = getInputData()
start()