import threading
from threading import Thread

class Source(Thread):
    best={
    2021:[2.5,6.7,12.5,9.2,4.4,2.5],
    2022:[3.1,7.2,13.1,10.6,4.9,2.9],
    2012:[1.8,4.2,8.6,6.9,2.9,0.98]
}
    def __init__(self,nm="",key=0):
        Thread.__init__(self)
        self.name=nm
        self.key=key
    def run(self):
        print(Thread.getName(self)+" came inside")
        print(threading.currentThread().getName(),self.best[self.key])
        


a=Source("Razak",2021)
b=Source("Rajiya",2020)
c=Source("Mohamed",2012)
a.start()
#a.join()
b.start()
b.join()
c.start()