# Analysis:

The program calculates federal and state income tax for Colorado. Requirements:

- All taxpayers are charged a flat federal tax rate of 20%.
- All taxpayers are charged a flat state tax rate of 4.55%.
- Taxpayers are allowed a $10,000 standard deduction.
- For each dependent, a taxpayer is allowed an additional $3,000 deduction.
- Gross income must be entered to the nearest penny.


# Design:

We'll create a function calculate_taxes that takes in gross income and the number of dependents and returns the federal and state income taxes.


# Implementation:

taxform.py
```

# Testing:

We'll use doctests to validate the function against specific test cases:

'''
    Examples:
    >>> calculate_taxes(50000, 2)
    (6800.0, 1547.0)

    >>> calculate_taxes(75000, 3)
    (11200.0, 2548.0)

'''