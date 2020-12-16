def foo(a):
    """
	  A test function
	  """
	  return False


def bar(e: int) -> None:
	  """
	  >>> bar(1, 1, 1)
	  """
	  return None


class Spam:
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
