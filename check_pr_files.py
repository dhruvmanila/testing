def test1(test: bool) -> bool:
	"""
	A test function
	>>> test1()
	False
	"""
	return False

def test2(test: int) -> None:
	"""
	A test function
	>>> test2
	None
	"""
	return None

def test3(test: int) -> None:
	"""
	>>> test3(1, 1, 1)
	"""
	return None


class TClass:
	def __init__(self, test: str) -> None:
		self.test = test

	def add(self, num1: int, num2: int) -> int:
		"""
		Add two numbers
		>>> add(1, 1)
		2
		"""
		return a + b

if __name__ == '__main__':
	pass
