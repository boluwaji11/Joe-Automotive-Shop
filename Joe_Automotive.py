# This program computes auto repair cost

import Classes.CarClass
import Classes.CustomerClass
import Classes.ServiceQuoteClass


def main():
    # Welcome Header
    print("--- Welcome to Joe's Automotive Shop ---")
    print("-----------------------------------------")

    # Get the customer information from the user
    print("--Customer Information--")
    print("-------------")
    name = input("Please enter customer name: ")
    address = input("Please enter address: ")
    phone = input("Please enter phone number: ")
    customer = Classes.CustomerClass.Customer(name, address, phone)
    print()

    # Get the car information
    print("--Car Information--")
    print("-------------")
    make = input("Please enter the make of the car: ")
    model = input("Please enter the model: ")
    year = input("Please enter the year: ")
    car = Classes.CarClass.Car(make, model, year)
    print()

    # Calculate the cost of service
    print("--Service Charges--")
    print("-------------")
    pcharge = float(input("Please enter the estimated part charge: "))
    lcharge = float(input("Please enter the estimated labor charge: "))
    quote = Classes.ServiceQuoteClass.ServiceQuote(pcharge, lcharge)
    print()

    # Display the output
    # Header
    print("------------------------------------")
    print("Hello, ", customer.get_name(), "!", sep="")
    print(
        "To service your ",
        car.get_year(),
        " ",
        car.get_model(),
        " ",
        car.get_make(),
        ", see your bill below:",
        sep="",
    )
    print()

    # Charges
    print(
        "The Part Charge is: ", "\t$", format(quote.get_parts_charges(), ",.2f"), sep=""
    )
    print(
        "The Labor Charge is: ",
        "\t$",
        format(quote.get_labor_charges(), ",.2f"),
        sep="",
    )
    print(
        "The Sales Tax is: ",
        "\t$",
        format(quote.get_sales_tax_amount(), ",.2f"),
        sep="",
    )

    # Overall Service Charge
    print()
    print(
        customer.get_name(),
        ", the total service charge is: $",
        format(quote.get_total_charges(), ",.2f"),
        sep="",
    )
    print()
    print("Thank You!")


# Call the main function
main()