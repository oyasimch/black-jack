 ## BlacK JacK
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

print(logo)

 ###     Initilization Of The Coad
import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user= []
com= []
###      User Input For Name
Prime = input('Enter Your Name You Want To Be Addresed By? \n ')

###     Formation Of Functions

def serve(i):
    for i in range(0,i):
        user.append(random.choice(cards))
        com.append(random.choice(cards))

def Draw(xx):
    xx.append(random.choice(cards))

def check(opp):
        o = 0
        x = 0
        for i in opp:
            if i == 10:
                x = 1
        for i in opp:
            if i == 11:
                o = 1
        if o+x == 2:
            return True
        else:
            return False


def winner(Prime):
    if sum(com) > 21:
        print(f'{Prime}, You Win. Your Score is   {sum(user)}')
    elif sum(user) > 21:
        print(f'{Prime}, You Lose. Your Score is   {sum(user)}')
    elif 21 >= sum(user) > sum(com):
        print(f'{Prime}, You Win. Your Score is   {sum(user)}')
    elif sum(user) < sum(com) <= 21:
        print(f'{Prime}, You Lose. Your Score is   {sum(user)}')
    elif sum(user) == sum(com):
        print ("draw")

########       MAIN        ########

serve(2)
print(f'The Score Of The {Prime} Is  {user}')
print(f'The First Card of the Computer is  {com[0]}')

if check(user) == True:
    print(f'{Prime}, You Win. Your Score is   {sum(user)}')
elif check(com) == True:
    print(f'{Prime}, You Lose. Your Score is   {sum(user)}')

while sum(user) <= 21 or sum(com) <= 21 :
    if sum(user) > 21 :
        for i in user:
            if i == 11:
                user[i] = 1
    if sum(user)<21:
        
        input_u =input("Do You Want To Draw Again ? y / n ")
        if input_u == "y":
            Draw(user)
    print(user)
    if sum(user) => 21 or input_u == "n":
        break
if sum(com) >= 21:
    print (f'{Prime}, You Win. Your Score is   {sum(user)}')
while sum(com) < 17:
    Draw(com)


print(user,com)

winner(Prime)      