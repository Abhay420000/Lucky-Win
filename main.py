from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
import threading
import random
import time
from kivy.core.audio import Sound, SoundLoader

#print(Window.size)


class Main(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.sound = SoundLoader.load('./MSIco/sound.wav')
        self.music = SoundLoader.load('./MSIco/music.wav')
        self.music.loop = True
        self.music.play()

        #Play the sound
        self.s_cd = True

    def config_sound(self):
        if self.s_cd == True:
            self.s_cd = False
            self.ids.bsof.s = "./MSIco/no-sound.png"
        elif self.s_cd == False:
            self.s_cd = True
            self.ids.bsof.s = "./MSIco/sound.png"
    
    def config_music(self):
        if self.music.state == "play":
            self.music.stop()
            self.ids.bmof.s = "./MSIco/no-music.png"
        elif self.music.state == "stop":
            self.music.play()
            self.ids.bmof.s = "./MSIco/music.png"

    def pp(self):
        self.speed = 3
        #print(self.ids.gobtn.state)
        self.spd = Clock.schedule_interval(self.incSpeed,0.05)
        
    def rollit(self):
        #random spin(UpWards[0] or DownWards[1])
        self.ids.gobtn.disabled = True
        #print(Window.size)
        #print(self.ids.gobtn.size)
        #print(self.ids.b11.size)
        self.spd.cancel()

        #Determine the rotation of slots
        self.c1 = random.randint(0,1)
        self.c2 = random.randint(0,1)
        self.c3 = random.randint(0,1)

        self.sf1,self.sf2,self.sf3 = 1,1,1

        nL = [100,1000,10000,100000,10000000]
            
        self.slot1 = Clock.schedule_interval(self.s1, random.random() / nL[random.randint(0,4)])
        self.slot2 = Clock.schedule_interval(self.s2, random.random() / nL[random.randint(0,4)])
        self.slot3 = Clock.schedule_interval(self.s3, random.random() / nL[random.randint(0,4)])

        #Moving wheels for 1-5 seconds
        t = threading.Thread(target = self.timer, daemon= True)
        t.start()
        self.lock = threading.Lock()

    def incSpeed(self,uknwn):
        if self.speed < 31:
            self.speed = self.speed + 1
            self.ids.pgpow.value += 1
            if self.speed < 10:
                self.ids.g1.color = (random.randint(0,255)/255,random.randint(0,255)/255,random.randint(0,255)/255)
            elif self.speed < 20:
                self.ids.g2.color = (random.randint(0,255)/255,random.randint(0,255)/255,random.randint(0,255)/255)
            elif self.speed < 30:
                self.ids.g3.color = (random.randint(0,255)/255,random.randint(0,255)/255,random.randint(0,255)/255)
        else:
            pass

    def timer(self):
        t = time.time()

        if self.s_cd == True:
            self.sound.play()

        #Determining Slot rotation time according speed
        if self.speed < 8:
            time_tr = 2
        elif self.speed < 15:
            time_tr = 3
        elif self.speed < 22:
            time_tr = 4
        else:
            time_tr = 5 
        
        #print(time_tr," sec run")

        #Timer for rolling
        while (time.time() - t < time_tr):
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
    
        if self.s_cd == True:
            self.sound.stop()

    def s1(self,uknwn):
        if self.c1 == 0:
            self.lock.acquire()
            self.sf1 = 1
            self.ids.b0.pos[1] += self.speed
            self.ids.b1.pos[1] += self.speed
            self.ids.b2.pos[1] += self.speed
            self.ids.b3.pos[1] += self.speed
            self.ids.b4.pos[1] += self.speed
            self.ids.b5.pos[1] += self.speed
            self.ids.b6.pos[1] += self.speed
            self.sf1 = 0
            self.lock.release()
            if int(self.ids.b0.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b0.pos[1] - Window.size[1]
                self.ids.b0.pos[1] = Window.size[1] + junkspace - 7*self.ids.b0.height
            if int(self.ids.b1.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b1.pos[1] - Window.size[1]
                self.ids.b1.pos[1] = Window.size[1] + junkspace - 7*self.ids.b1.height
            if int(self.ids.b2.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b2.pos[1] - Window.size[1]
                self.ids.b2.pos[1] = Window.size[1] + junkspace - 7*self.ids.b2.height
            if int(self.ids.b3.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b3.pos[1] - Window.size[1]
                self.ids.b3.pos[1] = Window.size[1] + junkspace - 7*self.ids.b3.height
            if int(self.ids.b4.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b4.pos[1] - Window.size[1]
                self.ids.b4.pos[1] = Window.size[1] + junkspace - 7*self.ids.b4.height
            if int(self.ids.b5.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b5.pos[1] - Window.size[1]
                self.ids.b5.pos[1] = Window.size[1] + junkspace - 7*self.ids.b5.height
            if int(self.ids.b6.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b6.pos[1] - Window.size[1]
                self.ids.b6.pos[1] = Window.size[1] + junkspace - 7*self.ids.b6.height
        else:
            self.lock.acquire()
            self.sf1 = 1
            self.ids.b0.pos[1] -= self.speed
            self.ids.b1.pos[1] -= self.speed
            self.ids.b2.pos[1] -= self.speed
            self.ids.b3.pos[1] -= self.speed
            self.ids.b4.pos[1] -= self.speed
            self.ids.b5.pos[1] -= self.speed
            self.ids.b6.pos[1] -= self.speed
            self.sf1 = 0
            self.lock.release()
            if int(self.ids.b0.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b0.pos[1]
                self.ids.b0.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b1.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b1.pos[1]
                self.ids.b1.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b2.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b2.pos[1]
                self.ids.b2.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b3.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b3.pos[1]
                self.ids.b3.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b4.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b4.pos[1]
                self.ids.b4.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b5.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b5.pos[1]
                self.ids.b5.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b6.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b6.pos[1]
                self.ids.b6.pos[1] = Window.size[1] - junkspace

    def s2(self,uknwn):
        if self.c2 == 0:
            self.lock.acquire()
            self.sf2 = 1
            self.ids.b9.pos[1] += self.speed
            self.ids.b10.pos[1] += self.speed
            self.ids.b7.pos[1] += self.speed
            self.ids.b8.pos[1] += self.speed
            self.ids.b11.pos[1] += self.speed
            self.ids.b12.pos[1] += self.speed
            self.ids.b13.pos[1] += self.speed
            self.sf2 = 0
            self.lock.release()
            if int(self.ids.b9.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b9.pos[1] - Window.size[1]
                self.ids.b9.pos[1] = Window.size[1] + junkspace - 7*self.ids.b1.height
            if int(self.ids.b10.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b10.pos[1] - Window.size[1]
                self.ids.b10.pos[1] = Window.size[1] + junkspace - 7*self.ids.b1.height
            if int(self.ids.b11.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b11.pos[1] - Window.size[1]
                self.ids.b11.pos[1] = Window.size[1] + junkspace - 7*self.ids.b2.height
            if int(self.ids.b7.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b7.pos[1] - Window.size[1]
                self.ids.b7.pos[1] = Window.size[1] + junkspace - 7*self.ids.b3.height
            if int(self.ids.b8.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b8.pos[1] - Window.size[1]
                self.ids.b8.pos[1] = Window.size[1] + junkspace - 7*self.ids.b4.height
            if int(self.ids.b12.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b12.pos[1] - Window.size[1]
                self.ids.b12.pos[1] = Window.size[1] + junkspace - 7*self.ids.b4.height
            if int(self.ids.b13.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b13.pos[1] - Window.size[1]
                self.ids.b13.pos[1] = Window.size[1] + junkspace - 7*self.ids.b4.height

        else:
            self.lock.acquire()
            self.sf2 = 1
            self.ids.b9.pos[1] -= self.speed
            self.ids.b10.pos[1] -= self.speed
            self.ids.b7.pos[1] -= self.speed
            self.ids.b8.pos[1] -= self.speed
            self.ids.b11.pos[1] -= self.speed
            self.ids.b12.pos[1] -= self.speed
            self.ids.b13.pos[1] -= self.speed
            self.sf2 = 0
            self.lock.release()
            if int(self.ids.b9.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b9.pos[1]
                self.ids.b9.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b10.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b10.pos[1]
                self.ids.b10.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b11.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b11.pos[1]
                self.ids.b11.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b7.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b7.pos[1]
                self.ids.b7.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b8.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b8.pos[1]
                self.ids.b8.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b12.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b12.pos[1]
                self.ids.b12.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b13.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b13.pos[1]
                self.ids.b13.pos[1] = Window.size[1] - junkspace

    def s3(self,uknwn):
        if self.c3 == 0:
            self.lock.acquire()
            self.sf3 = 1
            self.ids.b14.pos[1] += self.speed
            self.ids.b15.pos[1] += self.speed
            self.ids.b16.pos[1] += self.speed
            self.ids.b17.pos[1] += self.speed
            self.ids.b18.pos[1] += self.speed
            self.ids.b19.pos[1] += self.speed
            self.ids.b20.pos[1] += self.speed
            self.sf3 = 0
            self.lock.release()
            if int(self.ids.b14.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b14.pos[1] - Window.size[1]
                self.ids.b14.pos[1] = Window.size[1] + junkspace - 7*self.ids.b1.height
            if int(self.ids.b15.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b15.pos[1] - Window.size[1]
                self.ids.b15.pos[1] = Window.size[1] + junkspace - 7*self.ids.b1.height
            if int(self.ids.b16.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b16.pos[1] - Window.size[1]
                self.ids.b16.pos[1] = Window.size[1] + junkspace - 7*self.ids.b2.height
            if int(self.ids.b17.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b17.pos[1] - Window.size[1]
                self.ids.b17.pos[1] = Window.size[1] + junkspace - 7*self.ids.b3.height
            if int(self.ids.b18.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b18.pos[1] - Window.size[1]
                self.ids.b18.pos[1] = Window.size[1] + junkspace -7*self.ids.b4.height
            if int(self.ids.b19.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b19.pos[1] - Window.size[1]
                self.ids.b19.pos[1] = Window.size[1] + junkspace -7*self.ids.b4.height
            if int(self.ids.b20.pos[1]) >= int(Window.size[1]):
                junkspace = self.ids.b20.pos[1] - Window.size[1]
                self.ids.b20.pos[1] = Window.size[1] + junkspace -7*self.ids.b4.height
        else:
            self.lock.acquire()
            self.sf3 = 1
            self.ids.b14.pos[1] -= self.speed
            self.ids.b15.pos[1] -= self.speed
            self.ids.b16.pos[1] -= self.speed
            self.ids.b17.pos[1] -= self.speed
            self.ids.b18.pos[1] -= self.speed
            self.ids.b19.pos[1] -= self.speed
            self.ids.b20.pos[1] -= self.speed
            self.sf3 = 0
            self.lock.release()
            if int(self.ids.b14.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b14.pos[1]
                self.ids.b14.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b15.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b15.pos[1]
                self.ids.b15.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b16.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b16.pos[1]
                self.ids.b16.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b17.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b17.pos[1]
                self.ids.b17.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b18.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b18.pos[1]
                self.ids.b18.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b19.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b19.pos[1]
                self.ids.b19.pos[1] = Window.size[1] - junkspace
            if int(self.ids.b20.pos[1]) <= int(Window.size[1]-7*self.ids.b1.height):
                junkspace = Window.size[1]-7*self.ids.b1.height - self.ids.b20.pos[1]
                self.ids.b20.pos[1] = Window.size[1] - junkspace
    def fixpointloc(self):
        #range of each 9 cells
        #x-axis size(min), y-axis size(min), x-axis size(max), y-axix size(max)
        #starting from upper to right = r1,middle to right = r2,end to right = r3
        global cd
        if cd == 1:
            c1_ = (self.ids.b1.pos[0],self.ids.b1.pos[1],self.ids.b1.pos[0]+self.ids.b1.size[0],self.ids.b1.pos[1]+self.ids.b1.size[1])
            c2_ = (self.ids.b8.pos[0],self.ids.b8.pos[1],self.ids.b8.pos[0]+self.ids.b8.size[0],self.ids.b8.pos[1]+self.ids.b8.size[1])
            c3_ = (self.ids.b15.pos[0],self.ids.b15.pos[1],self.ids.b15.pos[0]+self.ids.b15.size[0],self.ids.b15.pos[1]+self.ids.b15.size[1])
            c4 = (self.ids.b2.pos[0],self.ids.b2.pos[1],self.ids.b2.pos[0]+self.ids.b2.size[0],self.ids.b2.pos[1]+self.ids.b2.size[1])
            c5 = (self.ids.b9.pos[0],self.ids.b9.pos[1],self.ids.b9.pos[0]+self.ids.b9.size[0],self.ids.b9.pos[1]+self.ids.b9.size[1])
            c6 = (self.ids.b16.pos[0],self.ids.b16.pos[1],self.ids.b16.pos[0]+self.ids.b16.size[0],self.ids.b16.pos[1]+self.ids.b16.size[1])
            c7 = (self.ids.b3.pos[0],self.ids.b3.pos[1],self.ids.b3.pos[0]+self.ids.b3.size[0],self.ids.b3.pos[1]+self.ids.b3.size[1])
            c8 = (self.ids.b10.pos[0],self.ids.b10.pos[1],self.ids.b10.pos[0]+self.ids.b10.size[0],self.ids.b10.pos[1]+self.ids.b10.size[1])
            c9 = (self.ids.b17.pos[0],self.ids.b17.pos[1],self.ids.b17.pos[0]+self.ids.b17.size[0],self.ids.b17.pos[1]+self.ids.b17.size[1])
            cd = 0
            self.ccc = [c1_,c2_,c3_,c4,c5,c6,c7,c8,c9]
        
    def scorecalc(self):
        global clev,plev,llock,skp1
        #print("self.c1= ",self.c1_,"\nself.c2= ",self.c2_,"\nself.c3= ",self.c3_,"\nself.c4= ",self.c4,"\nself.c5= ",self.c5,"\nself.c6= ",self.c6,"\nself.c7= ",self.c7,"\nself.c8= ",self.c8,"\nself.c9= ",self.c9)        
        #aproxx. positions after run of every item
        pt0 = (self.ids.b0,self.ids.b0.pos[0]+self.ids.b0.size[0]/2,self.ids.b0.pos[1]+self.ids.b0.size[1]/2)
        pt1 = (self.ids.b1,self.ids.b1.pos[0]+self.ids.b1.size[0]/2,self.ids.b1.pos[1]+self.ids.b1.size[1]/2)
        pt2 = (self.ids.b2,self.ids.b2.pos[0]+self.ids.b2.size[0]/2,self.ids.b2.pos[1]+self.ids.b2.size[1]/2)
        pt3 = (self.ids.b3,self.ids.b3.pos[0]+self.ids.b3.size[0]/2,self.ids.b3.pos[1]+self.ids.b3.size[1]/2)
        pt4 = (self.ids.b4,self.ids.b4.pos[0]+self.ids.b4.size[0]/2,self.ids.b4.pos[1]+self.ids.b4.size[1]/2)
        pt5 = (self.ids.b5,self.ids.b5.pos[0]+self.ids.b5.size[0]/2,self.ids.b5.pos[1]+self.ids.b5.size[1]/2)
        pt6 = (self.ids.b6,self.ids.b6.pos[0]+self.ids.b6.size[0]/2,self.ids.b6.pos[1]+self.ids.b6.size[1]/2)
        pt7 = (self.ids.b7,self.ids.b7.pos[0]+self.ids.b7.size[0]/2,self.ids.b7.pos[1]+self.ids.b7.size[1]/2)
        pt8 = (self.ids.b8,self.ids.b8.pos[0]+self.ids.b8.size[0]/2,self.ids.b8.pos[1]+self.ids.b8.size[1]/2)
        pt9 = (self.ids.b9,self.ids.b9.pos[0]+self.ids.b9.size[0]/2,self.ids.b9.pos[1]+self.ids.b9.size[1]/2)
        pt10 = (self.ids.b10,self.ids.b10.pos[0]+self.ids.b10.size[0]/2,self.ids.b10.pos[1]+self.ids.b10.size[1]/2)
        pt11 = (self.ids.b11,self.ids.b11.pos[0]+self.ids.b11.size[0]/2,self.ids.b11.pos[1]+self.ids.b11.size[1]/2)
        pt12 = (self.ids.b12,self.ids.b12.pos[0]+self.ids.b12.size[0]/2,self.ids.b12.pos[1]+self.ids.b12.size[1]/2)
        pt13 = (self.ids.b13,self.ids.b13.pos[0]+self.ids.b13.size[0]/2,self.ids.b13.pos[1]+self.ids.b13.size[1]/2)
        pt14 = (self.ids.b14,self.ids.b14.pos[0]+self.ids.b14.size[0]/2,self.ids.b14.pos[1]+self.ids.b14.size[1]/2)
        pt15 = (self.ids.b15,self.ids.b15.pos[0]+self.ids.b15.size[0]/2,self.ids.b15.pos[1]+self.ids.b15.size[1]/2)
        pt16 = (self.ids.b16,self.ids.b16.pos[0]+self.ids.b16.size[0]/2,self.ids.b16.pos[1]+self.ids.b16.size[1]/2)
        pt17 = (self.ids.b17,self.ids.b17.pos[0]+self.ids.b17.size[0]/2,self.ids.b17.pos[1]+self.ids.b17.size[1]/2)
        pt18 = (self.ids.b18,self.ids.b18.pos[0]+self.ids.b18.size[0]/2,self.ids.b18.pos[1]+self.ids.b18.size[1]/2)
        pt19 = (self.ids.b19,self.ids.b19.pos[0]+self.ids.b19.size[0]/2,self.ids.b19.pos[1]+self.ids.b19.size[1]/2)
        pt20 = (self.ids.b20,self.ids.b20.pos[0]+self.ids.b20.size[0]/2,self.ids.b20.pos[1]+self.ids.b20.size[1]/2)

        ptl = [pt0,pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8,pt9,pt10,pt11,pt12,pt13,pt14,pt15,pt16,pt17,pt18,pt19,pt20]
        del pt0,pt1,pt2,pt3,pt4,pt5,pt6,pt7,pt8,pt9,pt10,pt11,pt12,pt13,pt14,pt15,pt16,pt17,pt18,pt19,pt20

        r2 = []

        #print(*self.ccc, sep = "\n")
        #print(*ptl, sep = "\n")
        #print()
        cd_ = 1
        for i in self.ccc:
            for j in ptl:
                #print(j[1]," = ",i[0],"\n",j[1]," = ",i[2],"\n",j[2]," = ",i[1],"\n",j[2]," = ",i[3])
                if j[1] > i[0] and j[1] < i[2] and j[2] > i[1] and j[2] < i[3]:
                    if cd_ <= 6 and cd_ > 3:
                        r2.append(j[0])
            cd_ += 1

        score = 0
        sd = {"./ImData/A.PNG":2000,"./ImData/H.PNG":2000,"./ImData/O.PNG":2000,"./ImData/V.PNG":2000,"./ImData/B.PNG":1000,"./ImData/I.PNG":1000,"./ImData/P.PNG":1000,"./ImData/W.PNG":1000,"./ImData/C.PNG":750,"./ImData/J.PNG":750,"./ImData/Q.PNG":750,"./ImData/X.PNG":750,"./ImData/D.PNG":500,"./ImData/K.PNG":500,"./ImData/R.PNG":500,"./ImData/Y.PNG":500,"./ImData/E.PNG":100,"./ImData/L.PNG":100,"./ImData/S.PNG":100,"./ImData/Z.PNG":100,"./ImData/F.PNG":50,"./ImData/M.PNG":50,"./ImData/T.PNG":50,"./ImData/A1.PNG":50,"./ImData/G.PNG":0,"./ImData/N.PNG":0,"./ImData/U.PNG":0,"./ImData/B2.PNG":0}
        #print(r2[0].source, r2[1].source, r2[2].source)
        if r2[0].source == r2[1].source == r2[2].source:
            score += sd[r2[2].source]
            self.ids.trys.text = str(int(self.ids.trys.text) + int(sd[r2[2].source]/100))
        elif r2[0].source == r2[1].source:
            score += int(sd[r2[1].source]/2)
        elif r2[1].source == r2[2].source:
            score += int(sd[r2[2].source]/2)
        elif r2[0].source == r2[2].source:
            score += int(sd[r2[2].source]/2)

        self.ids.scrs.text = str(int(self.ids.scrs.text) + score)

        #print(score)

        #Level Clear Case Handler
        if int(self.ids.target.text) < int(self.ids.scrs.text):
            self.ids.lev.text = str(int(self.ids.lev.text) + 1)
            self.ids.target.text = str(int(self.ids.target.text) + 2000*int(self.ids.lev.text))
            self.ids.trys.text = str(int(self.ids.trys.text) + 1 + int(self.ids.lev.text)*10)

            #Level Update
            clev = self.ids.lev.text
        
        #Level Fail Handler when Level > 1
        if (int(self.ids.target.text) > int(self.ids.scrs.text)) and (int(self.ids.trys.text) == 1):
            self.ids.target.text = str(int(self.ids.target.text) - 2000*int(self.ids.lev.text))
            self.ids.lev.text = str(int(self.ids.lev.text) - 1)
            self.ids.trys.text = 1 + int(self.ids.lev.text)*10
            self.ids.scrs.text = str(int(self.ids.target.text) - 2000*(int(self.ids.lev.text)-1))
        
        #Chances Minus on Each Spin
        self.ids.trys.text = str(int(self.ids.trys.text) - 1)
        
        #Level Fail Handler when Level > 1
        if self.ids.lev.text == "1" and int(self.ids.trys.text) < 1:
            self.ids.scrs.text = "0"
            self.ids.trys.text = "10"
        self.ids.pgpow.value = 1
        self.ids.g1.color = (0,0,0)
        self.ids.g2.color = (0,0,0)
        self.ids.g3.color = (0,0,0)

        #If Current Level Is not Same as Previous one ...
        if plev != clev:
            llock = 0
            skp1 = 1
        #print(plev,clev,llock)
        #... then images will change according to Level
        if int(self.ids.lev.text) - 1 % 4 == 0:
            if skp1 == 1 and llock == 0:
                data = ["A","B","C","D","E","F","G"]
                self.change(data)
                skp1 = 0
                llock = 1
        elif int(self.ids.lev.text) - 1 % 4 == 1:
            if llock == 0:
                data = ["H","I","J","K","L","M","N"]
                self.change(data)
                llock = 1
        elif int(self.ids.lev.text) - 1 % 4 == 2:
            if llock == 0:
                data = ["O","P","Q","R","S","T","U"]
                self.change(data)
                llock = 1
        elif int(self.ids.lev.text) - 1 % 4 == 3:
            if llock == 0:
                data = ["V","W","X","Y","Z","A1","B2"]
                self.change(data)
                llock = 1
        plev = clev
    
    def change(self,data):

        #Changing Images on Level Change
        #print(self.ids)
        self.ids.b0.source = f"./ImData/{data[0]}.PNG"
        self.ids.b1.source = f"./ImData/{data[1]}.PNG"
        self.ids.b2.source = f"./ImData/{data[2]}.PNG"
        self.ids.b3.source = f"./ImData/{data[3]}.PNG"
        self.ids.b4.source = f"./ImData/{data[4]}.PNG"
        self.ids.b5.source = f"./ImData/{data[5]}.PNG"
        self.ids.b6.source = f"./ImData/{data[6]}.PNG"
        
        self.ids.b7.source = f"./ImData/{data[0]}.PNG"
        self.ids.b8.source = f"./ImData/{data[1]}.PNG"
        self.ids.b9.source = f"./ImData/{data[2]}.PNG"
        self.ids.b10.source = f"./ImData/{data[3]}.PNG"
        self.ids.b11.source = f"./ImData/{data[4]}.PNG"
        self.ids.b12.source = f"./ImData/{data[5]}.PNG"
        self.ids.b13.source = f"./ImData/{data[6]}.PNG"
        
        self.ids.b14.source = f"./ImData/{data[0]}.PNG"
        self.ids.b15.source = f"./ImData/{data[1]}.PNG"
        self.ids.b16.source = f"./ImData/{data[2]}.PNG"
        self.ids.b17.source = f"./ImData/{data[3]}.PNG"
        self.ids.b18.source = f"./ImData/{data[4]}.PNG"
        self.ids.b19.source = f"./ImData/{data[5]}.PNG"
        self.ids.b20.source = f"./ImData/{data[6]}.PNG"

        #Setting Up Positions Of Each Block on Level Change
        self.ids.b0.pos = (0, Window.size[1])
        self.ids.b1.pos = (0, Window.size[1] - self.ids.b0.size[1] * 1)
        self.ids.b2.pos = (0, Window.size[1] - self.ids.b0.size[1] * 2)
        self.ids.b3.pos = (0, Window.size[1] - self.ids.b0.size[1] * 3)
        self.ids.b4.pos = (0, Window.size[1] - self.ids.b0.size[1] * 4)
        self.ids.b5.pos = (0, Window.size[1] - self.ids.b0.size[1] * 5)
        self.ids.b6.pos = (0, Window.size[1] - self.ids.b0.size[1] * 6)

        self.ids.b7.pos = (self.ids.b0.size[0], Window.size[1])
        self.ids.b8.pos = (self.ids.b0.size[0], Window.size[1] - self.ids.b0.size[1] * 1)
        self.ids.b9.pos = (self.ids.b0.size[0], Window.size[1] - self.ids.b0.size[1] * 2)
        self.ids.b10.pos = (self.ids.b0.size[0], Window.size[1] - self.ids.b0.size[1] * 3)
        self.ids.b11.pos = (self.ids.b0.size[0], Window.size[1] - self.ids.b0.size[1] * 4)
        self.ids.b12.pos = (self.ids.b0.size[0], Window.size[1] - self.ids.b0.size[1] * 5)
        self.ids.b13.pos = (self.ids.b0.size[0], Window.size[1] - self.ids.b0.size[1] * 6)

        self.ids.b14.pos = (self.ids.b0.size[0] * 2, Window.size[1])
        self.ids.b15.pos = (self.ids.b0.size[0] * 2, Window.size[1] - self.ids.b0.size[1] * 1)
        self.ids.b16.pos = (self.ids.b0.size[0] * 2, Window.size[1] - self.ids.b0.size[1] * 2)
        self.ids.b17.pos = (self.ids.b0.size[0] * 2, Window.size[1] - self.ids.b0.size[1] * 3)
        self.ids.b18.pos = (self.ids.b0.size[0] * 2, Window.size[1] - self.ids.b0.size[1] * 4)
        self.ids.b19.pos = (self.ids.b0.size[0] * 2, Window.size[1] - self.ids.b0.size[1] * 5)
        self.ids.b20.pos = (self.ids.b0.size[0] * 2, Window.size[1] - self.ids.b0.size[1] * 6)


class Casino(App):
    pass


cd = 1
skp1 = 0 #For 1st Time when Level Starts
llock = 1 #1 = Lock and 0 = Unlock (Lock on same and  Unlock on Diff)

clev = 1
plev = 1



Casino().run()
