l = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def updatelist(n,t):
    l[n-1] = t

def refresh():
    
    print( ' '+ l[9] +'  |  '+ l[9]+ '  |  '+ l[9])
    print( ' '+ l[0] +'  |  '+ l[1]+ '  |  '+ l[2])
    print('____|_____|____')
    print( ' '+ l[9] +'  |  '+ l[9]+ '  |  '+ l[9])
    print( ' '+ l[3] +'  |  '+ l[4]+ '  |  '+ l[5])    
    print('____|_____|____')
    print( ' '+ l[9] +'  |  '+ l[9]+ '  |  '+ l[9])
    print( ' '+ l[6] +'  |  '+ l[7]+ '  |  '+ l[8])
    

refresh()
p = ["O","X","O","X","O","X","O","X","O"]     

for i in p:
    t = i
    n= input("go on "+ t + " choose your position")
    n=int(n)
    if l[n-1] == ' ':
        updatelist(n,t)
        refresh()
    else:
        print("you can't do that ")


