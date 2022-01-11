def countVowels(my_string):
    count = 0
    vowels = set("aeiouAEIOU")
    for alphabet in my_string:
        if alphabet in vowels:
            count = count + 1
    return count
my_string = str("Sakti Suman")
print(countVowels(my_string))