import hashlib
import os

def read_wordlist():
    with open('rockyou.txt', 'r', encoding='latin-1') as file:
        return [line.strip() for line in file.readlines()]
    
def check_hash(word_list, show_hash):
    for word in word_list:
        hashed_word = hashlib.sha256(word.encode()).hexdigest()
        if hashed_word == show_hash:
            return word
    return None

words = read_wordlist()

os.system('cls')
user_hash = input("Enter hash: ")

password = check_hash(words, user_hash)
if password:
    print("Pass:", password)
else:
    print("NOT Found")
