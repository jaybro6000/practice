# Program01.py
# Jalen Brown

# Step 1. Input
Employee = int(input("Enter the employee's ID: "))
    
Hours_Worked = int(input("Enter the number of hours worked in a week: "))

Wage = float(input("Hourly pay rate: "))

Federal_rate = float(input("Enter the federal tax withholding rate (as a percentage): "))

State_rate = float(input("Enter the state tax withholding rate (as a percentage): "))

# Step 2. Processing
Gross_pay = Wage * Hours_Worked
Federal_withholding = Gross_pay * Federal_rate / 100
State_withholding = Gross_pay * State_rate / 100
Total_deductions = Federal_withholding + State_withholding 
Net_pay = Gross_pay - Total_deductions

# Step 3. Output
print("Summary")
print("Employee's ID: ", Employee)
print("Hours Worked: ", Hours_Worked)
print("Wage: $",format(Wage))
print("Gross pay: $",format(Gross_pay))
print("Deductions")
print(f"  Federal withholding ({Federal_rate}%): $ {Federal_withholding:.2f}")
print(f"  State withholding ({State_rate}%): $ {State_withholding:.2f}")
print("  Total deductions: $", format(Total_deductions))
print("Net pay: $", format(Net_pay))