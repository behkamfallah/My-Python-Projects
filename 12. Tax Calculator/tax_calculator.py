import customtkinter as ctk


class TaxCalculator:
    def __init__(self):
        # Initialize our window
        self.window = ctk.CTk()
        self.window.title('Simple Tax Calculator')
        self.window.geometry('300x250')
        self.window.resizable(False, False)

        # Widget padding
        self.padding: dict = {'padx': 20, 'pady': 10}

        # Income label and entry
        self.income_label = ctk.CTkLabel(self.window, text='Income:')
        self.income_label.grid(row=0, column=0, **self.padding)
        self.income_entry = ctk.CTkEntry(self.window)
        self.income_entry.grid(row=0, column=1, **self.padding)

        # Tax Percent label and entry
        self.tax_rate_label = ctk.CTkLabel(self.window, text='Percent:')
        self.tax_rate_label.grid(row=1, column=0, **self.padding)
        self.tax_rate_entry = ctk.CTkEntry(self.window)
        self.tax_rate_entry.grid(row=1, column=1, **self.padding)

        #  Result Tax amount label and entry
        self.result_label = ctk.CTkLabel(self.window, text='Tax:')
        self.result_label.grid(row=2, column=0, **self.padding)
        self.result_entry = ctk.CTkEntry(self.window)
        self.result_entry.insert(0, '0')
        self.result_entry.grid(row=2, column=1, **self.padding)

        #  Remaining
        self.remaining_label = ctk.CTkLabel(self.window, text='Remaining:')
        self.remaining_label.grid(row=3, column=0, **self.padding)
        self.remaining_entry = ctk.CTkEntry(self.window)
        self.remaining_entry.insert(0, '0')
        self.remaining_entry.grid(row=3, column=1, **self.padding)

        # Calculate button
        self.calculate_button = ctk.CTkButton(self.window, text='Calculate', command=self.calculate_tax)
        self.calculate_button.grid(row=4, column=1, **self.padding)

    def update_result(self, text: str, text2):
        """Updates the result of the tax and remaining field."""

        self.result_entry.delete(0, ctk.END)
        self.result_entry.insert(0, text)
        self.remaining_entry.delete(0, ctk.END)
        self.remaining_entry.insert(0, text2)

    def calculate_tax(self):
        """Calculates the total tax and remaining based on the percent."""

        try:
            income: float = float(self.income_entry.get())
            tax_rate: float = float(self.tax_rate_entry.get())
            remaining_money: float = income * (100 - tax_rate) / 100
            self.update_result(f'€{income * (tax_rate / 100):,.2f}', f'€{remaining_money:,.2f}')
        except ValueError:
            self.update_result('Invalid input', 'Invalid input')

    def run(self):
        """Runs the tkinter app."""

        self.window.mainloop()


if __name__ == '__main__':
    tc = TaxCalculator()
    tc.run()
