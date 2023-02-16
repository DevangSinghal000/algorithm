r = int(input("Enter the rows: "))
c = int(input("Enter the columns: "))

print("Enter Matrix 1:")
m1 = [[int(input()) for i in range(c)] for i in range(r)]
print("Matrix 1 is: ")
for n in m1:
   print(n)
 
print("Enter Matrix 2:")
m2 = [[int(input()) for i in range(r)] for i in range(c)]
for n in m2:
   print(n)

result = [[0 for i in range(r)] for i in range(c)]
for i in range(len(m1)):
        
            # iterating by column by B
  for j in range(len(m2[0])):
        
                # iterating by rows of B
    for k in range(len(m2)):
            result[i][j] += m1[i][k] * m2[k][j]
print("Multi of matrix")            
for c in result:
        print(c)         
        


