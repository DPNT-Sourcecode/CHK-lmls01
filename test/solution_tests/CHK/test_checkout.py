from solutions.CHK import checkout_solution


class TestSum():
    def test_checkout(self):
        assert checkout_solution.checkout("AAABBCD") == 210

