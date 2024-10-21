import sys
from read import read_laptops
from write import write_laptops
from operations import display_laptops, purchased_laptops, sell_laptops

print("\n")
print("\n")
print("\n")
print("----------------------------------------------------------------- The Future Store--------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------Putalisadak, Kathmandu | Contact No: 9812985439--------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------------------------------The Future of computing is here-------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("\n")



def main():
    try:
        laptops = read_laptops("laptops.txt")
    except Exception as e:
        print(f"An error occurred while reading laptops from the text file: {e}")
        sys.exit(1)
   
    while True:
        print("What can we do for you:?")
        print("1. Display available laptops in the Store")
        print("2. Purchase laptops from manufacturer")
        print("3. Sell laptops to customers")
        print("4. Exit")
       
        choice = input("Enter your choice: ")
       
        if choice == '1':
            display_laptops(laptops)
           
        elif choice == '2':
            customer_name = input("Enter customer name: ")
            customer_address = input("Enter customer address: ")
            purchased_laptops(laptops, customer_name, customer_address)
           
            try:
                write_laptops("laptops.txt", laptops)
               
            except Exception as e:
                print(f"An error occurred while writing laptops to the text file: {e}")
                sys.exit(1)
               
        elif choice == '3':
            customer_name = str(input("Enter customer name: "))
            customer_address = input("Enter customer address: ")
            sell_laptops(laptops, customer_name, customer_address)
           
            try:
                write_laptops("laptops.txt", laptops)
               
            except Exception as e:
                print(f"An error occurred while writing laptops to the text file: {e}")
                sys.exit(1)
               
        elif choice == '4':
            print("Exiting...Thank you For doing Business with us")
            sys.exit()
           
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()