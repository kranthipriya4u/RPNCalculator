# RPNCalculator
Command-line reverse polish notation (RPN) calculator

# Documentation
Used 'Operator' library For Math calculations.In Future if we want to add more operators we can just add to the list.Rest will handle by the code.

- 'evaluate' Function: Helps to split the Input Expression,find for token (operator)in the Expression, and Push the data to stack.
- 'apply' Function: Helps to perform operational calculation on the last 2 elements of stack and push the results back to stack.
- 'run' Function: Helps to run the program in loop untill it receives exit command.


# Binary Operators
- +: addition
- -: subtraction
- *: multiplication
- /: true division

# Usage
Simply run rpn_calculator.py. You can push numbers as you'd do in a RPN calculator, and stack them with operators.

# python rpn_calculator.py
---
    > 5 
    5
    > 8
    8
    > +
    13

---

    > 5 5 5 8 + + -
    -13.0
    > 13 +
    0.0

---

    > -3
    -3.0
    > -2
    -2.0
    > *
    6.0
    > 5
    5.0
    > +
    11.0

---

# Todo
-  Use Numpy-Array For better Performance.
-  Use Regex opearations while evaluating expressions.
