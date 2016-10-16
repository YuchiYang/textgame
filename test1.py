def intro():
    print("welcome to game. \nPress h for help at any time")
    input("Press any key to start")

def qbank(n):
    n=int(n)
    qtype=0
    if(n==-1):
        print("Game over")
        quit()

    if(n==-9):
        print("You have finished the demo. More is soon to come")
        quit()

    if (n==0):
        print ("\n Hello Yuchy\n \n")
        print ("1. Hello Tom")
        print ("2. who the hell are you?")
        print ("3. Sup babe")
        qtype=[2,-5,6]

    elif (n==1):
        print ("\n How was your day? \n \n")
        print ("1. It was good")
        print ("2. why do you care?")
        print ("3. good now that you are here")
        qtype=[1,-3,99]

    elif (n==2):
        print ("\n It's Tom!? what happened to you?\n \n")
        print ("1. Sorry Tom, had a rough day..")
        print ("2. Whatever.. Im out!")
        qtype=[2,-10]

    elif (n==3):
        print ("\n Good to hear, so would you like dinner?\n \n")
        print ("1. Yeah I would love to!")
        print ("2. Sure are you going to make something special for me?")
        print ("3. Lets go to Mcdonalds!")
        qtype=[7,12,3]

    elif (n==4):
        print ("\n Whoa whats the matter? \n \n")
        print ("1. Nothing...")
        print ("2. Leave me alone loser!")
        print ("3. Just stessed")
        qtype=[0,-7,2]

    elif (n==5):
        print ("\n Sure! I will make something special for you \n \n")
        print ("1. yay")
        print ("2. But you suck")
        qtype=[5,-4]

    elif (n==6):
        print ("\n Where can we eat")
        print ("1. Le Fancy ")
        print ("2. Idk anything")
        print ("3. Mcdonalds")
        qtype=[6,-1,0]

    elif (n==7):
        print ("yo smaran why are you trying to be Tom?")
        print ("1. bc im black yo")
        print ("2. just for fun")
        print ("3. I'm secretly.. Tom Riddle dun dun..")
        qtype=[2,0,-5]

    elif (n==301):
        print("ughhhh Mcdonalds?? Can you think of something else")
        qtype=[-5,0]

    return qtype


def getans(num_options):
    a = input("")

    try:
        a=int(a)
        if (a<=0) or (a>num_options):
            print("Not a valid option")
            a=getans(num_options)
        else:
            return a

    except ValueError:
        if (a=='h'):
            print("Help Manual")
            print("h for help\nx for exit")
        elif (a=='x'):
            print("Exiting game")
            quit()
        else:
            print("Please select a valid option")
        a=getans(num_options)

    return a

def qmap():
    q=[]
    for i in range(100):
        q.append(0)
    q[0]=[0,1,2,1]
    q[1]=[1,3,4,3]
    q[2]=[2,3,-1]
    q[3]=[3,6,5,301]
    q[4]=[4,-9,-9,-9]
    q[5]=[5,-9,-9]
    q[6]=[6,-9,7,-9]
    q[7]=[301,6]
    q[8]=[7,1,2,3]

    return q

def wait(n):
    for looptime in range (10000):
        for looptime2 in range (n):
            a=1

def currentfinder(qmap1,pos):
    t=0
    if(pos<0):
        return pos
    for i in range (0,len(qmap1)+1):
        t=qmap1[i][0]
        if (pos==t):
            return i
    
if __name__ == "__main__":
    intro()
    relation_points=0
    current_question_index=0
    questionid=0
    qmapper=qmap()

    while(1):
        current_question_index = currentfinder(qmapper,questionid)
        all_rel_pts = qbank(questionid)
        if(all_rel_pts[0]==-5):
            questionid=qmapper[current_question_index][1]
            continue
        answer = getans(len(qmapper[current_question_index])-1)
        relation_points+=all_rel_pts[answer-1]
        questionid=qmapper[current_question_index][answer]
