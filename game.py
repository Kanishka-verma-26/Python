import random

def get_guess():
    return list(input("Whats is your guessed number : "))

def generate_code():
    digits = [str(i) for i in range(10)]
    random.shuffle(digits)
    #random 3 digit code
    return digits[-3:]

def gen_clues(code,user_guess):
    if user_guess == code:
        return "CODE CRACKED!"

    clues = []

    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("match")
        elif num in code:
            clues.append("Close")
        else:
            clues.append("Nope")
    if clues == []:
        return ["Nope"]
    else:
        return clues


print("Welcome code Breaker!")
secret_code = generate_code()
clue_report = []
while clue_report != "CODE CRACKED":
    guess = get_guess()
    clue_report = gen_clues(guess,secret_code)
    print("Here is the result of your guess : ")
    for i in clue_report:
        print(i)
