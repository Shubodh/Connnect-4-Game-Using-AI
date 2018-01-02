from turtle import*
    


def draw_board():
    #Drawing the board
    delay(0)

    color('Red') 
    pu()    
    goto(0,-20)
    pd()
    
    fd(240)

    pu()    
    goto(0,0)
    pd()

    color('Black')
    
    lt(270)

    for i in range(0,4):
        lt(90)
        fd(240)

    lt(180)
    fd(240)
    lt(180)

    for j in range(0,4):
        lt(90)
        fd(240)
        lt(180)
        fd(240)
        lt(90)
        fd(60)

    lt(180)
    fd(240)
    lt(180)

    for k in range(0,2):
        lt(90)
        fd(60)
        lt(270)
        fd(240)
        lt(90)
        fd(60)    
        lt(90)
        fd(240)
        lt(180)


    pu()    
    goto(0,0)
    pd()
    lt(90)





def gui_action_computerTurn(A,j):
    
    
    
    i = finding_row(A,j)
    pu()
    setpos(i*60,j*60)
    pd()
    color('Blue') 
    pu()
    fd(30)
    pd()

    begin_fill()
    circle(30)
    end_fill()

def gui_action_humanTurn(A,j):
    
    
    
    i = finding_row(A,j)
    pu()
    setpos(i*60,j*60)
    pd()
    color('Green') 
    pu()
    fd(30)
    pd()

    begin_fill()
    circle(30)
    end_fill()

    
    
draw_board()   
gui_action_humanTurn(2)


done()

