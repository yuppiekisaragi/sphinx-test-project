class TestClass():
    """
    Simple class containing various documented methods for Sphinx testing

    """

    def fib(self, sequence = [], steps=5):
        """
        Recursively return the Fibonacci sequence as a list, up to N steps.

        :param sequence: current Fibonacci sequence. 
        :type sequence: List[int] 
        :param steps: maximum length.
        :type steps: int
        :return: updated Fibonacci sequence
        :rtype: List[int]

        """
        if not sequence:
            #initialize w/ (0, 1)
            sequence = [0, 1]

        while (len(sequence)+1) <= steps:
            sequence.append(sequence[-2] + sequence[-1])
            self.fib(sequence=sequence, steps=steps)

        else:
            return sequence

