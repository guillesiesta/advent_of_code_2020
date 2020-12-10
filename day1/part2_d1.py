''' 
--- Part Two ---

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. 
They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

In your expense report, what is the product of the three entries that sum to 2020?
'''


# abrir y leer archivo
f = open ('input.txt','r')
mensaje = f.read()
f.close()

list_numbers = mensaje.split('\n')

for i in list_numbers:
    for j in list_numbers:
        for k in list_numbers:
            if(int(i)+int(j)+int(k)==2020):
                print(int(i)*int(j)*int(k))