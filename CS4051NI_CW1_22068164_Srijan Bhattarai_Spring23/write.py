
def write_laptops(filename, laptops):
    with open(filename, "w") as file:
        for name, details in laptops.items():
            brand = details["brand"]
            price = "${:.2f}".format(details["price"])
            quantity = details["quantity"]
            processor = details["processor"]
            graphic_card = details["graphic_card"]
            line = "{}, {}, {}, {}, {}, {}\n".format(name, brand, price, quantity, processor, graphic_card)
            file.write(line)
