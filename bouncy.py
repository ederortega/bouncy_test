class IntegerClass:
    """ logic to identify a number's class (bouncy, increasing, decreasing) """

    def decompose(self, number):
        """ return an list with number's digits """
        digitlist = []
        # get modulus until number becomes cero
        while number > 0:
            remain = int(number) % 10
            number = int(number / 10)
            digitlist.append(remain)

        # digits in right order
        digitlist.reverse()
        return digitlist

    def isIncreasing(self, number):
        """ return True if number is increasing """
        digits = self.decompose(number)
        for index in range(len(digits) - 1):
            if digits[index] > digits[index + 1]:
                return False

        return True

    def isDecreasing(self, number):
        """ return True if number is decreasing """
        digits = self.decompose(number)
        for index in range(len(digits) - 1):
            if digits[index] < digits[index + 1]:
                return False

        return True

    def isBouncy(self, number):
        """ return True if number is bouncy """
        digits = self.decompose(number)
        # no bouncy numbers below one-hundred
        if len(digits) < 3:
            return False
        # neither increasing nor decreasing
        if self.isIncreasing(number) or self.isDecreasing(number):
            return False

        return True


class BouncyProportion:
    """ logic to get the bouncy proportion """

    def count(self, from_num, to):
        """ return the number of bouncies in a range """
        iclass = IntegerClass()
        count_bouncy = 0
        for num in range(from_num, to + 1):
            if iclass.isBouncy(num):
                count_bouncy += 1

        return count_bouncy

    def leastBouncy(self, percentage, maximun):
        """ Return the least bouncy according to percentage """
        count = 0
        num = 100
        while count / num < percentage / 100:
            num += 1
            count += self.count(num, num)

        return num
        """
        for num in range(100, maximun + 1):
            count += self.count(num, num)
            if count / num >= percentage / 100:
                return num

        return 0
        """
