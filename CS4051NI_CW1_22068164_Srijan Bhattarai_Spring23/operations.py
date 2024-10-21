import datetime


def generate_bill_name(transaction_type):
  now = datetime.datetime.now()
  timestamp = now.strftime("%Y%m%d%H%M%S")
  return "{}_{}.txt".format(transaction_type, timestamp)


def calculate_vat(total_amount):
  vat_rate = 0.13
  return total_amount * vat_rate


def display_laptops(laptops):
  print(
    "+----------+--------------------+---------------+----------+----------+--------------------+--------------------+"
  )
  print("| {:<8} | {:<18} | {:<13} | {:<8} | {:<8} | {:<18} | {:<18} |".format(
    "Symbol", "Name", "Brand", "Price", "Quantity", "Processor",
    "Graphic Card"))
  print(
    "+----------+--------------------+---------------+----------+----------+--------------------+--------------------+"
  )
  symbol = 1
  for name, details in laptops.items():
    brand = details["brand"]
    price = "${:.2f}".format(details["price"])
    quantity = details["quantity"]
    processor = details["processor"]
    graphic_card = details["graphic_card"]
    print(
      "| {:<8} | {:<18} | {:<13} | {:<8} | {:<8} | {:<18} | {:<18} |".format(
        symbol, name, brand, price, quantity, processor, graphic_card))
    symbol += 1
  print(
    "+----------+--------------------+---------------+----------+----------+--------------------+--------------------+"
  )


def purchased_laptops(laptops, customer_name, customer_address):

  purchased_laptops = []
  Total_Net_Amount = 0
  Total_Vat = 0
  Total_Gross_Amount = 0
  shipment_cost = 100

  while True:
    symbol = input(
      "Enter the symbol number of the laptop you want to purchase or type 'e' to exit: "
    )
    if symbol == 'e':
      break
    try:
      symbol = int(symbol)
      name = list(laptops.keys())[symbol - 1]
    except (ValueError, IndexError):
      print("Invalid symbol number.")
      continue

    quantity = input("Enter the quantity to purchase the laptops: ")
    try:
        quantity=int(quantity)
        if quantity <=0:
           print("Invalid,Quantity must be greater than 0")
        else:
            break
    except ValueError :
        print("Invalid input. Please enter a valid integer.")
        continue



    price = laptops[name]["price"]
    shipment_cost = 100
    net_amount = price * quantity
    vat = calculate_vat(net_amount)
    gross_amount = net_amount + vat
    Total_Net_Amount += net_amount
    Total_Vat += vat
    Total_Gross_Amount += gross_amount + shipment_cost
    laptops[symbol]["quantity"] += quantity

    purchased_laptops.append({
      "customer name": customer_name,
      "customer address": customer_address,
      "name": name,
      "brand": laptops[name]["brand"],
      "quantity": quantity,
      "price": laptops[name]["price"]
    })

    buy_more = input("Do you want to buy more products? (y/n): ")
    if buy_more.lower() == 'n':
      break

  if purchased_laptops:
    print("Total amount (without VAT): ${:.2f}".format(Total_Net_Amount))
    print("VAT (13%): ${:.2f}".format(Total_Vat))
    print("Shipment Cost: ${:.2f}".format(shipment_cost))
    print("Total amount (with VAT): ${:.2f}".format(Total_Gross_Amount))

    # Generate bill name
  bill_name = generate_bill_name("purchase")

  # Write bill to file
  with open(bill_name, "w") as file:
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("----------------------------------------------------------------- The Future Store----------------------------------------------------------------------------------------- ")
    file.write("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("-------Putalisadak, Kathmandu | Contact No: 9812985439----------------------------------------------------------------------")
    file.write("-------------------------------------------------------------------------The Future of computing is here----------------")
    file.write("--------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\t \t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tPurchase Bill")
    file.write("\n")
    file.write("--------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Date: {}\n".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    file.write("\n")
    file.write("Customer Name: {}\n".format(customer_name))
    file.write("Shipping Address: {}\n".format(customer_address))

    file.write("\n")
    file.write("--------------------------------------------------------------------------------------------------------------" )
    file.write("\n")
    for laptop in purchased_laptops:
      file.write("{:<20} | {:<15} | {:<15} | {:<10}\n".format(
        laptop["name"], laptop["brand"], laptop["quantity"], laptop["price"]))

    file.write("\n")
    file.write("--------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("{:<20} | {:<15} | {:<15} | {:<10}\n".format( "", "", "Subtotal:", Total_Net_Amount))
    file.write("{:<20} | {:<15} | {:<15} | {:<10}\n".format("", "", "VAT (13%):", Total_Vat))
    file.write("{:<20} | {:<15} | {:<15} | {:<10}\n".format( "", "", "Shipment Cost:", shipment_cost))
    file.write("{:<20} | {:<15} | {:<15} | {:<10}\n".format( "", "", "Total:", Total_Gross_Amount))
    print("Bill generated at: {}".format(bill_name))


def sell_laptops(laptops, customer_name, customer_address):
  sell_laptops = []
  Total_Net_Amount = 0
  Total_Vat = 0
  Total_Gross_Amount = 0
  while True:
    symbol = input(
      "Enter the symbol number of the laptop you want to sell or type 'e' to exit: "
    )
    if symbol == 'e':
      break
    try:
      symbol = int(symbol)
      name = list(laptops.keys())[symbol - 1]
    except (ValueError, IndexError):
      print("Invalid symbol number.")
      continue

    quantity = input("Enter the quantity to purchase the laptops: ")
    try:
        quantity=int(quantity)
        if quantity <=0:
           print("Invalid,Quantity must be greater than 0")
        else:
            break
    except ValueError :
        print("Invalid input. Please enter a valid integer.")
        continue

    

    price = laptops[symbol]["price"]
    shipment_cost = 100
    net_amount = price * quantity
    vat = calculate_vat(net_amount)
    gross_amount = net_amount + vat
    Total_Net_Amount += net_amount
    Total_Vat += vat
    Total_Gross_Amount += gross_amount
    laptops[symbol]["quantity"] -= quantity

    sell_laptops.append({
      "customer name": customer_name,
      "customer address": customer_address,
      "name": name,
      "brand": laptops[name]["brand"],
      "quantity": quantity,
      "price": laptops[name]["price"]
    })

    buy_more = input("Do you want to sell more products? (y/n): ")
    if buy_more.lower() == 'n':
      break

  if sell_laptops:
    print("Total amount (without VAT):${:.2f}".format(Total_Net_Amount))
    print("VAT (13%): ${:.2f}".format(Total_Vat))
    print("Shipment Cost: ${:.2f}".format(shipment_cost))
    print("Total amount (with VAT): ${:.2f}".format(Total_Gross_Amount))

    # Generate bill name
  bill_name = generate_bill_name("sale")

  # Write bill to file
  with open(bill_name, "w") as file:
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write(
      "------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"
    )
    for laptop in sell_laptops:
      file.write("{:<20} | {:<15} | {:<15} | {:<10}\n".format(
        laptop["name"], laptop["brand"], laptop["quantity"], laptop["price"]))

  # Generate bill name
  bill_name = generate_bill_name("sale")

  # Write bill to file
  with open(bill_name, "w") as file:
    file.write("\n")
    file.write("\n")
    file.write("\n")
    file.write("----------------------------------------------------------------- The Future Store-------------------------------------------------------------- ")
    file.write("-----------------------------------------------------------------------------------------------------------------------------------------")
    file.write("-----------------Putalisadak, Kathmandu | Contact No: 9812985439----------------------------------------------------------------------")
    file.write("--------------------------------------------------------------------The Future of computing is here----------------")
    file.write("--------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("\t \t \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\Sale Bill")
    file.write("\n")
    file.write("--------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Date: {}\n".format(
      datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    file.write("\n")
    file.write("Customer Name: {}\n".format(customer_name))
    file.write("Shipping Address: {}\n".format(customer_address))

    file.write("\n")
    file.write("--------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    for laptop in purchased_laptops:
      file.write("{:<20} | {:<15} | {:<15} | {:<10}\n".format(
        laptop["name"], laptop["brand"], laptop["quantity"], laptop["price"]))

    file.write("\n")
    file.write(
      "--------------------------------------------------------------------------------------------------------------"
    )
    file.write("\n")
    file.write("{:<20} | {:<15} | {:<15} | {:<10}\n".format(
      "", "", "Subtotal:", Total_Net_Amount))
    file.write("{:<20} | {:<15} | {:<15} | {:<10}\n".format(
      "", "", "VAT (13%):", Total_Vat))
    file.write("{:<20} | {:<15} | {:<15} | {:<10}\n".format(
      "", "", "Shipment Cost:", shipment_cost))
    file.write("{:<20} | {:<15} | {:<15} | {:<10}\n".format(
      "", "", "Total:", Total_Gross_Amount))
    print("Bill generated at: {}".format(bill_name))
   