# sudoku

Count = 0
TryCount = 0

N = 81

Puzzle = [
	5,0,2,1,7,8,0,0,0,
	3,9,0,0,0,0,8,1,7,
	0,1,0,0,0,3,2,6,5,
	0,8,0,9,1,6,5,0,0,
	2,5,6,0,0,4,3,0,1,
	9,0,1,3,2,0,0,0,8,
	6,0,9,0,0,7,0,5,0,
	7,0,5,0,0,0,9,8,3,
	0,0,0,0,0,0,7,0,6,
]

Row = [
	[ 1,  2,  3,  4,  5,  6,  7,  8,  9],
	[10, 11, 12, 13, 14, 15, 16, 17, 18],
	[19, 20, 21, 22, 23, 24, 25, 26, 27],
	[28, 29, 30, 31, 32, 33, 34, 35, 36],
	[37, 38, 39, 40, 41, 42, 43, 44, 45],
	[46, 47, 48, 49, 50, 51, 52, 53, 54],
	[55, 56, 57, 58, 59, 60, 61, 62, 63],
	[64, 65, 66, 67, 68, 69, 70, 71, 72],
	[73, 74, 75, 76, 77, 78, 79, 80, 81], 
]

Col = [
	[1,	10,	19,	28,	37,	46,	55,	64,	73],
	[2,	11,	20,	29,	38,	47,	56,	65,	74],
	[3,	12,	21,	30,	39,	48,	57,	66,	75],
	[4,	13,	22,	31,	40,	49,	58,	67,	76],
	[5,	14,	23,	32,	41,	50,	59,	68,	77],
	[6,	15,	24,	33,	42,	51,	60,	69,	78],
	[7,	16,	25,	34,	43,	52,	61,	70,	79],
	[8,	17,	26,	35,	44,	53,	62,	71,	80],
	[9,	18,	27,	36,	45,	54,	63,	72,	81],
]

Block = [
	[1, 2, 3, 10, 11, 12, 19, 20, 21],
	[4, 5, 6, 13, 14, 15, 22, 23, 24],
	[7, 8, 9, 16, 17, 18, 25, 26, 27],
	[28, 29, 30, 37, 38, 39, 46, 47, 48],
	[31, 32, 33, 40, 41, 42, 49, 50, 51],
	[34, 35, 36, 43, 44, 45, 52, 53, 54],
	[55, 56, 57, 64, 65, 66, 73, 74, 75],
	[58, 59, 60, 67, 68, 69, 76, 77, 78],
	[61, 62, 63, 70, 71, 72, 79, 80, 81],
]


def isNumberOK(a, n, c):
	global TryCount
	TryCount = TryCount + 1
	# print(f"{TryCount} {n}=>{c}: {a}")

	if Puzzle[n-1]>0 :
		if Puzzle[n-1]==c :
			return True
		return False

	if isGroupOK(a, n, c, Block) and isGroupOK(a, n, c, Row) and isGroupOK(a, n, c, Col) :
		return True

	return False


def isGroupOK(a, n, c, t):
	for i in range(0,9) :
		for j in range(0,9) :

			# find the check numbers
			if(t[i][j]==n) :
				for k in range(0,9) :
					if Puzzle[t[i][k]-1]==c :
						return False

				for k in range(0,9) :
					if t[i][k]<n and a[t[i][k]-1]==c :
						return False

	return True


def printSolution(a):
	for i in range(0, len(a)+1):
		if i%27 == 0:
			print("+-------+-------+-------+", i)
		if i%9 == 0 and i < len(a)-8:
			print("|", a[i], a[i+1], a[i+2], "|", a[i+3], a[i+4], a[i+5], "|", a[i+6], a[i+7], a[i+8], "|")


def addNumber(a, n):
	global Count

	# print(f"{TryCount} : {a}")

	if n > N :
		printSolution(a)
		Count = Count+1
	else:
		for c in range(1, 10) :
			# print(f"--> {n} -- {c}")
			if isNumberOK(a, n, c) :
				a = a[0 : n-1]
				a.append(c)
				addNumber(a, n+1)


if __name__ == '__main__':
	printSolution(Puzzle)
	addNumber([], 1)
	print("Answer:", Count, "Try:", TryCount)

	print(range(1, 10), list(range(1, 10)))