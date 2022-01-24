if x in word and x!='':

        count=word.count(x)
        loc=0
        while count==1 or count>1:
            loc=word.find(x,loc)
            list[loc]=x
            loc+=1
            count-=1  
        print('Good choice!')