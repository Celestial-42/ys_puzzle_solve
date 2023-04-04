import copy

# cur_state = [True,False,True,True,True]
cur_state = [1, 0, 1, 1, 1]
change_bit = (
  [0, 2, 3],
  [1, 3, 4],
  [2, 0, 4],
  [3, 0, 1],
  [4, 1, 2]
)


def insert(k, state):
  new_state = copy.deepcopy(state)
  for bit in change_bit[k]:
    # new_state[bit] = not new_state[bit]
    new_state[bit] = new_state[bit] + 1
    if (new_state[bit] == 2):
      new_state[bit] = 0
  return new_state


def solved(state):
  solved_flag = True
  for bit in list(state):
    print("test",bit)
    if (bit != 1):
      solved_flag = False
  return solved_flag
    # return False1

hist_st = [copy.deepcopy(cur_state)]
step = []


def solve(state):
  fin_flag = False
  for idx, st in enumerate(state):
    print("looping-begin:", idx)
    if not st:
      nxt_st = insert(idx, state)
      print("nxt_st :", nxt_st)
      if nxt_st in hist_st:
        print("repeated!")
        print(state)
        continue
      elif solved(nxt_st):
        step.append(copy.deepcopy(idx))
        print("Solved!!!!!!!!!!!!!!!!!")
        return True
      else:
        step.append(copy.deepcopy(idx))
        hist_st.append(copy.deepcopy(state))
        print("-----start inserting", idx)
        print(nxt_st)
        fin_flag = solve(nxt_st)
        if fin_flag:
          return True
        elif step:
          print(step.pop())
    print("looping-fin  :", idx, state)
  print("&&&&&&&iter_return!", step, state)
  return fin_flag


solve(cur_state)
print(step)
