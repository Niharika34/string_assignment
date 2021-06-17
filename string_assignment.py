
poem = """Earth has not any thing to show more fair:
Dull would he be of soul who could pass by
A sight so touching in its majesty:
This City now doth, like a garment, wear
The beauty of the morning; silent, bare,
Ships, towers, domes, theatres, and temples lie
Open unto the fields, and to the sky;
All bright and glittering in the smokeless air.
Never did sun more beautifully steep
In his first splendour, valley, rock, or hill;
Ne'er saw I, never felt, a calm so deep!
The river glideth at his own sweet will:
Dear God! the very houses seem asleep;
And all that mighty heart is lying still!
"""

# 1.Create a variable to store the above poem.
print(poem)

# 2.extract the first word in the second line (Hint: new line character is identified by '\n' in Python).
lines= poem.split('\n')
words_in_sec_line= lines[1].split()
print (words_in_sec_line[0])

#3. Replace all ';' by '.'
poem.replace(";", ".")

#4. Count the occurences of 'and' in the poem.
# word_count = "and"
# print(poem.split(" "))
# print(count_word(poem,word_count))
print (poem.count('and'))

#5. Count the number of words in the poem.
print (len(poem.split()))

#6. Count the number of characters in the poem.
print (len(poem))

#7. Count the number of lines in the poem
print (len(poem.split('\n')))

#8. Use string formatting to print 10th, 20th, 30th, 40th, 50th words in the poem.
words= poem.split()
print ("10th: {}".format(words[9]))
print ("20th: {}".format(words[19]))
print ("30th: {}".format(words[29]))
print ("40th: {}".format(words[39]))
print ("50th: {}".format(words[49]))


