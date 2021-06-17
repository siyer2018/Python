###########################################################################
### COP 4045 - Python Programming - Dr. Oge Marques - FAU - Summer 2021 ###
###            Assignment 4:  Fuel Consumption       ###
###              Sharmada Iyer - Z23479365   DUE:6/17/21                   ###
###########################################################################


import csv #import CSV for csv.reader
import pylab #import pylab for plotting

print("\n\n\n--------> Vehicle Fuel Consumption Information <--------\n") #INTRODUCTION AND INSTRUCTIONS FOR USERS

print("\n\n\nSelect (1) to check out the vehicles that are within your choice of mile range. ")
print("Select (2) to plot a trend line for either City, Highway, or Overall MPG. You may choose to display the results or store them in a file")
print("Select (0) to exit the program")


#Function: Create Mileage List
#Description: This function will read the file as a CSV and extract the important information
def create_mileage_list(mpgfile):
    mileage_list=[] #declare mileage list
    epafile=csv.reader(mpgfile) #csv reader function
    for line_list in epafile: #line list inside of the csv read file
        
        if line_list[70]=='car': #Only Cars
            car_tuple=(line_list[2],line_list[3],int(line_list[10])) #Create a tuple and extract the necessary information (Make, Model, MPG (HWY))
            mileage_list.append(car_tuple) #append each car tuple into the mileage list
    return mileage_list #return the list 


#Function: MPG Interval Filter
#Description: This function will extract the cars that are within the user's given range.
def mpginterval_filter(minval,maxval,mpglist): 

    range_list=[] #declare a range list
    for car_tuple in mpglist: #tuples inside of the mpglist
        if car_tuple[2]>=minval and car_tuple[2]<=maxval: #cars in the user's range
            range_list.append(car_tuple) #append the cars into the range list
        
            

    return range_list #return the range list
     
#Function: Create Trend List
#Description: This function will gather the necessary x and y coordinates based on the user's input.
def create_trend_list(userinput,trendfile):
    x,y=[],[] #declare x and y
    ftrend=csv.reader(trendfile) #csv reader
    next(ftrend) #ignore the header line of CSV

    if userinput=='H': #Highway
       for line_lst in ftrend:
            x.append(line_lst[0]) #Append Year
            y.append(float(line_lst[6])) #Highway MPG
    elif userinput=='C': #City
        for line_lst in ftrend:          
          x.append(line_lst[0]) #Append Year
          y.append(float(line_lst[5]))  #City MPG
    elif userinput=='O': #Overall
        for line_lst in ftrend:            
            x.append(line_lst[0]) #Append Year
            y.append(float(line_lst[4]))  #Overall MPG

    else: #Any other input
       print("Invalid input") #Invalid input
       x.append(int(0)) # 0
       y.append(float(0)) #0
    
    return x,y #return the coordinates
    


    


    
    






option=int(input("\n Please select '1' for Mileage Info, '2' for Trend Plot, or '0' to exit: ")) #Selecting an input
mpglist=[] #Declaring MPG list

while option!=0: #as long as no exit
    
    if (option==1): #Option 1
        mpgfile=open("epadata2015.csv","r") #open file in read mode
        mpglist=create_mileage_list(mpgfile)  #Create mileage list function called     
        
        min_input=int(input("\n\n Enter the miminum MPG Interval: ")) #Enter a minimum value
        max_input=int(input("\n\n Enter the maximum MPG Interval: ")) #Enter a maximum value

        if min_input>max_input: #If the minimun is greater than maximum
            print("That is an invalid input.") #Display invalid input to user

        else:
            range_values=mpginterval_filter(min_input,max_input,mpglist)  #get the cars with the range values
            print("The following cars fall within the given range: ") #Print message
            for car_tuple in range_values: #traverse through list
                print(" ", car_tuple[0],car_tuple[1]) #display the results

        mpgfile.close() #close file

        
        
        
        
      

        

    elif (option==2): #Option 2

        x,y=[],[] # declare x and y 
        
        
        trendOption=input("\n\nEnter 'H' for Highway MPG, 'C' for City MPG, 'O' for the Overall MPG, or 'X' to exit: ") #Select MPG or Quit
        trendOption=trendOption.upper() #all results are converted to uppercase

        
        while trendOption!='X': #Whole the user does not quit
            trendfile=open("epadata2020.csv","r") #open trend file
            if trendOption=='H':  #Highway
                x,y=create_trend_list(trendOption,trendfile) #Create trend based on highway
                trendfile.close() #close file

                pylab.plot(x,y) #Plot
                pylab.ylabel("Highway MPG") #Y Label
                pylab.xlabel("Year") #X Label
                pylab.title("Trendline: Highway MPG by year") #Title

            elif trendOption == 'C': #City
                x,y=create_trend_list(trendOption,trendfile) #Create trend based on city
                trendfile.close() #close file

                pylab.plot(x,y) #Plot
                pylab.ylabel("City MPG") #Y Label
                pylab.xlabel("Year") #X Label
                pylab.title("Trendline: City MPG by year") #Title

            elif trendOption == 'O': 
                x,y=create_trend_list(trendOption,trendfile) #Create trend based on overall
                trendfile.close() #close file

                pylab.plot(x,y) #Plot
                pylab.ylabel("Overall MPG") #Y Label
                pylab.xlabel("Year") #X Label
                pylab.title("Trendline: Overall MPG by year") #Title
        
            else: #Any other input
                print(" You have entered and invalid input. Please try again.")  #display error message
                trendfile.close() #Close file

            userinput=input("\n\n Enter 'D' to display or 'F' to save to file: ") #Display file or Save File
            userinput=userinput.upper() #all results are converted to uppercase

            if userinput=='D': #Display
                pylab.show() #opens trend plot application
            
            elif userinput=='F': #File
                pylab.savefig("epa_plot.png") #Save to file, modifies if new trend line is created

            else:
                print("Invalid Input.") #Error message



            trendOption=input("\n\nEnter 'H' for Highway MPG, 'C' for City MPG, 'O' for the Overall MPG, or 'X' to exit: ") #Asks user if they would like to try again
            trendOption=trendOption.upper() #all results are converted to uppercase
            

    else:
        print(" You have entered and invalid input. Please try again.") #Invalid input error message

    

    







    option=int(input("Please select '1' for Mileage Info, '2' for Trend Plot, or '0' to exit: ")) #Asks user if they would like to try again
