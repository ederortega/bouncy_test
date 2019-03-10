from bouncy import BouncyProportion
"""
Eder Ortega Cardona
10/03/2018

Rules:

- increasing number: 134468
- decreasing number: 66420
- neither increasing nor decreasing: bouncy number (155349)
- no bouncy below one-hundred
- over half of the numbers below one-thousand (525) are bouncy
- least bouncy number reaches 50%: 538
- by the time we reach 21780 the proportion of bouncy numbers is equal to 90%

Requested solution:

Find the least number for which the proportion of bouncy numbers is exactly
99%.?
"""

b = BouncyProportion()
percentage = 99
print('Calculating for {}%...'.format(percentage))
print('The least bouncy number for {}% is {}'.format(
    percentage,
    b.leastBouncy(percentage, 1999000)))
