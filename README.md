# Tecnical test solution

## Case
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.

### Prerequisites
None

### Built with
Python 3.6.7

### Files description:

* **main.py** 
  Solution entry point, answer solution question.
* **bouncy.py**
  Contains classes to identify number class (increasing, decreasing, bouncy) and to calculate bouncy number proportion.
- **test.py**
  Test cases for bouncy.py classes.

## Author

* **Eder Ortega Cardona** - System Engineer