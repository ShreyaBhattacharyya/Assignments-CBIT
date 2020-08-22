#Algorithm: 
# Step 1: START GRADE-CALCULATION
# Step 2: INPUT ARRAY ‘SUBJECTS’ = [ S1, S2, S3, S4, S5]
# Step 3: CALCULATE SUM OF ARRAY ELEMENTS AS ‘TOTAL’ = SUM(SUBJECTS)
# Step 4: CALCULATE AVERAGE = TOTAL/5
# Step 5: IF AVERAGE>= 90
# PRINT ‘A+’
# ELSE IF AVERAGE<90 AND AVERAGE>=80
# PRINT ‘A’
# ELSE IF AVERAGE<80 AND AVERAGE>=70
# PRINT ‘B’
# ELSE IF AVERAGE<70 AND AVERAGE>=60
# PRINT ‘C’
# ELSE IF AVERAGE<60 AND AVERAGE>=50
# PRINT ‘D’
# ELSE
# PRINT ‘F’
# [END OF IF]
# Step 6: END GRADE-CALCULATION


#Code for Above Algorithm: 
Subjects= []
for i in range(0,5):
    n = eval(input("Enter marks in Subject:"))
    Subjects.append(n)
Total = sum(Subjects)
Average = Total/5
print("Grade = ", end = '')
if(Average>= 90):
    print('O')
elif(Average<90 and Average>=80):
    print('A')
elif(Average<80 and Average>=70):
    print('B')
elif(Average<70 and Average>=60):
    print('C')
elif(Average<60 and Average>=50):
    print('D')
else:
    print('F')
