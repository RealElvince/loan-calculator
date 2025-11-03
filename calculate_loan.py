class LoanCalculator:
    def __init__(self,principal,interest_rate,years):
        self.principal = principal
        self.interest_rate = interest_rate
        self.years = years
    
    def total_interest(self):
        interest = self.principal*(self.interest_rate/100)*self.years
        return interest
    
    def total_amount(self):
        amount_repaid = self.principal + self.total_interest()
        return amount_repaid
    
    def monthly_installment(self):
        months = self.years*12
        monthly_installment = self.principal/months
        return monthly_installment

    
    

loan = LoanCalculator(principal=2_000_000,interest_rate=10,years=5)
loan = LoanCalculator(principal=50000,interest_rate=5,years=1)
loan = LoanCalculator(principal=20_000_000,interest_rate=18.75,years=15)

print("\n --- Loan Details ---")
print(f"Amount to be repaid after {loan.years} year(s) : {loan.total_amount():.2f}")
print(f"Total interest:{loan.total_interest():.2f}")
print(f"Monthly installment:{loan.monthly_installment():.2f}")
