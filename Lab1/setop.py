def set_not(set_, set_U):
	A = set_
	U = set_U
	return set_difference(U, A)

def set_union(set_A, set_B):
	A = set_A
	B = set_B
	R = []
	for i in A:
		R.append(i)
	for i in B:
		R.append(i)
	return set(R)

def set_intersection(set_A, set_B):
	A = set_A
	B = set_B
	R = []
	for i in A:
		for j in B:
			if i == j:
				R.append(i)
	return set(R)

def set_symmetric_difference(set_A, set_B):
	A = set_A
	B = set_B
	P = set_intersection(A, B)
	O = set_union(A, B)
	R = set_difference(O, P)
	return R

def set_difference(set_A, set_B):
	A = set_A
	B = set_B
	new_A = list(A).copy()
	G = set_intersection(A, B)
	for i in A:
		for j in G:
			if i == j:
				new_A.remove(i)

	return set(new_A)



