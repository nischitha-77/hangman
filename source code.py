import random
words=["Cat", "Dog", "Tree", "Book", "Ball","Orange", "Guitar", "Jacket", "Bicycle", "Puzzle",
    "Elephant", "Computer", "Chocolate", "Dinosaur", "Universe",
    "Kangaroo", "Penguin", "Giraffe", "Pasta", "Taco",
    "Pizza", "Sushi", "Sandwich", "Salad", "Icecream",
    "Iceland", "Brazil", "Canada", "Australia", "Japan",
    "France", "Italy", "Mexico", "Russia", "India",
    "Inception", "Gladiator", "Titanic", "Avatar", "Matrix",
    "Horror", "Comedy", "Drama", "Thriller", "Action",
    "Galaxy", "Meteor", "Volcano", "Ocean", "Mountain",
    "Desert", "Forest", "Island", "River", "Waterfall"]
choosen_word= random.choice(words)
choosen_word=choosen_word.lower()
word=['_' for _ in choosen_word]
attempts=10
print("Let's start the game!!")
while attempts>0 and '_' in word:
    print("\n"+' '.join(word))
    guess=input("Guess a letter:").lower()
    if guess in choosen_word:
        for index,letter in enumerate(choosen_word):
            if letter==guess:
                word[index]=guess
    else:
        print("Letter not in word")
        attempts-=1
if '_' not in word:
    print("You succeeded!!!")
    print(' '.join(word))
else:
    print("Try again later!!!"+choosen_word)
