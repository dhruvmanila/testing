def test1(a):
	"""
	A test function
	"""
	return False


def test3(e: int) -> None:
	"""
	>>> test3(1, 1, 1)
	"""
	return None


class TClass:
	def __init__(self, test: str) -> None:
		self.test = test

	def add(self, a: int, b: int) -> int:
		"""
		Add two numbers
		"""
		return a + b
