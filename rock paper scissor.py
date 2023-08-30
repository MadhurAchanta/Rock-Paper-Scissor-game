from random import*
a="rock","paper","scissor"
x=input("enter your choice in lower case\n")
b=choice(a)
if b=="rock" and x=="paper":
    print("you won")
elif b=="rock" and x=="scissor":
    print("I won")
elif b=="rock" and x=="rock":
    print("draw")
elif b=="paper" and x=="scissor":
    print("you won")
elif b=="paper" and x=="rock":
    print("I won")
elif b=="paper" and x=="paper":
    print("draw")
elif b=="scissor" and x=="scissor":
    print("draw")
elif b=="scissor" and x=="paper":
    print("I won")
elif b=="scissor" and x=="rock":
    print("you won")
print("my choice is:",b)
