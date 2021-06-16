###########################################################################
### COP 4045 - Python Programming - Dr. Oge Marques - FAU - Summer 2021 ###
###            Assignment 4:  Fuel Consumption       ###
###              Sharmada Iyer - Z23479365   DUE:6/17/21                   ###
###########################################################################


import csv






print("--------> Vehicle Fuel Consumption Information <--------\n") #INTRODUCTION AND INSTRUCTIONS FOR USERS



def create_mileage_list(mpgfile):
    mileage_list=[]
    epafile=csv.reader(mpgfile)
    for line_list in epafile:
        
        if line_list[70]=='car':
            car_tuple=(line_list[2],line_list[3],int(line_list[10]))
            mileage_list.append(car_tuple)
    return mileage_list         



def mpginterval_filter(minval,maxval,mpglist): 

    range_list=[]
    for car_tuple in mpglist:
        if car_tuple[2]>=minval and car_tuple[2]<=maxval:
            range_list.append(car_tuple)
        
            

    return range_list
     







option=int(input("\n Please select '1' for Mileage Info, '2' for Trend Plot, or '0' to exit: "))
mpglist=[]
while option==1 or option==2:
    
    if (option==1): 
        mpgfile=open("epadata2015.csv","r")
        mpglist=create_mileage_list(mpgfile)       
        
        min_input=int(input("\n\n Enter the miminum MPG Interval: "))
        max_input=int(input("\n\n Enter the maximum MPG Interval: "))

        range_values=mpginterval_filter(min_input,max_input,mpglist)
        print("The following cars fall within the given range: ")
        for car_tuple in range_values:
            print(" ", car_tuple[0],car_tuple[1])

        
        
        
        
      

        

    if (option==2): pass






    option=int(input("Please select '1' for Mileage Info, '2' for Trend Plot, or '0' to exit: "))
