user1 = input("choose: rock, paper, scissors")
user2 = input("choose: rock, paper, scissors")

if user1 == "rock" or user1 == "paper" or user1 == "scissors":
    if user2 == "rock" or user2 == "paper" or user2 == "scissors":
        if user1 == user2:
            print("equal")
        elif (
            user1 == "rock"
            and user2 == "scissors"
            or user1 == "scissors"
            and user2 == "rock"
        ):
            print("rock")
        elif user1 and user2 == "rock" or "paper":
            print("paper")
        elif user1 and user2 == "scissors" or "paper":
            print("scissors")
    else:
        print("invalid user2")
else:
    print("invalid user1")
