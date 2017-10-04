from prac_08.taxi import Taxi


class SilverTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name='', fuel=0, fanciness=0.0):
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def get_fare(self):
        return super().get_fare() + self.flagfall

    def __str__(self):
        return '{} plus flagfall of ${}'.format(super().__str__(), self.flagfall)
