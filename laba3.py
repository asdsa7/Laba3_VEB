import copy
class Matrix:

	def __init__(self, matrice):
		self.matrice = matrice

	@staticmethod
	def print(A): 
		for j in A:
			for i in j:
				print(i, end=" ")
			print()
		return ''

	@staticmethod
	def getminor(mas,k): 
		res=[]
		for r in mas[1:]:
			row=[]
			for j in range(len(r)):
				if j != k:
					row.append(r[j])
			res.append(row)
		return res

	@staticmethod
	def getdet(mas):
		n=len(mas)
		if n==2:
			return mas[0][0]*mas[1][1]-mas[0][1]*mas[1][0]
		det = 0
		sign = 1
		for i in range(n):
			det=det+sign*mas[0][i]*Matrix.getdet(Matrix.getminor(mas,i))
		sign=-sign
		return det  

	def __gt__(self, other): 
		return (Matrix.getdet(self.matrice) > Matrix.getdet(other.matrice))

	def __lt__(self, other):
		return (Matrix.getdet(self.matrice) < Matrix.getdet(other.matrice))

	def __eq__(self, other):
		return (Matrix.getdet(self.matrice) == Matrix.getdet(other.matrice))

	def __add__(self, other):
		A = copy.deepcopy(self.matrice)
		for i in range(len(A)):
			for i2 in range(len(other.matrice[i])):
				A[i][i2] = self.matrice[i][i2] + other.matrice[i][i2]
		return Matrix.print(A)

	def __mul__(self, other): 
		s = 0
		A = copy.deepcopy(self.matrice)
		for i in range(len(A)):
			for i2 in range(len(other.matrice[i])):
				for z in range(len(A[i2])):
					s = s + self.matrice[i][z] * other.matrice[z][i2]
					A[i][i2] = s
					s = 0
		return Matrix.print(A)

x1 = Matrix([[45,2],[1,8]])
x2 = Matrix([[8,19],[22,69]])
if x1 > x2:
	print('x1 > x2')

if x1 < x2:
	print('x1 < x2')

if x1 == x2:
	print('x1 == x2')

print()
print('Сумма: ')
print(x1 + x2)
print('Произведение: ')
print(x1 * x2)
