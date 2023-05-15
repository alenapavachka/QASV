#1
student1 = float(input("Enter the grades of the first student: "))
student2 = float(input("Enter the grades of the second student: "))
student3 = float(input("Enter the grades of the third student: "))
student4 = float(input("Enter the grades of the forth studenrt: "))
student5 = float(input("Enter the grades of the ifth student: "))
print(f"The average class grade is {round((student1 + student2 + student3 + student4 + student5)/5, 1)}")


#2
athlete1 = float(input("Enter the results of the first athlete: "))
athlete2 = float(input("Enter the results of the second athlete: "))
athlete3 = float(input("Enter the results of the third athlete: "))
athlete4 = float(input("Enter the results of the forth athlete: "))
print(f"{min(athlete1, athlete2, athlete3, athlete4)} is the best result and {max(athlete1, athlete2, athlete3, athlete4)}  is the worst result ")