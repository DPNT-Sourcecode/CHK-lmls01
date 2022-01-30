from solutions.CHK import checkout_solution


class TestCheckout2:
    def test_checkout(self):
        assert checkout_solution.checkout("AAAAABBCDEEFFF") == 365

    def test_checkout_2(self):
        assert checkout_solution.checkout("AAAAABBCDEEFF") == 365

    def test_checkout_3(self):
        assert checkout_solution.checkout("EE") == 80

    def test_checkout_4(self):
        assert checkout_solution.checkout("RRR") == 150

    def test_checkout_5(self):
        assert checkout_solution.checkout("NNN") == 120

    def test_invalid(self):
        assert checkout_solution.checkout("y") == -1
        assert checkout_solution.checkout("2") == -1




