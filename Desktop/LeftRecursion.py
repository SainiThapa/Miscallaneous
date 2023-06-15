CFG = input("Enter the CFG: ")
beta=''
if('->' in CFG):    
    tokens = CFG.split("->")
    
    rightstr=tokens[1].split("|")
    length=len(rightstr[0])
    if(rightstr[0][0]==tokens[0]):
            a=(tokens[0]+'->'+rightstr[1]+tokens[0]+"'")

            rhs =[rightstr[0][i] for i in range(1,length)]
            
            for x in rhs: 
                beta+=x                 
            b=(tokens[0]+"'->"+beta+tokens[0]+"'")
            print(a)
            if(a!=b):
                print(b)
            if rightstr[1].isupper() == True:
                print(rightstr[1]+"->"+"$")
    else:
        print("No Left recursion")
    # print(rightstr[0][0])
else:
    print("Enter a valid Context Free Grammar")