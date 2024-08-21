def loveApp():
        print("This is a love app that check for to compatible couples.")
        loveCalculator()



def loveCalculator():
        """This is a love calculator that check for two compatible couples."""
       
        boyfriend_name=str(input("please enter boyfriend name:"))
        girlfriend_name=str(input("please enter girlfriend name:"))
        word1=['t','r','u','e']
        word2=['l','o','v','e']
        count1=0
        count2=0
        for i in boyfriend_name:
        if i in word1:
        count1=count1+1
        for i in girlfriend_name:
        if i in word1:
        count1=count1+1
        for i in boyfriend_name:
        if i in word2:
                        count2=count2+1
        for i in girlfriend_name:
                if i in word2:
                        count2=count2+1 
                        score=int(str(count1)+str(count2))
        if score<10 or score >90:
                print(f"Your score is {score} you both are match")
        elif score > 40 and score < 50:
                print(f"Your score is {score} You are partially match")
        else:
        print(f"Your score is,{score}")
        print()
loveApp()