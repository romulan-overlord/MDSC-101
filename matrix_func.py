#sum difference and product of two matrices

row1 = input('enter number of rows for first matrix: ')
col1 = input('enter number of columns for first matrix: ')
matrix1 = []

for i in range(int(row1)):
	temp = []
	for j in range(int(col1)):
		temp.append(input('enter element ({},{}) of the first matrix: '.format(i,j)))
	matrix1.append(temp)

print(matrix1)

row2 = input('enter number of rows for second matrix: ')
col2 = input('enter number of columns for second matrix: ')
matrix2 = []

for i in range(int(row2)):
	temp = []
	for j in range(int(col2)):
		temp.append(input('enter element ({},{}) of the second matrix: '.format(i,j)))
	matrix2.append(temp)

def matrix_add(mat1, dim1, mat2, dim2):
	if dim1[0] != dim2[0] or dim1[1] != dim2[1]:
		print('matrices are not compatible.')
		return []
	result = []
	for i in range(int(dim1[0])):
		temp = []
		for j in range(int(dim1[1])):
			temp.append(int(mat1[i][j]) + int(mat2[i][j]))
		result.append(temp)
	return result

def matrix_sub(mat1, dim1, mat2, dim2):
	if dim1[0] != dim2[0] or dim1[1] != dim2[1]:
		print('matrices are not compatible.')
		return []
	result = []
	for i in range(int(dim1[0])):
		temp = []
		for j in range(int(dim1[1])):
			temp.append(int(mat1[i][j]) - int(mat2[i][j]))
		result.append(temp)
	return result

def matrix_mul(mat1, dim1, mat2, dim2):
	if dim1[1] != dim2[0]:
		print('matrices are not compatible.')
		return []
	result = []
	for i in range(int(dim1[0])):
		temp1 = []
		for j in range(int(dim2[1])):
			temp2 = 0
			for k in range(int(dim1[1])):
				print('multiplying {} and {} at i = {}, j = {}, k = {}'.format(matrix1[i][k], matrix2[k][j] , i, j, k))
				temp2 += int(matrix1[i][k]) * int(matrix2[k][j])
			print('appending {} to row {}'.format(temp2, i))
			temp1.append(temp2)
		result.append(temp1)
	return result


print(matrix_mul(matrix1, (row1,col1), matrix2, (row2,col2)))






