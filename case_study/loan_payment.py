#!/usr/bin/env python3
# Program: loan_repayments.py

"""an example in a similar field that follows the same concepts of analysis, design, implementation, and testing:
a program that calculates loan repayments."""
def calculate_loan_repayment(loan_amount, interest_rate, duration_years):
    """
    Calculate monthly loan repayment and total payment.

    Args:
    - loan_amount (float): The amount of the loan.
    - interest_rate (float): Annual interest rate (in percentage).
    - duration_years (int): Loan duration in years.

    Returns:
    - Tuple: (monthly_repayment, total_payment)

    Examples:
    >>> calculate_loan_repayment(10000, 5, 2)
    (438.71, 10529.13)

    >>> calculate_loan_repayment(20000, 7, 5)
    (396.02, 23761.44)
    """
    
    # Convert annual interest rate to monthly rate
    monthly_interest_rate = interest_rate / 12 / 100

    # Calculate number of monthly payments
    num_payments = duration_years * 12

    # Calculate monthly repayment
    monthly_repayment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -num_payments))

    # Calculate total payment
    total_payment = monthly_repayment * num_payments

    return round(monthly_repayment, 2), round(total_payment, 2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # Input values from user
    loan_amount = float(input("Enter the loan amount: "))
    interest_rate = float(input("Enter the interest rate (in percentage): "))
    duration_years = int(input("Enter the loan duration in years: "))

    # Calculate loan repayments
    monthly_repayment, total_payment = calculate_loan_repayment(loan_amount, interest_rate, duration_years)

    # Display the monthly repayment and total payment
    print(f"The Monthly Repayment is ${monthly_repayment}")
    print(f"The Total Payment is ${total_payment}")
