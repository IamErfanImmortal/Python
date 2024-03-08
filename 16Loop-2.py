words = ["Dog","Cat","Mouse"]
for index , word in enumerate(words):
    words[index] = word + "s"
print(words)
print("===========")
first,second,third = words
print("second is:", second)   