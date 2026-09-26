"""Easy Pandas examples using one small employee table."""

import numpy as np
import pandas as pd


employees = {
	"Name": ["Anu", "Ravi", "Kiran", "Sita", "Rahul"],
	"Age": [22, 25, 21, 24, 27],
	"City": ["Rajahmundry", "Hyderabad", "Chennai", "Rajahmundry", "Hyderabad"],
	"Salary": [25000, 45000, 30000, 35000, 55000],
	"Department": ["IT", "HR", "IT", "Finance", "IT"],
}

df = pd.DataFrame(employees)

print("All employees:")
print(df)

print("\nSalary above 30000:")
print(df[df["Salary"] > 30000])

print("\nIT employees earning above 30000:")
print(df[(df["Salary"] > 30000) & (df["Department"] == "IT")])

print("\nEmployees from Hyderabad or Chennai:")
print(df[df["City"].isin(["Hyderabad", "Chennai"])])

print("\nSalary from highest to lowest:")
print(df.sort_values("Salary", ascending=False))

df["Bonus"] = df["Salary"] * 0.10
df["TotalSalary"] = df["Salary"] + df["Bonus"]
df["Level"] = np.where(df["Salary"] >= 40000, "Senior", "Junior")

print("\nEmployees with bonus, total salary, and level:")
print(df)

print("\nAverage salary by department:")
print(df.groupby("Department")["Salary"].mean())

print("\nDepartment salary count, sum, average, lowest, and highest:")
print(df.groupby("Department")["Salary"].agg(["count", "sum", "mean", "min", "max"]))

print("\nAverage salary by city and department:")
print(df.groupby(["City", "Department"])["Salary"].mean())

print("\nEmployees in each department:")
print(df["Department"].value_counts())

print("\nSelect one row with loc:")
print(df.loc[0])

print("\nSelect names and salaries with loc:")
print(df.loc[:, ["Name", "Salary"]])

print("\nFirst three rows and first two columns with iloc:")
print(df.iloc[0:3, 0:2])

missing_data = pd.DataFrame({
	"Name": ["Anu", "Ravi", "Kiran", "Sita"],
	"Age": [22, None, 21, 24],
	"Salary": [25000, 45000, None, 35000],
})

print("\nMissing values in each column:")
print(missing_data.isnull().sum())

missing_data["Age"] = missing_data["Age"].fillna(missing_data["Age"].mean())
missing_data["Salary"] = missing_data["Salary"].fillna(0)
print("\nMissing values filled:")
print(missing_data)

print("\nRows with no missing values:")
print(missing_data.dropna())

print("\nRemove repeated names:")
print(pd.concat([df, df.iloc[[0]]]).drop_duplicates(subset=["Name"]))

print("\nRename columns:")
print(df.rename(columns={"Salary": "MonthlySalary", "Age": "EmployeeAge"}))

real_employees = pd.DataFrame({
	"Employee": ["A", "B", "C", "D", "E", "F"],
	"Department": ["IT", "HR", "IT", "Sales", "HR", "IT"],
	"Salary": [40000, 30000, 50000, 35000, 32000, 60000],
	"Experience": [2, 1, 4, 3, 2, 6],
})

print("\nReal-life example: salary above 40000:")
print(real_employees[real_employees["Salary"] > 40000])
print("Average salary:", real_employees["Salary"].mean())
print("Highest salary:", real_employees["Salary"].max())
print("Employee with highest salary:")
print(real_employees.loc[real_employees["Salary"].idxmax()])
print("Average salary by department:")
print(real_employees.groupby("Department")["Salary"].mean())
print("Employee count by department:")
print(real_employees["Department"].value_counts())

real_employees["AnnualSalary"] = real_employees["Salary"] * 12
print("\nAnnual salaries:")
print(real_employees)