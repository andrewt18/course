count = 0
summa = 0
while (count < 1000):
   if (count % 3 == 0) or (count % 5 == 0):
      summa += count
      count += 1
   else:
      count +=1
print(summa)