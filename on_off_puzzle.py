# 原神解谜用
# 适合开关类型谜题，特别是无法复位，无法参照攻略时XD
# cur_state为初始条件
# change_bit为对应的改变位置

import copy
cur_state = [True,False,True,True,True]
change_bit = (
							[0,2,3],
							[1,3,4],
							[2,0,4],
							[3,0,1],
							[4,1,2]
							)
def insert(k,state):
	new_state = copy.deepcopy(state)
	for bit in change_bit[k]:
		new_state[bit] = not new_state[bit]
	return new_state

hist_st = [copy.deepcopy(cur_state)]
step = [] 
def solve(state):
	fin_flag = False
	for idx,st in enumerate(copy.deepcopy(state)):
		print("looping-begin:",idx)
		if not st:
			temp = insert(idx,state)
			nxt_st = copy.deepcopy(temp)
			print("nxt_st :",nxt_st)
			if nxt_st in hist_st:
				print("repeated!")
				print(state)
				# continue
			elif nxt_st == [True,True,True,True,True]:
				step.append(copy.deepcopy(idx))	
				print("Solved!!!!!!!!!!!!!!!!!")
				return True
			else:
				step.append(copy.deepcopy(idx))
				hist_st.append(copy.deepcopy(state))
				print("-----start inserting",idx)
				print(nxt_st)
				fin_flag = solve(nxt_st)
				if fin_flag:
					return True
				elif step:
					print(step.pop())
		print("looping-fin  :",idx,state)
	print("iter_return!",step,state)
	return fin_flag

solve(cur_state)
print(step)
