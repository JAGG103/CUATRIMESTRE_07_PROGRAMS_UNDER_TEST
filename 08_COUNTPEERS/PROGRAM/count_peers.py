def count_peers(number: int)->int:
    count = 0
    if(number<=0):
        count = -1
    else:
        for i in range(1,number+1):
            if(i%2==0):
                count +=1
            
    return count


# if(__name__=="__main__"):
#     print(count_peers(-10)) 
#     print(count_peers(1)) 
#     print(count_peers(52))
