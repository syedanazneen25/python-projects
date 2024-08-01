print("Welcome!! Bill splitting along with Tip..")
total_bill = float(input("What is the total bill ?\n"))
tip = int(input("Enter the percentage for tip ?\n"))
person_count = int(input("Number of people for splitting the bill ?\n"))
tip_amount = (total_bill * tip)/100
bill_tip = total_bill + tip_amount
amount_per_person = round(bill_tip / person_count, 2)
print(f"Each person owes ${amount_per_person}")