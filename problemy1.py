def count_vowels_and_consonants(text: str) -> dict:

    unli=['a','e','i','u','o',"o'",'A','E','I','U','O',"O'"]
    sum_unli=0
    sum_undosh=0
    for i in text:
        if i.isalpha():
            if i in unli:
                sum_unli+=1
            else:
                sum_undosh+=1
    matn = {"unli":sum_unli,"undosh":sum_undosh}
    return matn
print(count_vowels_and_consonants("Salom!"))
