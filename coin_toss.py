# FILE NAME - coin_toss.py

# NAME: Kandise Perkins
# DATE: October 5, 2025
# BRIEF DESCRIPTION: generate a coin toss, if user enters numbers
#   51 or greater make it Tails. 



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience

import random

########## ENTER YER CODE BELOW THIS LINE ##########

# Don't forget to import random!!!!!
def main():
    coin_flip()
def coin_flip():
    print('===== Coin Flipper =====')

    #random number 1-100
    number = random.randint(1,100)

#output
    if number >= 51:
        print('Tails')
    else:
        print('Heads')


main()


########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 
The lab was fairly intuitive thankful for the jupyter notes. I forgot 
to imput the random number generator and restrict the boundaries 1-100.






'''
