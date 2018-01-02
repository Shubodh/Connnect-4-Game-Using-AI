
# coding: utf-8

# In[ ]:


from sys import maxsize 
import copy
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
    i = finding_row(A,j) - 1    
    if i < 0:
        i = 3
        pu()
        setpos(j*60,i*60)
        pd()
        color('Blue') 
        pu()
        fd(30)
        pd()

        begin_fill()
        circle(30)
        end_fill()        
        
    else: 
        i = finding_row(A,j) - 1
        pu()
        setpos(j*60,i*60)
        pd()
        color('Blue') 
        pu()
        fd(30)
        pd()

        begin_fill()
        circle(30)
        end_fill()

def gui_action_humanTurn(A,j):
    i = finding_row(A,j) - 1    
    if i < 0:    
    
        i = 3
        pu()
        setpos(j*60,i*60)
        pd()
        color('Green') 
        pu()
        fd(30)
        pd()

        begin_fill()
        circle(30)
        end_fill()

    else:
        i = finding_row(A,j) - 1
        pu()
        setpos(j*60,i*60)
        pd()
        color('Green') 
        pu()
        fd(30)
        pd()

        begin_fill()
        circle(30)
        end_fill()




# In[ ]:


A = [[0 for i in range(4)] for j in range(4)]

#Defining the possible actions
def possible_actions(A):
    actions = []    
    for j in range(0,4):
        for i in range(0,4):
            if A[i][j] == 0: 
                actions.append(j)
                break 
    return actions

#Defining the result states
def finding_row(A,coln):
    row = 0
    for i in range(0,4) :
        if A[i][coln] == 0 :
            row = i
            break
    return row

def result_states(A,playerNum,coln):
    n = coln
    m = finding_row(A,coln)
    A[m][n] = playerNum




def win_state(A):



    for j in range(0,4):
        for i in range(0,2):
            #Change this function for the example below and also add returning 0 
            if (A[i][j] == 1 and A[i+1][j] == 1 and A[i+2][j] == 1):
                return 1
            elif (A[i][j] == 2 and A[i+1][j] == 2 and A[i+2][j] == 2):
                return (-1)

    for j in range(0,2):
        for i in range(0,4):
            if (A[i][j] == 1 and A[i][j+1] == 1 and A[i][j+2] == 1):
                return 1
            elif (A[i][j] == 2 and A[i][j+1] == 2 and A[i][j+2] == 2):
                return (-1)            

    for j in range(0,2):
        for i in range(0,2):    
            if (A[i][j] == 1 and A[i+1][j+1] == 1 and A[i+2][j+2] == 1):
                return (1)
            elif (A[i][j] == 2 and A[i+1][j+1] == 2 and A[i+2][j+2] == 2):
                return (-1)
            elif (A[3-i][j] == 1 and A[2-i][j+1] == 1 and A[1-i][j+2] == 1):
                return (1)
            elif (A[3-i][j] == 2 and A[2-i][j+1] == 2 and A[1-i][j+2] == 2):
                return (-1)

    
    flag = False
    for a in A:
        if 0 in a:
            flag = True
            break
    if flag:
        return -2
    else:
        return 0






# In[3]:


#Defining the minimax algorithm


def minimax_decision(A):
    
    actions = possible_actions(A)
    abc = []
    for action in actions:
        a = copy.deepcopy(A)
        result_states(a,1,action)
        v = min_value(a)
        abc.append((v,action))
    
    return max(abc)[1]
    
def max_value(A):
    x = win_state(A)
    if x == -1:
        return -1
    elif x == 1:
        return 1
    elif x == 0:
        return 0
    
    v = - 10
    actions = possible_actions(A)
    for action in actions:
        a = copy.deepcopy(A)
        result_states(a,1,action)
        v = max(v,min_value(a))
    return v
        
def min_value(A):
    x = win_state(A)
    if x == -1:
        return -1
    elif x == 1:
        return 1
    elif x == 0:
        return 0
    
    v = 10
    actions = possible_actions(A)
    for action in actions:
        a = copy.deepcopy(A)
        result_states(a,2,action)
        v = min(v,max_value(a))

    return v
    


# In[4]:


#Defining the alpha-beta pruning algorithm

alpha = -10
beta = 10

def alpha_beta_search(A,alpha,beta):
    
    actions = possible_actions(A)
    abc = []
    for action in actions:
        a = copy.deepcopy(A)
        result_states(a,1,action)
        v = min_value_new(a,alpha,beta)
        abc.append((v,action))
       
    return max(abc)[1]
    
def max_value_new(A,alpha,beta):
    x = win_state(A)
    if x == -1:
        return -1
    elif x == 1:
        return 1
    elif x == 0:
        return 0
    
    v = - 10
    actions = possible_actions(A)
    
    for action in actions:
        a = copy.deepcopy(A)
        result_states(a,1,action)
        v = max(v,min_value_new(a,alpha,beta))
        if v >= beta:
            return v
        alpha = max(alpha,v)
    return v
        
def min_value_new(A,alpha,beta):
    x = win_state(A)
    if x == -1:
        return -1
    elif x == 1:
        return 1
    elif x == 0:
        return 0
    
    v = 10
    actions = possible_actions(A)
    for action in actions:
        a = copy.deepcopy(A)
        result_states(a,2,action)
        v = min(v,max_value_new(a,alpha,beta))
        if v <= alpha:
            return v
        beta = min(beta,v)        
    return v
    


# In[ ]:


A = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

draw_board()
print("Valid entry values: 0,1,2,3")
for y in range(0,16):
    if win_state(A) == (1):
        print("You have lost, game over")
        break
    elif win_state(A) == (-1):
        print("You have won")
        break
    elif y%2 == 0:
        j = minimax_decision(A)
        result_states(A,1,j)
        gui_action_computerTurn(A,j)
    else:
        a = raw_input('Enter a move')
        a = int(a)
        result_states(A,2,a)
        gui_action_humanTurn(A,a)
    print(A)

done()

# In[131]:





# In[6]:




    


# In[ ]:




