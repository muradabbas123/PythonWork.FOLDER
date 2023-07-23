#include_python
enter_number = input("write number : ")
converstion_number = input("select what to convert from : 'c=centimetertometer', m=metertocentimeter, mi=miletometer, mm=metertomillimeter ")                                       
enter_number = int(enter_number)
if converstion_number == 'c':
    converted = enter_number // 100
    print ('len in meters : ' + str(converted) )
elif converstion_number == 'm':
    converted = enter_number *  100
    print('len in centimeters :' + str(converted) )
elif converstion_number == 'mi':
    converted = enter_number * 1600 
    print(" =} len converted to meters from mile : " + str(converted) ) 
elif converstion_number == 'mm':
    converted = enter_number * 1000
    print('len in millimeters : ' + str(converted)) 




    




