def test1(abc: int) -> bool:
	"""
	A test function
	>>> test1(1)
	False
	"""
	return False


def test3(esdf: int) -> None:
	"""
	>>> test3(1, 1, 1)
	None
	"""
	return None


class TClass:
	def __init__(self, test: str):
		self.test = test

	def add(self, a, b):
		"""
		Add two numbers
		>>> add(1, 1)
		2
		"""
		return a + b
