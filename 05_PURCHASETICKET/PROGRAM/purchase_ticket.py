def purchase_ticket(status:str, fare:int, buffer:int):
    dic = {'Infant':None, 'Student':0.5, 'Normal':None, 'Pensioner':0.3, 'Disable':0.3, 'Default':None}
    actual_fare = -1

    for key in dic.keys():
        if(status == key and dic[key]!=None):
            actual_fare = fare - fare*dic[key]
            buffer = buffer - actual_fare
            return (actual_fare, buffer)
        elif(status == 'Normal'):
            actual_fare = fare
            buffer = buffer - actual_fare
            return (actual_fare, buffer)
        elif(status == 'Infant'):
            actual_fare = 0
            return (actual_fare, buffer)
        elif(status == 'Default'):
            return (actual_fare, buffer)

"""        
if __name__ == "__main__":
    print(purchase_ticket('Infant',2048,1024))
"""