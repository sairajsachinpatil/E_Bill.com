from datetime import datetime

print("Welcome to E_Bill.com")
print("_" * 50)
print("Your Shop Information and Registration:")

# Shop Name
while True:
    shop_name = input("What is your shop name? ").title()
    if shop_name == "":
        print("❌ Shop name can't be empty. Please enter again.")
    else:
        break

# Shop Address
while True:
    address = input(f"Enter {shop_name} shop address: ").strip()
    if address == "":
        print("❌ Address can't be empty. Please enter again.")
    else:
        break

# Contact Number
while True:
    contact_number = input(f"Enter {shop_name} shop contact number: ").strip()
    if contact_number == "":
        print("❌ Contact number can't be empty. Please enter again.")
    else:
        break

# GSTIN Handling
has_gstin = input("Does your shop have a GSTIN number? (yes/no): ").strip().lower()
if has_gstin == "yes":
    while True:
        GSTIN = input("Enter GSTIN number: ").strip()
        if GSTIN == "":
            print("❌ GSTIN can't be empty. Please enter again.")
        elif len(GSTIN) != 15:
            print("❌ GSTIN must be 15 characters. Please enter a valid one.")
        else:
            break
else:
    GSTIN = "N/A"

# Display Shop Info Once
print("\n✅ THANK YOU FOR SHARING INFORMATION")
print("_" * 50)
print("🧾 Shop Summary:")
print(f"Shop Name      : {shop_name}")
print(f"Shop Address   : {address}")
print(f"Contact Number : {contact_number}")
print(f"GSTIN Number   : {GSTIN}")
print("_" * 50)

# Start Billing Loop
bill_no = 1

while True:
    print("\n🧑‍💼 CUSTOMER DETAILS")
    while True:
        C_Name = input("Customer Name: ").strip().title()
        if C_Name == "":
            print("❌ Customer Name can't be empty. Please enter again.")
        else:
            break

    while True:
        C_MobNum = input("Mobile Number: ").strip()
        if not C_MobNum.isdigit() or len(C_MobNum) != 10:
            print("❌ Enter a valid 10-digit mobile number.")
        else:
            break

    C_Address = input("Customer address (optional, press Enter to skip): ")

    print("_" * 50)
    print("🛒 Product Details Entry")

    items = []
    sr_no = 1

    # Item Entry Loop
    while True:
        item_name = input(f"Enter name of item {sr_no}: ").strip()
        if item_name == "":
            print("❌ Item name can't be empty.")
            continue

        quantity = input("Enter quantity: ").strip()
        if not quantity.isdigit():
            print("⚠️ Quantity must be a number. Try again.")
            continue
        quantity = int(quantity)

        rate = input("Enter rate per unit (₹): ").strip()
        if not rate.isdigit():
            print("⚠️ Rate must be a number. Try again.")
            continue
        rate = int(rate)

        total_price = quantity * rate

        # Add to items list
        items.append([sr_no, item_name, quantity, rate, total_price])
        sr_no += 1

        more = input("Add another item? (yes/no): ").strip().lower()
        if more != "yes":
            break

    # Print Final Bill
    bill_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

    print("\n🧾 FINAL BILL")
    print("=" * 60)
    print(f"{shop_name.upper()}".ljust(45) + f"Bill No: {bill_no}")
    print(f"📍 {address}")
    print(f"📞 {contact_number}")
    if GSTIN != "N/A":
        print(f"🧾 GSTIN: {GSTIN}")
    print(f"🕒 Date & Time: {bill_time}")
    print("=" * 60)

    # Customer Info
    print(f"Customer Name  : {C_Name}")
    print(f"Mobile Number  : {C_MobNum}")
    if C_Address:
        print(f"Address        : {C_Address}")
    print("=" * 60)

    # Product Table Header
    print(f"{'Sr.':<4} {'Item Name':<20} {'Qty':<5} {'Rate':<10} {'Total':<10}")
    print("-" * 60)

    # Product Rows
    grand_total = 0
    for item in items:
        print(f"{item[0]:<4} {item[1]:<20} {item[2]:<5} ₹{item[3]:<9} ₹{item[4]:<10}")
        grand_total += item[4]

    # Total
    print("-" * 60)
    print(f"{'':<4} {'':<20} {'':<5} {'Grand Total':<10} ₹{grand_total}")
    print("=" * 60)
    print("🎉 Thank you for shopping with us! 🎉")
    print("=" * 60)

    # Ask if user wants to continue billing
    next_customer = input("\n➕ Bill next customer? (yes/no): ").strip().lower()
    if next_customer != "yes":
        print("\n🔚 Billing session ended.")
        break

    bill_no += 1  # Increment bill number for the next customer
