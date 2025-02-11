price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
    
else:
    down_payment = 0.2 * price
    
    print(f"down payment:{down_payment}")

has_good_income = True
has_good_credit = True
has_criminal_record = False

if has_good_income and has_good_credit:
    loan_amount = price - down_payment
    print(f"loan amount:{loan_amount}")
    print('eligible for loan amount')

if has_good_credit or has_good_credit:
    loan_amount = price - down_payment
    print(f"loan amount:{loan_amount}")
    print('eligible for loan amount')

if has_good_credit and not has_criminal_record:
    loan_amount = price - down_payment
    print(f"loan amount:{loan_amount}")
    print('eligible for loan amount') # type: ignore