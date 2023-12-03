class Mathematician:
    @staticmethod
    def square_nums(nums):
        """Takes a list of integers and returns the list of squares."""
        return [num ** 2 for num in nums]

    @staticmethod
    def remove_positives(nums):
        """Takes a list of integers and returns it without positive numbers."""
        return [num for num in nums if num <= 0]

    @staticmethod
    def filter_leaps(dates):
        """Takes a list of dates (integers) and removes those that are not 'leap years'."""
        return [year for year in dates if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]

m = Mathematician()


assert m.square_nums([7, 11, 5, 4]) == [49, 121, 25, 16]


assert m.remove_positives([26, -11, -8, 13, -90]) == [-11, -8, -90]


assert m.filter_leaps([2001, 1884, 1995, 2003, 2020]) == [1884, 2020]
