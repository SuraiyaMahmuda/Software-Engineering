from django.db import models

class Subtraction(models.Model):
    """
    Model representing a subtraction operation.

    Attributes:
        num_first (float): The first number in the subtraction operation.
        num_second (float): The second number to subtract from `num_first`.
    """

    num_first = models.FloatField()
    num_second = models.FloatField()

    def result(self):
        """
        Returns the result of subtracting `num_second` from `num_first`.

        Returns:
            float: The result of the subtraction.
        """
        return self.num_first - self.num_second
