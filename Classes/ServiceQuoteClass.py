class ServiceQuote:
    def __init__(self, pcharge, lcharge):
        self.__parts_charge = pcharge
        self.__labor_charge = lcharge
        self.__sales_tax = 0.05
        self.__sales_tax_amount = 0
        self.__total_charges = 0

    def set_parts_charges(self, pcharge):
        self.__parts_charge = pcharge

    def set_labor_charges(self, lcharge):
        self.__labor_charge = lcharge

    def get_parts_charges(self):
        return self.__parts_charge

    def get_labor_charges(self):
        return self.__labor_charge

    def get_sales_tax_amount(self):
        self.__sales_tax_amount = (
            self.__labor_charge + self.__parts_charge
        ) * self.__sales_tax
        return self.__sales_tax_amount

    def get_total_charges(self):
        self.__total_charges = (
            self.__labor_charge + self.__parts_charge + self.__sales_tax_amount
        )
        return self.__total_charges
