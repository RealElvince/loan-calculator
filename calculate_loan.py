class LoanCalculator:
    def __init__(self,principal,interest_rate,years):
        self.principal = principal
        self.interest_rate = interest_rate
        self.years = years
    
    def total_interest(self):
        interest = self.principal*(self.interest_rate/100)*self.years
        return interest