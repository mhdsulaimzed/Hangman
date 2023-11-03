import random

def get_random_words(wordfile="/usr/share/dict/words"):

    goodwords=[]
    
    with open(wordfile) as w:
        words=[x.strip() for x in w]
        for i in words:
            if not i.islower():
                continue

            if not i.isalpha():
                continue

            if  len(i) <5:
                continue

            

            
            else:
                goodwords.append(i)
    return random.choice(goodwords)






def masking_random_word():
    global r_w
    r_w=get_random_words()
    word_length=len(r_w)
    return "_"*word_length , r_w



def user_input():
    counter=0
    guessed_letter=[]
    for i in range(0,7):
        input_letter=input("enter a letter")
        guessed_letter.append(input_letter)
        counter+=1
        print(counter)
        if input_letter in r_w:



            
            
            print(guessed_letter)
            print("T")
            

        else:
            
            
            print(guessed_letter)
            print("F")

        
print(masking_random_word()  )    

user_input()
    
        
    
    


   















if  __name__ == "__main__":
    pass





