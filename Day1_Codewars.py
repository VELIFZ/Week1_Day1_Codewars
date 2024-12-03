# Odd or Even

def even_or_odd(number):
    if (number % 2 == 0):
        return 'Even'
    else:
        return "Odd"
    
# Convert a number to a string

def number_to_string(num):
    return str(num)

# Vowel Count

sentence = 'elif'
vowel = ['a', 'e', 'i', 'o', 'u']
v_count =[]
for v in sentence:
    if v in vowel:
        v_count.append(v)
        
print(len(v_count))