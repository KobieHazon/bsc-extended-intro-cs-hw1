import os
Q3_INPUT_PATH = "dorian_gray.txt"
Q3_SOL_PATH = 'output_dorian_gray.txt'
Q3_STUDENT_SOL_PATH = 'output.txt'
Q3_SOL = open(Q3_SOL_PATH, 'r').read().replace("\r\n", "\n")
Q3_SOL_LINES = Q3_SOL.splitlines()

Q5_SOL_PATH = r'boom_sol.txt'
Q5_SOL_LINES = open(Q5_SOL_PATH, 'r').read().splitlines()


def check_q3():
	res = {}
	avg_word_len(Q3_INPUT_PATH)
	if not os.path.exists(Q3_STUDENT_SOL_PATH):
		res['file_doesnt_exist'] = 'T3_3'
		return res

	# check if file isn't closed yet
	for var_name in globals():
		if hasattr(globals()[var_name], 'closed') and os.path.split(globals()[var_name].name)[1].endswith('output.txt'):
			if not globals()[var_name].closed:
				res['file_isnt_closed'] = 'T3_2'
				globals()[var_name].close()

	student_sol = open(Q3_STUDENT_SOL_PATH, 'r').read().replace("\r\n", "\n")
	student_sol_lines = student_sol.splitlines()
	if abs(len(student_sol_lines) - len(Q3_SOL_LINES)) > 2:
		res['not enough lines'] = 'T3_1'
	for i, (a, b) in enumerate(zip(Q3_SOL_LINES, student_sol_lines)):
		if a.strip() != b.strip():
			# print("{}: {} {}".format(i, a, b))
			res['not matching sol'] = 'T3_1'
			break

	os.remove(Q3_STUDENT_SOL_PATH)

	return res


def check_q5():
	res = {}
	student_boom_string = k_boom(100, 6)
	student_boom_elements = student_boom_string.split()
	if len(student_boom_elements) < 100:
		res['not enough numbers'] = 'T5_1'

	for i, (a, b) in enumerate(zip(Q5_SOL_LINES, student_boom_elements)):
		if a.strip() != b.strip():
			# print(i, ":", a, b)
			if a.strip().isdigit():
				if not b.strip().isdigit():
					res['not matching sol'] = 'T5_1'
				else:
					res['not matching sol'] = 'T5_3'
			elif a.strip() == 'boom!':
				if b.strip().isdigit():
					res['not matching sol'] = 'T5_1'
				elif b.strip().lower().count('boom') != 1:
					res['not matching sol'] = 'T5_1'
				else:
					res['format incorrect'] = 'T5_2'
			elif a.strip() == 'boom-boom!':
				if b.strip().isdigit():
					res['not matching sol'] = 'T5_1'
				elif b.strip().lower().count('boom') != 2:
					res['not matching sol'] = 'T5_1'
				else:
					res['format incorrect'] = 'T5_2'

	return res


def check_q6():
	res = {}
	inputs = [(559933195, 2, 0), (6284062826648, 2, 13), (9632569636984596322, 3, 6), (889562836895888958888, 8, 4),
			  (123456789987654321, 1, 18)]
	for i, input in enumerate(inputs):
		try:
			if max_even_seq(*input[0:2]) != input[2]:
				res['Wrong output for ' + str(input[0:2])] = 'T6_' + str(i)
		except:
			res['Wrong output for ' + str(input[0:2])] = 'T6_' + str(i)
	return res

print("STUDENT TEST Q3:", end=' ')
print(check_q3())

print("\nSTUDENT TEST Q5:", end=' ')
print(check_q5())

print("\nSTUDENT TEST Q6:", end=' ')
print(check_q6())