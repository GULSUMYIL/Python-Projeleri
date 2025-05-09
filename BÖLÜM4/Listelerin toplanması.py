#listelerin toplamı

def list_sum(dizi1,dizi2):
  result=[]
  for i in range(len(dizi1)):
    result.append(dizi1[i]+dizi2[i])
  return result

a = [1, 2, 3]
b = [7, 8, 9]
print(list_sum(a, b))