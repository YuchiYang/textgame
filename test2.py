__author__ = 'Smaran'

class custiomio:
    def printw(self,s,w):
        w = int(w)
        print(s)
        for i in range(1000):
            for j in range(1000):
                for k in range(w):
                    pass

    def getans(self,num_options):
        a = input("")

        try:
            a=int(a)
            if (a<=0) or (a>num_options):
                print("Not a valid option")
                a=self.getans(num_options)
            else:
                return a

        except ValueError:
            if (a=='h'):
                print("Help Manual")
                print("h for help\nx for exit")
            elif (a=='x'):
                print("Exiting game")
                quit()

            elif (a=='s'):
                print("saving game")

            else:
                print("Please select a valid option")
            a=self.getans(num_options)

        return a


class current_convo(custiomio):
    next_q=0
    ans_pts=0
    def __init__(self,convo_id,rel_pts,curr_q):
        self.convo_id=convo_id
        self.rel_points=int(rel_pts)
        self.curr_q=curr_q

    def qcontinue(self,done,ask):
        # print(self.next_q,len(self.next_q))
        rel=0
        if (done==0):
            if (ask==1):
                response=self.getans(len(self.next_q))
                self.next_q=self.next_q[response-1]
                rel=self.ans_pts[response-1]
            print("sfasf",rel)
            self.curr_q=self.next_q if self.next_q>0 else 0
            return rel + self.ctutorial(self.next_q,done)
        if (done==1):
            return 0


    def csel(self,cs):
        cs=int(cs)
        rel=0
        if (cs==0):
            rel=self.ctutorial(self.curr_q,0)
        elif (cs==1):
            self.ctom_d1(0)

        self.rel_points=rel


    def ctutorial(self,curr_q,done):
        ans_pts=0
        next_q=0
        ask=1
        n=curr_q

        if (n==-1):
            print("Ok I'm done talking to you bye")
            done=1

        elif(n==-9):
            print("You have finished this convo. More is soon to come")
            done=1

        elif(n==-12):
            print("ex of statement without q")
            n=2
            ask=0

        elif (n==0):
            print ("\n Welcome to the choice based game\n \n")
            print("I will give you a summary of how to play this game, its very easy but I can tell you anyway")
            print("would you like to learn")
            print ("1. Sure!")
            print ("2. No thanks, I can figure it out")
            ans_pts=[1,3]
            next_q=[1,2]

        elif (n==1):
            print("\n So you wake up one day bbla bla bla \n \n")
            print ("got it?")
            print ("1. yes")
            print ("2. no can you please repeat that??")
            ans_pts=[4,9]
            next_q=[-9,1]

        elif (n==2):
            print ("\n CoOoOoOoOl?\n \n")
            n=-9
            ask=0
            done=1

        self.ans_pts=ans_pts
        self.next_q=next_q
        return self.qcontinue(done,ask)


    def ctom_d1(self,n):
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
            qval=[2,-5,6]

        elif (n==1):
            print ("\n How was your day? \n \n")
            print ("1. It was good")
            print ("2. why do you care?")
            print ("3. good now that you are here")
            qval=[1,-3,99]

        elif (n==2):
            print ("\n It's Tom!? what happened to you?\n \n")
            print ("1. Sorry Tom, had a rough day..")
            print ("2. Whatever.. Im out!")
            qval=[2,-10]

        elif (n==3):
            print ("\n Good to hear, so would you like dinner?\n \n")
            print ("1. Yeah I would love to!")
            print ("2. Sure are you going to make something special for me?")
            print ("3. Lets go to Mcdonalds!")
            qval=[7,12,3]

        elif (n==4):
            print ("\n Whoa whats the matter? \n \n")
            print ("1. Nothing...")
            print ("2. Leave me alone loser!")
            print ("3. Just stessed")
            qval=[0,-7,2]

        elif (n==5):
            print ("\n Sure! I will make something special for you \n \n")
            print ("1. yay")
            print ("2. But you suck")
            qval=[5,-4]

        elif (n==6):
            print ("\n Where can we eat")
            print ("1. Le Fancy ")
            print ("2. Idk anything")
            print ("3. Mcdonalds")
            qval=[6,-1,0]

        elif (n==7):
            print ("yo smaran why are you trying to be Tom?")
            print ("1. bc im black yo")
            print ("2. just for fun")
            print ("3. I'm secretly.. Tom Riddle dun dun..")
            qval=[2,0,-5]

        elif (n==301):
            print("ughhhh Mcdonalds?? Can you think of something else")
            qval=[-5,0]

        return qtype

class character:
    def __init__(self,name,rel_points,curr_q,curr_c):
        self.name=name
        self.rel_points=int(rel_points)
        self.curr_q=curr_q
        self.curr_c=curr_c

    def haveconvo(self):
        convo=current_convo(self.curr_c,self.rel_points,self.curr_q)
        convo.csel(self.curr_c)
        print(convo.rel_points)
        self.rel_points=convo.rel_points

class action:
    def __init__(self):
        pass

    def intro(self):
        print("welcome to game. \nPress h for help at any time")
        input("Press any key to start")

    def chars(self):
        tom=character("tom",10,0,1)
        jim=character("Jim",0,0,2)

if __name__ == "__main__":
    # intro()
    tom=character("tom",0,0,0)
    tom.haveconvo()
    print(tom.rel_points)
