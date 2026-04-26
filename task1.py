matn=input("Matn kiriting: ")
unli=['a','e','i','u','o',"o'",'A','E','I','U','O',"O'"]
sum_unli=0
sum_undosh=0
for i in matn:
    if i.isalpha():
        if i in unli:
            sum_unli+=1
        else:
            sum_undosh+=1
matn = {"unli":sum_unli,"undosh":sum_undosh}
print(matn)        
