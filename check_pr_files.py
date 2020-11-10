def test1(a):
	"""
	A test function
	"""
	return False

def test2(d):
	"""
	A test function
	"""
	return None

def test3(e: int) -> None:
	"""
	>>> test3(1, 1, 1)
	"""
	return None


class TClass:
	def __init__(self, test) -> None:
		self.test = test

	def add(self, a: int, b: int) -> int:
		"""
		Add two numbers
		"""
		return a + b

if __name__ == '__main__':
	pass
