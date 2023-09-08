from persistence import *

import sys

# python3 action.py action.txt

def main(args : "list[str]"):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            #TODO: apply the action (and insert to the table) if possible
            if int(splittedline[1]) < 0:
                prodL = repo.products.find(id = splittedline[0])
                product = prodL.pop()
                if(int(product.quantity) + int(splittedline[1]) >=0):
                    new_quantity = int(product.quantity) + int(splittedline[1])
                    # print(new_quantity)
                    repo.products.update([new_quantity], [int(splittedline[0])])
                    activitie = Activitie(splittedline[0],splittedline[1],splittedline[2],splittedline[3])
                    repo.activities.insert(activitie)

            if int(splittedline[1]) > 0:
                prodL = repo.products.find(id = splittedline[0])
                product = prodL.pop()
                new_quantity = int(product.quantity) + int(splittedline[1])
                repo.products.update([new_quantity], [int(splittedline[0])])
                activitie = Activitie(splittedline[0],splittedline[1],splittedline[2],splittedline[3])
                repo.activities.insert(activitie)





if __name__ == '__main__':
    main(sys.argv)



