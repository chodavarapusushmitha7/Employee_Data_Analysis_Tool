# ============================================================
# Employee Data Analysis Tool
# Developed By : Chodavarapu Sushmitha
# Technologies : Python, Pandas, Matplotlib
# ============================================================

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Read the CSV file
# ------------------------------------------------------------
df = pd.read_csv("employee_data.csv")

# ------------------------------------------------------------
# Display Employee Data
# ------------------------------------------------------------
print("\n========== Employee Data ==========\n")
print(df)

# ------------------------------------------------------------
# Total Employees
# ------------------------------------------------------------
total_employees = len(df)
print("\nTotal Employees :", total_employees)

# ------------------------------------------------------------
# Average Salary
# ------------------------------------------------------------
average_salary = df["Salary"].mean()
print("Average Salary : ₹{:.2f}".format(average_salary))

# ------------------------------------------------------------
# Highest Salary Employee
# ------------------------------------------------------------
highest = df.loc[df["Salary"].idxmax()]

print("\n========== Highest Salary Employee ==========")
print("Name       :", highest["Name"])
print("Age        :", highest["Age"])
print("Department :", highest["Department"])
print("Salary     :", highest["Salary"])

# ------------------------------------------------------------
# Lowest Salary Employee
# ------------------------------------------------------------
lowest = df.loc[df["Salary"].idxmin()]

print("\n========== Lowest Salary Employee ==========")
print("Name       :", lowest["Name"])
print("Age        :", lowest["Age"])
print("Department :", lowest["Department"])
print("Salary     :", lowest["Salary"])

# ------------------------------------------------------------
# Department-wise Average Salary
# ------------------------------------------------------------
print("\n========== Department-wise Average Salary ==========\n")

department_salary = df.groupby("Department")["Salary"].mean()
print(department_salary)
# ------------------------------------------------------------
# Employee Search
# ------------------------------------------------------------

name = input("\nEnter Employee Name: ")

employee = df[df["Name"].str.lower() == name.lower()]

if not employee.empty:
    print("\n========== Employee Found ==========\n")
    print(employee)
else:
    print("\nEmployee Not Found")
# ------------------------------------------------------------
# Department Filter
# ------------------------------------------------------------

department = input("\nEnter Department Name: ")

filtered_data = df[df["Department"].str.lower() == department.lower()]

if not filtered_data.empty:
    print("\n========== Employees in", department.title(), "Department ==========\n")
    print(filtered_data)
else:
    print("\nDepartment Not Found")
# ------------------------------------------------------------
# Save Analysis Report
# ------------------------------------------------------------

df.to_csv("analysis_report.csv", index=False)

print("\nAnalysis report saved successfully!")
# ------------------------------------------------------------
# Bar Chart
# ------------------------------------------------------------
department_salary.plot(kind="bar")

plt.title("Department-wise Average Salary")
plt.xlabel("Department")
plt.ylabel("Average Salary")
plt.grid(axis="y")

plt.show()

# ------------------------------------------------------------
# Pie Chart
# ------------------------------------------------------------
department_count = df["Department"].value_counts()

department_count.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Employees in Each Department")
plt.ylabel("")

plt.show()

# ------------------------------------------------------------
# Line Chart
# ------------------------------------------------------------
plt.plot(
    df["Name"],
    df["Salary"],
    marker="o"
)

plt.title("Employee Salary Distribution")
plt.xlabel("Employee")
plt.ylabel("Salary")
plt.grid(True)

plt.show()

