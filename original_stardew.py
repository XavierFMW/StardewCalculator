import math
#       crop, brew, price
crops = [True, False]
beer = [False, True, 200]
coffee = [False, True, 150]
tea = [False, True, 100]
juice = [True, True]
mead = [False, True, 200]
ale = [False, True, 300]
wine = [True, True]

def StardewProfits():
    def CropCalculator():
        if crop_till == "No":
            crop_harv = math.floor((((28*crop_seas2) - crop_days2)/(crop_days2 - 1)) + 1)
            crop_profit = (crop_harv * crop_pric2 * crop_numb2) - (crop_numb2 * crop_seed2 * crop_harv)
        else:
            crop_harv = math.floor((((28 * crop_seas2) - crop_days2)/crop_regr2) + 1)
            crop_profit = (crop_harv * crop_pric2 * crop_numb2) - (crop_numb2 * crop_seed2)
        print(crop_harv)
        if crop_till == "No":
            if crop_seas == "4":
                print("\nIf you plant " + crop_numb + " of this crop on the 1st of the month in the greenhouse, and continue planting it every harvest for " + crop_seas + " months, and sell them all as basic quality, you will make " + str(crop_profit) + "g profit after 1 year.")
            else:
                print("\nIf you plant " + crop_numb + " of this crop on the 1st of the month, and continue planting it every harvest for " + crop_seas + " months, and sell them all as basic quality, you will make " + str(crop_profit) + "g profit after 1 year.")
        elif crop_till == "Yes":
            if crop_seas == "4":
                print("\nIf you plant " + crop_numb + " of this crop on the 1st of the month in the greenhouse, and continue harvesting it for " + crop_seas + " months, and sell them all as basic quality, you will make " + str(crop_profit) + "g profit after 1 year.")
            else:
                print("\nIf you plant " + crop_numb + " of this crop on the 1st of the month, and continue harvesting it for " + crop_seas + " months, and sell them all as basic quality, you will make " + str(crop_profit) + "g profit after 1 year.")
    def BeerCalculator():
        crop_harv = math.floor((((28 * crop_seas2) - 5) / 4) + 1)
        crop_profit = (crop_harv * 200 * crop_numb2 * qual) - (crop_numb2 * crop_seed2 * crop_harv)
        if crop_seas == "4":
            print("\nIf you begin planting Wheat on the 1st of Summer in the greenhouse, and continue planting Wheat every harvest for " + crop_seas + " months, you will sell " + str(crop_harv * crop_numb2) + " mug(s) of " + brew_qual + " quality Beer, you will make " + str(crop_profit) + "g profit after 1 year.")
        else:
            print("\nIf you begin planting Wheat on the 1st of Summer, and continue planting Wheat every harvest for " + crop_seas + " months, you will sell " + str(crop_harv * crop_numb2) + " mug(s) of " + brew_qual + " quality Beer, you will make " + str(crop_profit) + "g profit after 1 year.")
    def CoffCalculator():
        crop_harv = math.floor((((28 * crop_seas2) - 11) / 2) + 1)
        crop_profit = (math.floor(crop_harv/5) * 150 * crop_numb2) - (crop_numb2 * crop_seed2)
        if crop_seas == "4":
            print("\nIf you plant " + crop_numb + " coffee plant(s) on the 1st of Spring in the greenhouse, and continue harvesting Coffee Beans for " + crop_seas + " months, you will harvest " + str(crop_harv * crop_numb2) + " Coffee Beans, and sell " + str(math.floor((crop_harv * crop_numb2)/5)) + " cup(s) of Coffee, making " + str(crop_profit) + "g profit after 1 year.")
        else:
            print("\nIf you plant " + crop_numb + " coffee plant(s) on the 1st of Spring, and continue harvesting Coffee Beans for " + crop_seas + " month(s), you will harvest " + str(crop_harv * crop_numb2) + " Coffee Beans, and sell " + str(math.floor((crop_harv * crop_numb2)/5)) + " cup(s) of Coffee, making " + str(crop_profit) + "g profit after 1 year.")
    def TeasCalculator():
        crop_harv = math.floor(((28 * crop_seas2) - 22) + 1)
        crop_profit = (crop_harv * 100 * crop_numb2) - (crop_numb2 * crop_seed2)
        if crop_seas == "4":
            print("\nIf you plant " + crop_numb + " tea plant(s) on the 1st of Spring in the greenhouse, and continue harvesting Tea Leaves for " + crop_seas + " months, you will sell " + str(crop_harv * crop_numb2) + " cup(s) of Green Tea, making " + str(crop_profit) + "g profit after 1 year.")
        else:
            print("\nIf you plant " + crop_numb + " tea plant(s) on the 1st of Spring, and continue harvesting Tea Leaves for " + crop_seas + " month(s), you will sell " + str(crop_harv * crop_numb2) + " cup(s) of Green Tea, making " + str(crop_profit) + "g profit after 1 year.")
    def JuicCalculator():
        if crop_till == "No":
            crop_harv = math.floor((((28 * crop_seas2) - crop_days2)/(crop_days2 - 1)) + 1)
            crop_profit = (crop_harv * crop_pric2 * crop_numb2 * 2.25) - (crop_numb2 * crop_seed2 * crop_harv)
        else:
            crop_harv = math.floor((((28 * crop_seas2) - crop_days2)/crop_regr2) + 1)
            crop_profit = (crop_harv * crop_pric2 * crop_numb2 * 2.25) - (crop_numb2 * crop_seed2)
        if crop_till == "No":
            if crop_seas == "4":
                print("\nIf you plant " + crop_numb + " of this crop on the 1st of the month in the greenhouse, and continue planting it every harvest for " + crop_seas + " months, and sell them all as bottles of Juice, you will make " + str(crop_profit) + "g profit after 1 year.")
            else:
                print("\nIf you plant " + crop_numb + " of this crop on the 1st of the month, and continue planting it every harvest for " + crop_seas + " months, and sell them all as bottles of Juice, you will make " + str(crop_profit) + "g profit after 1 year.")
        elif crop_till == "Yes":
            if crop_seas == "4":
                print("\nIf you plant " + crop_numb + " of this crop on the 1st of the month in the greenhouse, and continue harvesting it for " + crop_seas + " months,, and sell them all as bottles of Juice, you will make " + str(crop_profit) + "g profit after 1 year.")
            else:
                print("\nIf you plant " + crop_numb + " of this crop on the 1st of the month, and continue harvesting it for " + crop_seas + " months, and sell them all as bottles of Juice, you will make " + str(crop_profit) + "g profit after 1 year.")
    def MeadCalculator():
        crop_harv = math.floor(((28 * crop_seas2) / 3.5))
        crop_profit = (crop_harv * 200 * crop_numb2 * qual)
        if crop_seas2 == 1:
            print("\nIf you place " + crop_numb + " beehive(s) on the 1st of Spring, harvesting honey as soon as it's ready, on average every 3-4 days, you will, on average, sell " + str(crop_harv * crop_numb2) + " bottle(s) of " + brew_qual + " quality Mead, and make " + str(crop_profit) + "g profit after 1 year.")
        elif crop_seas2 == 2:
            print("\nIf you place " + crop_numb + " beehive(s) on the 1st of Summer, harvesting honey as soon as it's ready, on average every 3-4 days, you will, on average, sell " + str(crop_harv * crop_numb2) + " bottle(s) of " + brew_qual + " quality Mead, and make " + str(crop_profit) + "g profit after 1 year.")
        elif crop_seas2 == 3:
            print("\nIf you place " + crop_numb + " beehive(s) on the 1st of Fall, harvesting honey as soon as it's ready, on average every 3-4 days, you will, on average, sell " + str(crop_harv * crop_numb2) + " bottle(s) of " + brew_qual + " quality Mead, and make " + str(crop_profit) + "g profit after 1 year.")
    def AlesCalculator():
        crop_harv = math.floor(((28 * crop_seas2) - 12) + 1)
        crop_profit = (crop_harv * 300 * crop_numb2 * qual) - (crop_numb2 * crop_seed2)
        if crop_seas == "4":
            print("\nIf you plant " + crop_numb + " Hops plant(s) on the 1st of Summer in the greenhouse, and sell " + str(crop_harv * crop_numb2) + " mug(s) of " + brew_qual + " Ale, you will make " + str(crop_profit) + "g after 1 year.")
        else:
            print("\nIf you plant " + crop_numb + " Hops plant(s) on the 1st of Summer, and sell " + str(crop_harv * crop_numb2) + " mug(s) of " + brew_qual + " Ale, you will make " + str(crop_profit) + "g after 1 year.")
    def WineCalculator():
        if crop_till == "No":
            crop_harv = math.floor((((28*crop_seas2) - crop_days2)/ (crop_days2 - 1)) + 1)
            crop_profit = (crop_harv * crop_pric2 * crop_numb2 * 3 * qual) - (crop_numb2 * crop_seed2 * crop_harv)
        else:
            crop_harv = math.floor((((28*crop_seas2) - crop_days2)/crop_regr2) + 1)
            crop_profit = (crop_harv * crop_pric2 * crop_numb2 * 3 * qual) - (crop_numb2 * crop_seed2)
        if crop_till == "No":
            if crop_seas == "4":
                print("\nIf you plant " + crop_numb + " of this crop on the 1st of the month in the greenhouse, and continue planting it every harvest for " + crop_seas + " months, and sell them all as bottles of " + brew_qual + " quality Wine, you will make " + str(crop_profit) + "g profit after 1 year.")
            else:
                print("\nIf you plant " + crop_numb + " of this crop on the 1st of the month, and continue planting it every harvest for " + crop_seas + " months, and sell them all as bottles of " + brew_qual + " quality Wine, you will make " + str(crop_profit) + "g profit after 1 year.")
        elif crop_till == "Yes":
            if crop_seas == "4":
                print("\nIf you plant " + crop_numb + " of this crop on the 1st of the month in the greenhouse, and continue harvesting it for " + crop_seas + " months, and sell them all as bottles of " + brew_qual + " quality Wine, you will make " + str(crop_profit) + "g profit after 1 year.")
        else:
            print("\nIf you plant " + crop_numb + " of this crop on the 1st of the month, and continue harvesting it for " + crop_seas + " months, and sell them all as bottles of " + brew_qual + " quality Wine, you will make " + str(crop_profit) + "g profit after 1 year.")

    input("Welcome to the Stardew Valley Crop Profit calculator! Press Enter to continue.")

    crop_brew = input("Will you be making a brewed product? (Yes or No, match capitalization): ")
    while crop_brew != "Yes" and crop_brew != "No":
        crop_brew = input("Will you be making a brewed product? (Yes or No, match capitalization): ")

    if crop_brew == "Yes":

        brew_type = input("What kind of product are you brewing? (Beer, Coffee, Tea, Juice, Mead, Pale Ale, or Wine): ")
        while brew_type != "Wine" and brew_type != "Pale Ale" and brew_type != "Mead" and brew_type != "Juice" and brew_type != "Tea" and brew_type != "Coffee" and brew_type != "Beer":
            brew_type = input("What kind of product are you brewing? (Beer, Coffee, Tea, Juice, Mead, Pale Ale, or Wine): ")

        if brew_type == "Wine" or brew_type == "Beer" or brew_type == "Pale Ale" or brew_type == "Mead":

            brew_qual = input("What quality is your product? Basic, Silver, Gold, Iridium, match capitalization (Note: Quality of brewed products is based off time in Cask equipment, time needed for this found on wiki): ")
            while brew_qual != "Basic" and brew_qual != "Silver" and brew_qual != "Gold" and brew_qual != "Iridium":
                brew_qual = input("What quality is your product? Basic, Silver, Gold, Iridium, match capitalization (Note: Quality of brewed products is based off time in Cask equipment, time needed for this found on wiki): ")

    if crop_brew == "Yes":
        if brew_type == "Wine" or brew_type == "Beer" or brew_type == "Pale Ale" or brew_type == "Mead":
            if brew_qual == "Basic":
                qual = 1
            elif brew_qual == "Silver":
                qual = 1.25
            elif brew_qual == "Gold":
                qual = 1.5
            elif brew_qual == "Iridium":
                qual = 2

    if crop_brew == "Yes":
        if brew_type == "Beer":
            product = beer
        elif brew_type == "Coffee":
            product = coffee
        elif brew_type == "Tea":
            product = tea
        elif brew_type == "Juice":
            product = juice
        elif brew_type == "Mead":
            product = mead
        elif brew_type == "Pale Ale":
            product = ale
        elif brew_type == "Wine":
            product = wine
    else:
        product = crops

    if brew_type == "Beer" or brew_type == "Coffee" or brew_type == "Tea" or brew_type == "Pale Ale":
        input("\nAs a note, the product you have chosen requires growing a specific crop, as such, some specifics of this crop will not be asked. Press Enter to Continue. \n")
    elif brew_type == "Mead":
        input("\nAs a note, the product you have chosen doesn't require growing crops, as such, some specifics of this product will not be asked. Press Enter to Continue. \n")

    if product[0]:
        crop_till = input("Does your crop regrow (Yes or No, match capitalization): ")
        while crop_till != "Yes" and crop_till != "No":
            crop_till = input("Does your crop regrow (Yes or No, match capitalization): ")

        crop_days = input("How long does your crop take to grow (in days, including day planted and harvested, initial growth if crop regrows): ")
        while not crop_days.isnumeric():
            crop_days = input("How long does your crop take to grow, (in days, including day planted and harvested), Please Enter a Valid Number: ")

        if crop_till == "Yes":
            crop_regr = input("How long does your crop take to regrow (in days, including harvest): ")
            while not crop_regr.isnumeric():
                crop_regr = input("How long does your crop take to regrow, (in days, including harvest), Please Enter a Valid Number: ")

        crop_seas = input("How many seasons does this crop grow in (4 in greenhouse): ")
        while crop_seas != "1" and crop_seas != "2" and crop_seas != "3" and crop_seas != "4":
            crop_seas = input("How many seasons does this crop grow in, must be at most 4 (4 in greenhouse), Please Enter a Valid Number: ")

    if product[0]:
        crop_pric = input("How much gold does one of your crops make (Basic quality, no perks): ")
        while not crop_pric.isnumeric():
            crop_pric = input("How much gold does one of your crops make, (Basic quality, no perks), Please Enter a Valid Number: ")
    else:
        crop_pric = product[2]

    if product == coffee:
        crop_numb = input("How many of this product are you making (Note, input number of coffee plants being grown, not cups of coffee to be made): ")
        while not crop_numb.isnumeric():
            crop_numb = input("How many of this product are you making (Note, input number of coffee plants being grown, not cups of coffee to be made), Please Enter a Valid Number: ")
    elif product == tea:
        crop_numb = input("How many of this product are you making (Note, input number of tea plants being grown, not cups of tea to be made): ")
        while not crop_numb.isnumeric():
            crop_numb = input("How many of this product are you making (Note, input number of tea plants being grown, not cups of tea to be made), Please Enter a Valid Number: ")
    elif product == mead:
        crop_numb = input("How many of this product are you making (Note, input number of Bee Hives placed, not bottles of mead to be made): ")
        while not crop_numb.isnumeric():
            crop_numb = input("How many of this product are you making (Note, input number of Bee Hives placed, not bottles of mead to be made), Please Enter a Valid Number: ")
    elif product == ale:
        crop_numb = input("How many of this product are you making (Note, input number of hops plants planted, not mugs of ale to be made): ")
        while not crop_numb.isnumeric():
            crop_numb = input("How many of this product are you making (Note, input number of hops plants planted, not mugs of ale to be made), Please Enter a Valid Number: ")
    else:
        crop_numb = input("How many of this product are you making: ")
        while not crop_numb.isnumeric():
            crop_numb = input("How many of this product are you making, Please Enter a Valid Number: ")

    if brew_type == "Beer" or brew_type == "Coffee" or brew_type == "Tea" or brew_type == "Pale Ale":
        green = input("Are you growing your products crop in the greenhouse? (Yes or No, match capitalization): ")
        while green != "Yes" and green != "No":
            green = input("Are you growing your products crop in the greenhouse? (Yes or No, match capitalization): ")
        if green == "Yes":
            crop_seas = "4"
        elif green == "No":
            if product == beer:
                crop_seas = input("For how many seasons are you growing this product? (Must be 2 or less): ")
                while crop_seas != "1" and crop_seas != "2":
                    crop_seas = input("For how many seasons are you growing this product? (Must be 2 or less): ")
            elif product == coffee:
                crop_seas = input("For how many seasons are you growing this product? (Must be 2 or less): ")
                while crop_seas != "1" and crop_seas != "2":
                    crop_seas = input("For how many seasons are you growing this product? (Must be 2 or less): ")
            elif product == tea:
                crop_seas = input("For how many seasons are you growing this product? (Must be 3 or less): ")
                while crop_seas != "1" and crop_seas != "2" and crop_seas != "3":
                    crop_seas = input("For how many seasons are you growing this product? (Must be 3 or less): ")
            elif product == ale:
                crop_seas = 1
    elif brew_type == "Mead":
        crop_seas = input("For how many seasons will you be producing Honey, must be 3 or less\n(Note: This Number represents the for how many Seasons you've let the Bee Hives produce Honey, given you begin on the 1st of the month, and immediately harvest the Honey): ")
        while crop_seas != "1" and crop_seas != "2" and crop_seas != "3":
            crop_seas = input("For how many seasons will you be producing Honey, must be 3 or less\n(Note: This Number represents the for how many Seasons you've let the Bee Hives produce Honey, given you begin on the 1st of the month, and immediately harvest the Honey) Please Enter a Valid Number: ")

    if product != mead:
        crop_seed = input("How much gold does one of your crops' seeds cost: ")
        while not crop_seed.isnumeric():
            crop_seed = input("How much gold does one of your crops' seeds cost, Please Enter a Valid Number: ")

    crop_numb2 = int(crop_numb)
    crop_seas2 = int(crop_seas)
    if brew_type != "Mead":
        crop_seed2 = int(crop_seed)
    if product[0]:
        crop_pric2 = int(crop_pric)
        crop_days2 = int(crop_days)
        if crop_till == "Yes":
            crop_regr2 = int(crop_regr)

    if brew_type == "Beer":
        BeerCalculator()
    elif product == coffee:
        CoffCalculator()
    elif product == tea:
        TeasCalculator()
    elif product == juice:
        JuicCalculator()
    elif brew_type == "Mead":
        MeadCalculator()
    elif product == ale:
        AlesCalculator()
    elif product == wine:
        WineCalculator()
    else:
        CropCalculator()

    clear = input("Type \"Clear\" to Repeat, or \"Exit\" to End the Program: ")


StardewProfits()