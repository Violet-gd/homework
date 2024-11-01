'''
Portfolio Task - Grade Analyser

In order to decide student's overall classification, the university needs to take an overall mean average of their grades across all modules.
The classifications and boundaries are as follows:
>= 70 : 1
>=60 : 2:1
>=50 : 2:2
>=40 : 3
<40 : F

Each student's data is stored in a row in a csv file (4 sample files have been provided).
Students can have between 1 - 12 modules, for example:
203982,73,42,55,83,,,,,,,, # 4 modules
203742,55,97,57,37,76,68,,,,,, # 6 modules
You should ensure that you consider the number of modules when calculating your mean.

Your code needs to:
- ask for the filename of the student file
- read in the data, and for each student calculate their average grade and classification
- write out this calculated data in the format:
     student_id,average_grade,classification
     The average grade should be given to 2 decimal places
     this can be acheived by using the following in an fstring: {variable_name:.2f}
- write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

Your output files must be structured exactly as described - output files for all the test files have been provided so you can compare and ensure they are identical.

Note:
Your code will only be tested on valid files in the format shown in the 4 example files in this folder - you do not need to validate any data.
'''
x=input("What you want to out")
with open(f"{x}","r") as f:
     grade=[i.strip().split(",") for i in f]
grade.pop(0)
res=[]
for i in grade:
     mean=0
     num_mod=0
     for j in i[1:]:
          if j:
               mean+=float(j)
               num_mod+=1
     mean=mean/num_mod
     if mean>=70.00:
          res.append([i[0],mean,"1"])
     elif mean>=60.00:
          res.append([i[0],mean,"2:1"])
     elif mean>=50.00:
          res.append([i[0],mean,"2:2"])
     elif mean>=40.00:
          res.append([i[0],mean,"3"])
     else:
          res.append([i[0],mean,"F"])
with open(f"{x}_out.csv","w")as f:
     for i in res:
          f.write(f"{i[0]},{i[1]:.2f},{i[2]}\n")