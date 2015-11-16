#[[1,2],[3,4],[5,6],[7,8]]

a=[]
for i in range(4):
    a=a+[[i+1,i+2]]

    
a=[]
for i in range(3):
    a=a+[[2*i+1,2*i+2,2*i+3,2*i+4]]


a=[]
for i in range(3):
    d=[]
    for j in range(1,5):
        d=d+[2*i+j]
    a=a+[d]


from graphics import *
win=graphWin()
win.setCoords(0,0,20,20)
for i in range(3,9):
    cir=Circle(Point(i,i),1)
    cir.draw(win)
    
