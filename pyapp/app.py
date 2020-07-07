class Square: 
	def __init__(self, side): 
		self.side = side 

	def area(self): 
		return self.side**2

	def perimeter(self): 
		return 4 * self.side

	def __repr__(self): 
		s = str(self.area())
		return s 


if __name__ == '__main__': 
	# read input from the user 
	side = int(input('enter the side length to create a Square: ')) 
	
	# create a square with the provided side 
	square = Square(side) 

	# print the created square 
	print(square) 
