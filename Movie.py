import random

movies_dataset = {
    "HINDI": [
        "LAGAAN", "DANGAL", "PK", "DRISHYAM", "SHOLAY",
        "ANDHADUN", "BARFI", "QUEEN", "BABY", "AIRLIFT"
    ],
    "ENGLISH": [
        "INCEPTION", "TITANIC", "GLADIATOR", "JOKER",
        "AVATAR", "INTERSTELLAR", "MATRIX", "ALIEN"
    ],
    "TAMIL": [
        "GHILLI", "ROBOT", "SIVAJI", "MASTER",
        "VIKRAM", "KAITHI", "JAI BHIM"
    ]
}

print("Choose a movie category:")
print("1. Hindi")
print("2. English")
print("3. Tamil")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    movie_list = movies_dataset["HINDI"]
elif choice == "2":
    movie_list = movies_dataset["ENGLISH"]
elif choice == "3":
    movie_list = movies_dataset["TAMIL"]
else:
    print("Invalid choice")
    exit()

movie = random.choice(movie_list)
n = len(movie)

arr = []
for i in range(n):
    arr.append("_")

print()
print("Game Rules:")
print("You have 7 chances to guess the movie name.")
print("You can enter either a letter or the full movie name.")
print()

for i in arr:
    print(i, end=" ")
print()

tries = 1
won = 0

while tries <= 7:
    guess = input("\nEnter your guess: ").upper()

    if guess == movie:
        print("Hurray! You won. The movie was", movie)
        won = 1
        break

    elif len(guess) == 1:
        found = 0
        for i in range(n):
            if movie[i] == guess:
                arr[i] = guess
                found = 1

        for i in arr:
            print(i, end=" ")
        print()

        if found == 1:
            print("Yes,", guess, "is present")
        else:
            print("Sorry,", guess, "is not present")

    else:
        print("Wrong guess")

    tries += 1
    print("Remaining chances:", 7 - tries + 1)

if won == 0:
    print("\nSorry, you lost. The correct answer was", movie)
