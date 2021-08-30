from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
import threading
import random
import time


class Main(BoxLayout):
    
    def pp(self):
        self.speed = 3
        #print(self.ids.gobtn.state)
        self.spd = Clock.schedule_interval(self.incSpeed,0.05)
        
    def rollit(self):
        #random spin(UpWards[0] or DownWards[1])
        self.ids.gobtn.disabled = True
        print(Window.size)
        print(self.ids.gobtn.size)
        print(self.ids.b11.size)
        self.spd.cancel()
        self.c1 = random.randint(0,1)
        self.c2 = random.randint(0,1)
        self.c3 = random.randint(0,1)

        self.sf1,self.sf2,self.sf3 = 1,1,1

        nL = [100,1000,10000,100000,10000000]
            
        self.slot1 = Clock.schedule_interval(self.s1, random.random() / nL[random.randint(0,4)])
        self.slot2 = Clock.schedule_interval(self.s2, random.random() / nL[random.randint(0,4)])
        self.slot3 = Clock.schedule_interval(self.s3, random.random() / nL[random.randint(0,4)])

        #Moving wheels for 5 seconds
        t = threading.Thread(target = self.timer)
        t.start()
        self.lock = threading.Lock()

    def incSpeed(self,uknwn):
        if self.speed < 31:
            self.speed = self.speed + 1
            self.ids.pgpow.value += 1 
        else:
            pass

    def timer(self):
        t = time.time()
        while (time.time() - t < random.randint(2,5)):
            time.sleep(1)
        else:
            t = 0
            while t != 1:
                self.lock.acquire()
                if self.sf1 == 0:
                    self.slot1.cancel()
                    t += 1
                else:
                    continue
                self.lock.release()
            t = 0
            while t != 1:
                self.lock.acquire()
                if self.sf2 == 0:
                    self.slot2.cancel()
                    t += 1
                else:
                    continue
                self.lock.release()
            t = 0
            while t != 1:
                self.lock.acquire()
                if self.sf3 == 0:
                    self.slot3.cancel()
                    t += 1
                else:
                    continue
                self.lock.release()
        self.ids.gobtn.disabled = False
        self.scorecalc()
    
    def s1(self,uknwn):
        if self.c1 == 0:
            self.lock.acquire()
            self.sf1 = 1
            self.ids.b1.pos[1] += self.speed
            self.ids.b2.pos[1] += self.speed
            self.ids.b3.pos[1] += self.speed
            self.ids.b4.pos[1] += self.speed
            self.ids.b11.pos[1] += self.speed
            self.sf1 = 0
            self.lock.release()
            if int(self.ids.b11.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b11.pos[1] - Window.size[1]
                self.ids.b11.pos[1] = Window.size[1] + junkspace - 5*self.ids.b1.height
            if int(self.ids.b1.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b1.pos[1] - Window.size[1]
                self.ids.b1.pos[1] = Window.size[1] + junkspace - 5*self.ids.b1.height
            if int(self.ids.b2.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b2.pos[1] - Window.size[1]
                self.ids.b2.pos[1] = Window.size[1] + junkspace - 5*self.ids.b2.height
            if int(self.ids.b3.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b3.pos[1] - Window.size[1]
                self.ids.b3.pos[1] = Window.size[1] + junkspace - 5*self.ids.b3.height
            if int(self.ids.b4.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b4.pos[1] - Window.size[1]
                self.ids.b4.pos[1] = Window.size[1] + junkspace - 5*self.ids.b4.height
        else:
            self.lock.acquire()
            self.sf1 = 1
            self.ids.b1.pos[1] -= self.speed
            self.ids.b2.pos[1] -= self.speed
            self.ids.b3.pos[1] -= self.speed
            self.ids.b4.pos[1] -= self.speed
            self.ids.b11.pos[1] -= self.speed
            self.sf1 = 0
            self.lock.release()
            if int(self.ids.b11.pos[1]) <= int(Window.size[1]-5*self.ids.b1.height):
                junkspace = Window.size[1]-5*self.ids.b1.height - self.ids.b11.pos[1]
                self.ids.b11.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b1.pos[1]) <= int(Window.size[1]-5*self.ids.b1.height):
                junkspace = Window.size[1]-5*self.ids.b1.height - self.ids.b1.pos[1]
                self.ids.b1.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b2.pos[1]) <= int(Window.size[1]-5*self.ids.b1.height):
                junkspace = Window.size[1]-5*self.ids.b1.height - self.ids.b2.pos[1]
                self.ids.b2.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b3.pos[1]) <= int(Window.size[1]-5*self.ids.b1.height):
                junkspace = Window.size[1]-5*self.ids.b1.height - self.ids.b3.pos[1]
                self.ids.b3.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b4.pos[1]) <= int(Window.size[1]-5*self.ids.b1.height):
                junkspace = Window.size[1]-5*self.ids.b1.height - self.ids.b4.pos[1]
                self.ids.b4.pos[1] = Window.size[1] - junkspace
                
    def s2(self,uknwn):
        if self.c2 == 0:
            self.lock.acquire()
            self.sf2 = 1
            self.ids.b5.pos[1] += self.speed
            self.ids.b6.pos[1] += self.speed
            self.ids.b7.pos[1] += self.speed
            self.ids.b8.pos[1] += self.speed
            self.ids.b55.pos[1] += self.speed
            self.sf2 = 0
            self.lock.release()
            if int(self.ids.b55.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b55.pos[1] - Window.size[1]
                self.ids.b55.pos[1] = Window.size[1] + junkspace - 5*self.ids.b1.height
            if int(self.ids.b5.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b5.pos[1] - Window.size[1]
                self.ids.b5.pos[1] = Window.size[1] + junkspace - 5*self.ids.b1.height
            if int(self.ids.b6.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b6.pos[1] - Window.size[1]
                self.ids.b6.pos[1] = Window.size[1] + junkspace - 5*self.ids.b2.height
            if int(self.ids.b7.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b7.pos[1] - Window.size[1]
                self.ids.b7.pos[1] = Window.size[1] + junkspace - 5*self.ids.b3.height
            if int(self.ids.b8.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b8.pos[1] - Window.size[1]
                self.ids.b8.pos[1] = Window.size[1] + junkspace - 5*self.ids.b4.height
        else:
            self.lock.acquire()
            self.sf2 = 1
            self.ids.b5.pos[1] -= self.speed
            self.ids.b6.pos[1] -= self.speed
            self.ids.b7.pos[1] -= self.speed
            self.ids.b8.pos[1] -= self.speed
            self.ids.b55.pos[1] -= self.speed
            self.sf2 = 0
            self.lock.release()
            if int(self.ids.b55.pos[1]) <= int(Window.size[1]-5*self.ids.b1.height):
                junkspace = Window.size[1]-5*self.ids.b1.height - self.ids.b55.pos[1]
                self.ids.b55.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b5.pos[1]) <= int(Window.size[1]-5*self.ids.b1.height):
                junkspace = Window.size[1]-5*self.ids.b1.height - self.ids.b5.pos[1]
                self.ids.b5.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b6.pos[1]) <= int(Window.size[1]-5*self.ids.b1.height):
                junkspace = Window.size[1]-5*self.ids.b1.height - self.ids.b6.pos[1]
                self.ids.b6.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b7.pos[1]) <= int(Window.size[1]-5*self.ids.b1.height):
                junkspace = Window.size[1]-5*self.ids.b1.height - self.ids.b7.pos[1]
                self.ids.b7.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b8.pos[1]) <= int(Window.size[1]-5*self.ids.b1.height):
                junkspace = Window.size[1]-5*self.ids.b1.height - self.ids.b8.pos[1]
                self.ids.b8.pos[1] = Window.size[1] - junkspace

    def s3(self,uknwn):
        if self.c3 == 0:
            self.lock.acquire()
            self.sf3 = 1
            self.ids.b9.pos[1] += self.speed
            self.ids.b10.pos[1] += self.speed
            self.ids.b11_.pos[1] += self.speed
            self.ids.b12.pos[1] += self.speed
            self.ids.b99.pos[1] += self.speed
            self.sf3 = 0
            self.lock.release()
            if int(self.ids.b99.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b99.pos[1] - Window.size[1]
                self.ids.b99.pos[1] = Window.size[1] + junkspace - 5*self.ids.b1.height
            if int(self.ids.b9.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b9.pos[1] - Window.size[1]
                self.ids.b9.pos[1] = Window.size[1] + junkspace - 5*self.ids.b1.height
            if int(self.ids.b10.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b10.pos[1] - Window.size[1]
                self.ids.b10.pos[1] = Window.size[1] + junkspace - 5*self.ids.b2.height
            if int(self.ids.b11_.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b11_.pos[1] - Window.size[1]
                self.ids.b11_.pos[1] = Window.size[1] + junkspace - 5*self.ids.b3.height
            if int(self.ids.b12.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b12.pos[1] - Window.size[1]
                self.ids.b12.pos[1] = Window.size[1] + junkspace -5*self.ids.b4.height
        else:
            self.lock.acquire()
            self.sf3 = 1
            self.ids.b9.pos[1] -= self.speed
            self.ids.b10.pos[1] -= self.speed
            self.ids.b11_.pos[1] -= self.speed
            self.ids.b12.pos[1] -= self.speed
            self.ids.b99.pos[1] -= self.speed
            self.sf3 = 0
            self.lock.release()
            if int(self.ids.b9.pos[1]) <= int(Window.size[1]-5*self.ids.b1.height):
                junkspace = Window.size[1]-5*self.ids.b1.height - self.ids.b9.pos[1]
                self.ids.b9.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b10.pos[1]) <= int(Window.size[1]-5*self.ids.b1.height):
                junkspace = Window.size[1]-5*self.ids.b1.height - self.ids.b10.pos[1]
                self.ids.b10.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b11_.pos[1]) <= int(Window.size[1]-5*self.ids.b1.height):
                junkspace = Window.size[1]-5*self.ids.b1.height - self.ids.b11_.pos[1]
                self.ids.b11_.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b12.pos[1]) <= int(Window.size[1]-5*self.ids.b1.height):
                junkspace = Window.size[1]-5*self.ids.b1.height - self.ids.b12.pos[1]
                self.ids.b12.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b99.pos[1]) <= int(Window.size[1]-5*self.ids.b1.height):
                junkspace = Window.size[1]-5*self.ids.b1.height - self.ids.b99.pos[1]
                self.ids.b99.pos[1] = Window.size[1] - junkspace

    def fixpointloc(self):
        #range of each 9 cells
        #x-axis size(min), y-axis size(min), x-axis size(max), y-axix size(max)
        #starting from upper to right = r1,middle to right = r2,end to right = r3
        global cd
        if cd == 1:
            c1_ = (self.ids.b1.pos[0],self.ids.b1.pos[1],self.ids.b1.pos[0]+self.ids.b1.size[0],self.ids.b1.pos[1]+self.ids.b1.size[1])
            c2_ = (self.ids.b5.pos[0],self.ids.b5.pos[1],self.ids.b5.pos[0]+self.ids.b5.size[0],self.ids.b5.pos[1]+self.ids.b5.size[1])
            c3_ = (self.ids.b9.pos[0],self.ids.b9.pos[1],self.ids.b9.pos[0]+self.ids.b9.size[0],self.ids.b9.pos[1]+self.ids.b9.size[1])
            c4 = (self.ids.b2.pos[0],self.ids.b2.pos[1],self.ids.b2.pos[0]+self.ids.b2.size[0],self.ids.b2.pos[1]+self.ids.b2.size[1])
            c5 = (self.ids.b6.pos[0],self.ids.b6.pos[1],self.ids.b6.pos[0]+self.ids.b6.size[0],self.ids.b6.pos[1]+self.ids.b6.size[1])
            c6 = (self.ids.b10.pos[0],self.ids.b10.pos[1],self.ids.b10.pos[0]+self.ids.b10.size[0],self.ids.b10.pos[1]+self.ids.b10.size[1])
            c7 = (self.ids.b3.pos[0],self.ids.b3.pos[1],self.ids.b3.pos[0]+self.ids.b3.size[0],self.ids.b3.pos[1]+self.ids.b3.size[1])
            c8 = (self.ids.b7.pos[0],self.ids.b7.pos[1],self.ids.b7.pos[0]+self.ids.b7.size[0],self.ids.b7.pos[1]+self.ids.b7.size[1])
            c9 = (self.ids.b11_.pos[0],self.ids.b11_.pos[1],self.ids.b11_.pos[0]+self.ids.b11_.size[0],self.ids.b11_.pos[1]+self.ids.b11_.size[1])
            cd = 0
            self.ccc = [c1_,c2_,c3_,c4,c5,c6,c7,c8,c9]
        
    def scorecalc(self):
        #print("self.c1= ",self.c1_,"\nself.c2= ",self.c2_,"\nself.c3= ",self.c3_,"\nself.c4= ",self.c4,"\nself.c5= ",self.c5,"\nself.c6= ",self.c6,"\nself.c7= ",self.c7,"\nself.c8= ",self.c8,"\nself.c9= ",self.c9)        
        #aproxx. positions after run of every item
        pt1 = (self.ids.b1,self.ids.b1.pos[0]+self.ids.b1.size[0]/2,self.ids.b1.pos[1]+self.ids.b1.size[1]/2)
        pt2 = (self.ids.b2,self.ids.b2.pos[0]+self.ids.b2.size[0]/2,self.ids.b2.pos[1]+self.ids.b2.size[1]/2)
        pt3 = (self.ids.b3,self.ids.b3.pos[0]+self.ids.b3.size[0]/2,self.ids.b3.pos[1]+self.ids.b3.size[1]/2)
        pt4 = (self.ids.b4,self.ids.b4.pos[0]+self.ids.b4.size[0]/2,self.ids.b4.pos[1]+self.ids.b4.size[1]/2)
        pt11 = (self.ids.b11,self.ids.b11.pos[0]+self.ids.b11.size[0]/2,self.ids.b11.pos[1]+self.ids.b11.size[1]/2)
        pt5 = (self.ids.b5,self.ids.b5.pos[0]+self.ids.b5.size[0]/2,self.ids.b5.pos[1]+self.ids.b5.size[1]/2)
        pt55 = (self.ids.b55,self.ids.b55.pos[0]+self.ids.b55.size[0]/2,self.ids.b55.pos[1]+self.ids.b55.size[1]/2)
        pt6 = (self.ids.b6,self.ids.b6.pos[0]+self.ids.b6.size[0]/2,self.ids.b6.pos[1]+self.ids.b6.size[1]/2)
        pt7 = (self.ids.b7,self.ids.b7.pos[0]+self.ids.b7.size[0]/2,self.ids.b7.pos[1]+self.ids.b7.size[1]/2)
        pt8 = (self.ids.b8,self.ids.b8.pos[0]+self.ids.b8.size[0]/2,self.ids.b8.pos[1]+self.ids.b8.size[1]/2)
        pt9 = (self.ids.b9,self.ids.b9.pos[0]+self.ids.b9.size[0]/2,self.ids.b9.pos[1]+self.ids.b9.size[1]/2)
        pt99 = (self.ids.b99,self.ids.b99.pos[0]+self.ids.b99.size[0]/2,self.ids.b99.pos[1]+self.ids.b99.size[1]/2)
        pt10 = (self.ids.b10,self.ids.b10.pos[0]+self.ids.b10.size[0]/2,self.ids.b10.pos[1]+self.ids.b10.size[1]/2)
        pt11_ = (self.ids.b11_,self.ids.b11_.pos[0]+self.ids.b11_.size[0]/2,self.ids.b11_.pos[1]+self.ids.b11_.size[1]/2)
        pt12 = (self.ids.b12,self.ids.b12.pos[0]+self.ids.b12.size[0]/2,self.ids.b12.pos[1]+self.ids.b12.size[1]/2)

        #print("pt1= ",pt1,"\npt2= ",pt2,"\npt3= ",pt3,"\npt4= ",pt4,"\npt11= ",pt11,"\npt5= ",pt5,"\npt55= ",pt55,"\npt6= ",pt6,"\npt7= ",pt7,"\npt8= ",pt8,"\npt9= ",pt9,"\npt99= ",pt99,"\npt10= ",pt10,"\npt11_= ",pt11_,"\npt12= ",pt12)
        #print(pt1[0].pos)
        ptl = [pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8,pt9,pt10,pt11_,pt12,pt11,pt55,pt99]
        del pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8,pt9,pt10,pt11_,pt12,pt11,pt55,pt99
        r1 = []
        r2 = []
        r3 = []

        cd_ = 1
        for i in self.ccc:
            for j in ptl:
                if j[1] > i[0] and j[1] < i[2] and j[2] > i[1] and j[2] < i[3]:
                    if cd_ <= 3:
                        r1.append(j[0])
                    elif cd_ <= 6 and cd_ > 3:
                        r2.append(j[0])
                    elif cd_ > 6 and cd_ <=9:
                        r3.append(j[0])
                    cd_ += 1

        score = 0
        
        if r1[0].text == r1[1].text:
            score += 100
        if r1[1].text == r1[2].text:
            score += 100
        if r2[0].text == r2[1].text:
            score += 100
        if r2[1].text == r2[2].text:
            score += 100
        if r3[0].text == r3[1].text:
            score += 100
        if r3[1].text == r3[2].text:
            score += 100

        if r1[0].text == r1[2].text:
            score += 50
        if r2[0].text == r2[2].text:
            score += 50
        if r3[0].text == r3[2].text:
            score += 50
        """if r1[0].text == r1[1].text == r1[2].text:
            score += 30
            self.ids.trys.text = "Chances: " + str(int(self.ids.trys.text[9:]) + 3)
        if r2[0].text == r2[1].text == r2[2].text:
            score += 30
            self.ids.trys.text = "Chances: " + str(int(self.ids.trys.text[9:]) + 3)
        if r3[0].text == r3[1].text == r3[2].text:
            score += 30
            self.ids.trys.text = "Chances: " + str(int(self.ids.trys.text[9:]) + 3)"""
        if r1[0].text == r1[1].text == r1[2].text and r2[0].text == r2[1].text == r2[2].text and r3[0].text == r3[1].text == r3[2].text:
            score += 250
            self.ids.trys.text = "Chances: " + str(int(self.ids.trys.text[9:]) + 10)

        self.ids.scrs.text = "Score: " + str(int(self.ids.scrs.text[6:]) + score)

        if int(self.ids.target.text[9:]) < int(self.ids.scrs.text[6:]):
            self.ids.lev.text = "Level: " + str(int(self.ids.lev.text[7:]) + 1)
            self.ids.target.text = "Targate: " + str(int(self.ids.target.text[9:])+2000*int(self.ids.lev.text[7:]))
        if int(self.ids.target.text[9:]) < int(self.ids.scrs.text[6:]) and int(self.ids.trys.text[9:]) < 1:
            self.ids.target.text = "Targate: " + str(int(self.ids.target.text[9:]) - 2000*int(self.ids.lev.text[7:]))
            self.ids.lev.text = "Level: " + str(int(self.ids.lev.text[7:]) - 1)
            self.ids.trys.text = "Chances: " + str(int(self.ids.trys.text[9:]) + 1 + int(self.ids.lev.text[7:])*10)
            self.ids.scrs.text = "Score: " + str(int(self.ids.target.text[9:]) - 2000*(int(self.ids.lev.text[7:])-1))
        #print(int(self.ids.trys.text[9:]))
        self.ids.trys.text = "Chances: " + str(int(self.ids.trys.text[9:]) - int(self.ids.lev.text[7:]))
        if self.ids.lev.text[7:] == "1" and int(self.ids.trys.text[9:]) < 1:
            self.ids.scrs.text = "Score: 0"
            self.ids.trys.text = "Chances: 10"
        self.ids.pgpow.value = 1

        
class Lucky_Win(App):
    pass

cd = 1
Lucky_Win().run()
