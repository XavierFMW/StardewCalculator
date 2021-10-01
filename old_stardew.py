import math

class soldProduct:

    def __init__(self, price=None, quality=None, amount=None, type=None, prof=1):

        self.price = price
        self.quality = quality
        self.type = type
        self.amount = amount
        self.prof = prof

        self.qualities = {"basic": 1, "silver": 1.25, "gold": 1.5, "iridium": 2}
        self.profs = {"tiller": 1.10, "artisan": 1.40, None: 1}

        self.brews = {

        "beer":   200, 
        "coffee": 150,
        "tea":    100,
        "mead":   200,
        "ale":    300,
        }


    def yield_price(self):

        if self.type == "juice":
            return self.price * self.amount * self.qualities[self.quality] * 2.25 * self.prof

        elif self.type == "wine":
            return self.price * self.amount * self.qualities[self.quality] * 3 * self.prof

        else:
            return self.price * self.amount * self.qualities[self.quality] * self.prof


    def yield_setup(self):

        self.amount = int(input("First, how much of this product are you selling? (Please enter a whole number): "))

        self.quality = input("What quality of item are you selling? (Basic, silver, gold, iridium): ").lower()
        while self.quality not in self.qualities:
            self.quality = input("What quality of item are you selling? (Basic, silver, gold, iridium): ").lower()

        brew_bool = input("Is your product made in a keg, such as beer, wine, or juice? (y/n): ").lower()
        while brew_bool != "y" and brew_bool != "n":
            brew_bool = input("Is your product made in a keg, such as beer, wine, or juice? (y/n): ").lower()


        if brew_bool == "y":

            prof_bool = input("Do you posses the 'Artisan' profession? (y/n): ").lower()
            while prof_bool != "y" and brew_bool != "n":
                prof_bool = input("Do you posses the 'Artisan' profession? (y/n): ").lower()

            if prof_bool == "y":
                self.prof = self.profs["artisan"]

            self.type = input("What kind of brewed product are you making?: ").lower()
            while self.type not in self.brews:
                self.type = input("What kind of brewed product are you making?: ").lower()

            if self.type == "juice" or self.type == "wine":
                self.price = int(input("What is the base crop for your wine/juice? (input the price of a single, basic quality crop): "))

            else:
                self.price = self.brews[self.type]

        else:

            prof_bool = input("Do you posses the 'Tiller' profession? (y/n): ").lower()
            while prof_bool != "y" and brew_bool != "n":
                prof_bool = input("Do you posses the 'Tiller' profession? (y/n): ").lower()

            if prof_bool == "y":
                self.prof = self.profs["tiller"]

            self.price = int(input("What is the price of your crop? (input the price of a single, basic quality crop): "))
            self.type = "crop"

        print(self.yieldPrice())


    def grow_calculator(self):

        crop_num = int(input("First, how many of this crop are you growing? (please enter a whole number): "))
        crop_pric = int(input("How much does one basic quality version of your crop sell for? (please enter a whole number): "))
        crop_seas = int(input("For how many months will you be growing this crop? (please enter a whole number): "))
        crop_seed = int(input("How much does one seed for this crop cost? (please enter a whole number): "))

        till_bool = input("Do you have the 'tiller' profession? (y/n): ")
        while till_bool != "y" and till_bool != "n":
            till_bool = input("Do you have the 'tiller' profession? (y/n): ")

        if till_bool == "y":
            boost = 1.10

        else:
            boost = 1

        crop_trel = input("Is your crop a trellis crop (regrows after harvest?) (y/n): ")
        while crop_trel != "y" and crop_trel != "n":
            crop_trel = input("Is yout crop a trellis crop (regrows after harvest?) (y/n): ")


        if crop_trel == "n":

            crop_days = int(input("How many days does it take for this crop to grow to harvest? (include first day planted, please enter a whole number): "))

            crop_harv = math.floor((((28*crop_seas) - crop_days)/(crop_days - 1)) + 1)
            crop_profit = ((crop_harv * crop_pric * crop_num) - (crop_num * crop_seed * (crop_harv + 1))) * boost

            return crop_profit

        else:

            crop_days = int(input("How many days does it take for this crop to initially grow to harvest? (include first day planted, please enter a whole number): "))
            crop_regr = int(input("How many days does it take for this crop to regrow? (include day harvested, please enter a whole number): "))

            crop_harv = math.floor((((28 * crop_seas) - crop_days)/crop_regr) + 1)
            crop_profit = ((crop_harv * crop_pric * crop_num) - (crop_num * crop_seed)) * boost

            return crop_profit


