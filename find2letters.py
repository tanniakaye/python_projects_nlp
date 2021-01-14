#get user input
input1 = input("\nPlease enter a sentence: ")

#assign a different variable to the input to convert it into a list 
#but don't loose original avlue
input2 = input1.lower().split()

#assign a number of letter duplicates that can be found in words
double_letter = ["ss", "ff", "rr", "ll", "mm", "pp", "ii",
                  "cc", "xx", "ee", "oo", "aa","uu", "dd",
                  "bb", "tt", "vv", "hh", "gg",
                  "nn","ww", "yy", "zz"]

#sort the list so it has a batter ascending order
d_letter = sorted(double_letter)

#increment variable for repeating letters in the loop
counter = 0
#list to append repeating character and the word it occurs in
frequent_char = []

#print the result of number of duplicate letter appearing in the word and x times
print("\nDoube letter words used in your sentece include:\n")

for word in input2:   #word is an element from the input2 list taken from input1 variable

    for char in d_letter:  #char is an element from double_letter sorted list
        
        if char in word: #loop for double letter in each input word
            counter += 1 #increment
            frequent_char.append((char,word)) #append result

#print result for each word with repeating letters
for c,w in frequent_char:
    print("The repeating letter in", w, "is -" + c + ".")

#outcome if no repeating letters found    
if counter ==0:
    print("There are no double letters in your string.")