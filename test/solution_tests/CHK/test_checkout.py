from solutions.CHK import checkout_solution


# class TestSum():
    # def test_checkout(self):
    #     assert checkout_solution.checkout("AAABBCD") == 210
    #
    # def test_invalid(self):
    #     assert checkout_solution.checkout("Y") == -1
    #     assert checkout_solution.checkout("2") == -1

class TestCheckout2():
    def test_checkout(self):
        assert checkout_solution.checkout("AAABBCDEE") == 275

    def test_invalid(self):
        assert checkout_solution.checkout("Y") == -1
        assert checkout_solution.checkout("2") == -1


