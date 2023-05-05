import copy

# cur_state = [True,False,True,True,True]
cur_state = [1, 0, 1, 1, 1]
tar_state = [1, 1, 1, 1, 1]
maximum_val = 1
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
        if (new_state[bit] > maximum_val):
            new_state[bit] = 0
    return new_state


def solved(state):
    solved_flag = True
    for idx, bit in enumerate(list(state)):
        # print("test",bit)
        if (bit != tar_state[idx]):
            solved_flag = False
    return solved_flag
    # return False1


def vld_st_chk(state):
  return state


hist_st = [copy.deepcopy(cur_state)]
step = []


def solve(state):
    fin_flag = False
    for idx, st in enumerate(state):
        print("start-idx-loop-begin:", idx,change_bit[idx])
        if not vld_st_chk(st):
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
                # print("-----start inserting", idx)
                # print(nxt_st)
                fin_flag = solve(nxt_st)
                if fin_flag:
                    return True
                elif step:
                    print(step.pop())
        print("start-idx-loop-fin  :", idx, state)
    print("&&&&&&&iter_return!", step, state)
    return fin_flag


print(cur_state)
solve(cur_state)
print(step)
