def test1(a: int):
	"""
	A test function
	>>> test1()
	False
	"""
	return False


def test2(efg: int) -> None:
	"""
	>>> test2(1, 1, 1)
	"""
	return None


class TClass:
	def __init__(self, test: str) -> None:
		self.test = test

	def add(self, ab: int, bd: int) -> int:
		"""
		Add two numbers
		>>> add(1, 1)
		2
		"""
		return a + b

if __name__ == '__main__':
	pass
