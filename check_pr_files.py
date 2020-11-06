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
	>>> test3(1, 1, 1)
	"""
	return None

class TClass:
	def __init__(self, test):
		self.test = test

	def add(self, a: int, b) -> int:
		"""
		Add two numbers
		"""
		return a + b

if __name__ == '__main__':
	pass
