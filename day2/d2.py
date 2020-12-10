'''
To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.

For example, suppose you have the following list:

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear
for the password to be valid. For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

In the above example, 2 passwords are valid. The middle password, cdefg, is not; it contains no instances of b, but needs at least 1. The first and third
passwords are valid: they contain one a or nine c, both within the limits of their respective policies.

How many passwords are valid according to their policies?
'''
import re

# abrir y leer archivo
f = open ('input.txt','r')
mensaje = f.read()
f.close()

list_passwords = mensaje.split('\n')
# print(list_passwords)

def verifyPass(policy_and_password):
    policy, letter, password = policy_and_password.split(" ")
    min, max = policy.split("-")
    character = " ".join(re.findall("[a-zA-Z]+", letter))
    n_times = password.count(character)

    if(int(min)<=n_times<=int(max)):
        return True
    else:
        return False


counter = 0
for i in list_passwords:
    if(verifyPass(i)==True):
        counter = counter + 1

print(counter)