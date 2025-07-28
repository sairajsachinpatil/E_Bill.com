# E_Bill.com – Smart Billing System for Local Shops 🧾
E_Bill.com is a terminal-based billing system built in Python. It helps small shopkeepers manage shop registration, customer billing, and itemized receipts with ease — all in one clean, interactive script. Ideal for general stores, small retailers, and anyone who needs a quick offline billing solution.


# Features
🏪 Register and display shop details (name, address, contact, GSTIN)
👤 Capture customer information (name, mobile number, optional address)
🛒 Add multiple items with quantity and rate
🧾 Auto-calculation of total bill and grand total
🕒 Date/time-stamped invoice generation
🔁 Multiple customer billing loop
✅ Easy-to-read bill format in terminal


# Technologies Used
Python 3
datetime module (for timestamps)
CLI interface (no external libraries)


#Sample Output (Terminal)
🧾 FINAL BILL
============================================================
MY SHOP NAME                             Bill No: 1
📍 My Address
📞 9876543210
🕒 Date & Time: 28-07-2025 04:45 PM
============================================================
Customer Name  : Ravi Kumar
Mobile Number  : 9876543210
============================================================
Sr.  Item Name           Qty   Rate       Total     
------------------------------------------------------------
1    Notebook            2     ₹40        ₹80       
2    Pen                 5     ₹10        ₹50       
------------------------------------------------------------
                          Grand Total     ₹130
============================================================
🎉 Thank you for shopping with us! 🎉
============================================================


# Contributing
Feel free to fork the repo and submit pull requests to improve the project!


# License
This project is licensed under the MIT License.

