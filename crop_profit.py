from tkinter import ttk
from tkinter import *
import math

# TODO ACTUALLY MAKE SURE THIS WORKS! Pretty much everything's here, but there's a ton of bugs

class CropGUI:

    def __init__(self):

        root = Tk()
        root.title("Crop Profit Calculator")
        self.root = root

        self.current_profit = 0
        self.running_profit = 0
        self.amount = 0

        # Text inputs

        text_panel = Frame(root, width=500, height=400)
        text_panel.grid(row=1, column=1)

        Label(text_panel, text="Amount: ").grid(row=1, column=1)
        num_input = Entry(text_panel, width=20)
        num_input.grid(row=1, column=2)
        self.num_input = num_input

        Label(text_panel, text="Sell price (per raw crop): ").grid(row=2, column=1)
        price_input = Entry(text_panel, width=20)
        price_input.grid(row=2, column=2)
        self.price_input = price_input

        Label(text_panel, text="Seed cost (per seed): ").grid(row=3, column=1)
        seed_input = Entry(text_panel, width=20)
        seed_input.grid(row=3, column=2)
        self.seed_input = seed_input

        Label(text_panel, text="Initial grow time (Including day planted/harvested): ").grid(row=4, column=1)
        grow_input = Entry(text_panel, width=20)
        grow_input.grid(row=4, column=2)
        self.grow_input = grow_input

        Label(text_panel, text="Regrowth time (trellis crops only, after harvest): ").grid(row=5, column=1)
        regrow_input = Entry(text_panel, width=20)
        regrow_input.grid(row=5, column=2)
        self.regrow_input = regrow_input

        Label(text_panel, text="# of growing seasons: ").grid(row=6, column=1)
        season_input = Entry(text_panel, width=20)
        season_input.grid(row=6, column=2)
        self.season_input = season_input

        
        ttk.Separator(root).grid(row=2, column=1, sticky="ew")
        # Boolean inputs

        check_panel = Frame(root, width=500, height=400)
        check_panel.grid(row=3, column=1)

        self.quality = DoubleVar()
        self.quality.set(1.0)

        Radiobutton(check_panel, text="Basic Quality", variable=self.quality, value=1.0).grid(row=1, column=1)
        Radiobutton(check_panel, text="Silver Quality", variable=self.quality, value=1.25).grid(row=2, column=1)
        Radiobutton(check_panel, text="Gold Quality", variable=self.quality, value=1.50).grid(row=3, column=1)
        Radiobutton(check_panel, text="Iridium Quality", variable=self.quality, value=2).grid(row=4, column=1)

        # Type int definitions
        # 
        # 1 = Raw Crop
        # 2 = Juice
        # 3 = Wine
        # 4 = Other

        self.type = DoubleVar()
        self.type.set(1)

        Radiobutton(check_panel, text="Raw Crop", variable=self.type, value=1).grid(row=1, column=2)
        Radiobutton(check_panel, text="Juice", variable=self.type, value=2).grid(row=2, column=2)
        Radiobutton(check_panel, text="Wine", variable=self.type, value=3).grid(row=3, column=2)
        Radiobutton(check_panel, text="Other", variable=self.type, value=4).grid(row=4, column=2)

        self.tiller = DoubleVar()
        self.tiller.set(1.0)
        Checkbutton(check_panel, text="Tiller perk", variable=self.tiller, onvalue=1.1, offvalue=1.0).grid(row=5, column=1)

        self.artisan = DoubleVar()
        self.artisan.set(1.0)
        Checkbutton(check_panel, text="Artisan perk", variable=self.artisan, onvalue=1.4, offvalue=1.0).grid(row=6, column=1)

        self.trellis = BooleanVar()
        Checkbutton(check_panel, text="Trellis crop (regrows)", variable=self.trellis, onvalue=True, offvalue=False).grid(row=5, column=2)


        ttk.Separator(root).grid(row=4, column=1, sticky="ew")
        # Button inputs

        button_panel = Frame(root, width=500, height=400)
        button_panel.grid(row=5, column=1)

        Button(button_panel, text="Number of crops produced & profit earned", width=35, command=self.growing_product).grid(row=1, column=1)
        Button(button_panel, text="Profit from pre-made products", width=30, command=self.pregrown_product).grid(row=1, column=2)

        Button(button_panel, text="Add current profit to running total", bg="#248f1e", fg="white", width=35, command=self.add_to_running).grid(row=2, column=1)
        Button(button_panel, text="Clear running total", bg="#ba1a1a", fg="white", width=30, command=self.clear_running).grid(row=2, column=2)
        
        ttk.Separator(root).grid(row=6, column=1, sticky="ew")
        # Outputs

        output_labels = Frame(root, height=50)
        output_labels.grid(row=7, column=1)
        self.outputs = output_labels

        Label(output_labels, text="Amount of sellable products: 0", font=("Arial", 12)).grid(row=1, column=1)
        Label(output_labels, text="Total profit earned: 0", font=("Arial", 12)).grid(row=1, column=2)
        Label(output_labels, text="Running total: 0", font=("Arial", 12)).grid(row=2, column=1)


    def update_output(self):

        self.outputs.destroy()

        output_labels = Frame(self.root, height=50)
        self.outputs = output_labels
        
        Label(output_labels, text=f"Amount of sellable products: {self.amount}", font=("Arial", 12)).grid(row=1, column=1)
        Label(output_labels, text=f"Total profit earned: {self.current_profit}", font=("Arial", 12)).grid(row=1, column=2)
        Label(output_labels, text=f"Running total: {self.running_profit}", font=("Arial", 12)).grid(row=2, column=1)

        output_labels.grid(row=7, column=1)

    def pregrown_product(self, given_amount=False):

        if not given_amount:
            self.amount = int(self.num_input.get())

        amount = self.amount

        self.current_profit = math.floor(amount * int(self.price_input.get()) * self.quality.get())

        if self.type.get() == 3:  # Wine
            self.current_profit = math.floor(self.current_profit * 3 * self.artisan.get())

        elif self.type.get() == 2:  # Juice
            self.current_profit = math.floor(self.current_profit * 2.25 * self.artisan.get())

        elif self.type.get() == 1:  # Crops

            seed_cost = self.seed_input.get()
            self.current_profit = math.floor((self.current_profit * self.tiller.get()) - (amount * seed_cost))

        else:  # Other
            self.current_profit = math.floor(self.current_profit * self.artisan.get())

        self.update_output()

    
    def growing_product(self):
        
        amount = int(self.num_input.get())
        price = int(self.price_input.get())
        seed_cost = int(self.seed_input.get())
        grow_time = int(self.grow_input.get())
        grow_seasons = int(self.season_input.get())
        trellis = self.trellis.get()

        if not trellis:  # Crops do not regrow

            harvests = math.floor((((28 * grow_seasons) - grow_time)/(grow_time - 1)) + 1)

            self.current_profit = math.floor(((harvests * price * amount) - (amount * seed_cost * harvests)) * self.tiller.get() * self.quality.get())
            self.amount = harvests * amount

        else:  # Crops regrow

            regrow_time = int(self.regrow_input.get())
            harvests = math.floor((((28 * grow_seasons) - grow_time)/regrow_time) + 1)

            self.current_profit = math.floor(((harvests * price * amount) - (amount * seed_cost)) * self.tiller.get() * self.quality.get())
            self.amount = harvests * amount

        self.update_output()
        

    def add_to_running(self):

        self.running_profit += self.current_profit
        self.update_output()


    def clear_running(self):

        self.running_profit = 0
        self.update_output()


if __name__ == "__main__":

    app = CropGUI()
    print(app.tiller.get())
    app.root.mainloop()
