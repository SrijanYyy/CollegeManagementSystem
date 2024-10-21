def read_laptops(filename):
    laptops = {}
    with open(filename, "r") as file:
        for line in file:
            fields = line.strip().split(", ")
            name, brand, price, quantity, processor, graphic_card = fields
            laptops[name] = {
                "brand": brand,
                "price": float(price.strip("$")),
                "quantity": int(quantity),
                "processor": processor,
                "graphic_card": graphic_card
            }
    return laptops
