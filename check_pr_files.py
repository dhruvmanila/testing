def bar(a):
	"""
	A test function
	"""
	return False


def foo(e: int) -> None:
	"""
	>>> foo(1)
	"""
	return None


class Spam:
	"""
	>>> Spam()
	"""
	def __init__(self, test: str) -> None:
		self.test = test

	def add(self, a: int, b: int) -> int:
		"""
		Add two numbers
		"""
		return a + b


def baz():
	pass


if __name__ == '__main__':
	pass
