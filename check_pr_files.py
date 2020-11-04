class TestClass:
	classattr = 10
	def __init__(self, x, y):
		self.x = None
		self.y = None
	
	def add(self, x, y):
		return x + y
	
	def subtract(self, x, y):
		return x - y

def test1(a, b, c):
	"""
	A test function
	"""
	return False

def test2(d, e, f):
	"""
	A test function
	"""
	return None

def test3(a: int) -> None:
	"""
	>>> test3(1)
	"""
	return None

if __name__ == '__main__':
	pass
