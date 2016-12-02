__author__ = 'Smaran'
import json

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


class character:
    # self.name="BOT"
    # self.rel_points=100
    def __init__(self,name):
        self.name=name
        with open('.\\files\\progress.json') as data_file:
            data = json.load(data_file)
        self.rel_points=data[name][relationship_pts]

    def haveconvo(self):
        convo=current_convo(self.curr_c,self.rel_points,self.curr_q)
        convo.csel(self.curr_c)
        print(convo.rel_points)
        self.rel_points=convo.rel_points


if __name__ == "__main__":
    def intro():
        print("welcome to game. \nPress h for help at any time")
        input("Press any key to start")

    def loadProgress():
        l=[]
        data_name=[]
        with open('.\\files\\progress.json') as data_file:
            data = json.load(data_file)

        # a=len(data['convos'])
        # l.append(data['convos'][1]['convo'])
        # print(l,"lol ",a)

        for i in range (len(data['convos'])):
            l.append(data['convos'][i]['convo'])
            with open(l[i]) as data_file:
                data_name.append(json.load(data_file))

        print("Availible chats-")
        print(data_name[0]['title'])
        print(data_name[1]['title'])


    # intro()
    loadProgress()
    # tom=character("tom")
    # tom.haveconvo()
    # print(tom.rel_points)
