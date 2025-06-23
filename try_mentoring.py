class Loan :
    def __init__ (_, borrower, loan_amount):
        _.borrower = borrower
        _.loan_amount = loan_amount
    

class HomeLoan (Loan):
    def __init__ (_,borrower, loan_amount, interest_rate, tenure_years):
        super().__init__(borrower, loan_amount)
        _.interest_rate = interest_rate
        _.tenure_years = tenure_years
    
    def Calculate_emi (_):
        pembilang = (_.loan_amount*((_.interest_rate/12)*100)*(1+(_.interest_rate/12)*100)**(_.tenure_years*12))
        penyebut = ((1+(_.interest_rate/12)*100)**(_.tenure_years*12) - 1)
        EMI = pembilang/penyebut
        new_dict = {"borrower": _.borrower, "Loan Amount": _.loan_amount, "Monthly EMI": EMI}
        return new_dict

user_1 = HomeLoan("Alice Johnson", 400000, 12, 3)
print(user_1.Calculate_emi())