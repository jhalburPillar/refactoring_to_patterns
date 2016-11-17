from src.capital_stategy_revolver import CapitalStrategyRevolver
from src.capital_strategy_rctl import CapitalStrategyRCTL
from src.capital_strategy_term_loan import CapitalStrategyTermLoan


class Loan():
    def __init__(self, capital_strategy=None, commitment=None, outstanding=None, risk_rating=None, maturity=None, expiry=None ):
        self.commitment = commitment
        self.outstanding = outstanding
        self.risk_rating = risk_rating
        self.maturity = maturity
        self.expiry = expiry
        self.capital_strategy = capital_strategy

    def Loan(self, commitment, risk_rating, maturity):
        self.commitment = commitment
        self.outstanding = None
        self.risk_rating = risk_rating
        self.maturity = maturity
        self.expiry = None
        self.capital_strategy = None
        return self.__loan()

    def Loan(self, commitment, risk_rating, maturity, expiry):
        self.commitment = commitment
        self.outstanding = None
        self.risk_rating = risk_rating
        self.maturity = maturity
        self.expiry = expiry
        self.capital_strategy = None
        return self.__loan()

    def Loan(self, commitment, outstanding, risk_rating, maturity, expiry):
        self.commitment = commitment
        self.outstanding = outstanding
        self.risk_rating = risk_rating
        self.maturity = maturity
        self.expiry = expiry
        self.capital_strategy = None
        return self.__loan()

    def Loan(self, capital_strategy, commitment, risk_rating, maturity, expiry):
        self.commitment = commitment
        self.outstanding = None
        self.risk_rating = risk_rating
        self.maturity = maturity
        self.expiry = expiry
        self.capital_strategy = capital_strategy
        return self.__loan()


    def __loan(self):
        if self.capital_strategy is None:
            if self.expiry is None:
                self.capital_strategy = CapitalStrategyTermLoan()
            elif self.maturity is None:
                self.capital_strategy = CapitalStrategyRevolver()
            else:
                self.capital_strategy = CapitalStrategyRCTL()