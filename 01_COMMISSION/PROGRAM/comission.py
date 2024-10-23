def commission(a,b,c):
    if(a*45+b*30+c*25<=1000):
        q=(a*45+b*30+c*25)*0.10
    elif(a*45+b*30+c*25<1800):
        q=100+((a*45+b*30+c*25)-1000)*0.15
    else:
        q=220+((a*45+b*30+c*25)-1800)*0.20
    return q
    
# if __name__=='__main__':
#     print(commission(1, 15, 14))