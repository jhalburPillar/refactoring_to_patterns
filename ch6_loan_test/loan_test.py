import unittest

import nose.tools as nt

from src.loan import Loan


class LoanTest(unittest.TestCase):
    def setUp(self):
        self.commitment = None
        self.outstanding = None
        self.risk_rating = None
        self.maturity = None
        self.expiry = None
        self.capital_strategy = None

    def test_loan_should_return_term_loan(self):
        loanUT = Loan(commitment="c", risk_rating="rr", maturity="m")
        nt.assert_equals(loanUT.capital_strategy, "TermLoan")
