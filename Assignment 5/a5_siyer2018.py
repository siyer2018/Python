
###########################################################################
### COP 4045 - Python Programming - Dr. Oge Marques - FAU - Summer 2021 ###
###            Assignment 5:  Iris Data Sets and Dictionaries       ###
###              Sharmada Iyer - Z23479365   DUE:6/17/21                   ###
###########################################################################

import csv



print("\n\n\n--------> Iris Data Set Computation <--------\n") #INTRODUCTION AND INSTRUCTIONS FOR USERS

print("\n\n\nThe Iris flower dataset contains data of 3 iris plants: setosa, virginica and versicolor ")
print("The purpose of this app is to create a dictionary that computes the average of the petal length/width and the sepal length/width.")


fIris=csv.DictReader(open("iris.csv","r"))




def computeAverage(total,count): 
    return (total/count)
   
def printPretty(irisDict):
    print("-----------> Averages <-------------")
    for x in irisDict:
        print("\t",x)
        print("\t-------------")
        for y in irisDict[x]:
           print(y,":\t\t",irisDict[x][y])

        print("\n\n")
    



setosaTotalSL=float(0)
setosaTotalSW=float(0)
setosaTotalPL=float(0)
setosaTotalPW=float(0)

virginicaTotalSL=float(0)
virginicaTotalSW=float(0)
virginicaTotalPL=float(0)
virginicaTotalPW=float(0)

versicolorTotalSL=float(0)
versicolorTotalSW=float(0)
versicolorTotalPL=float(0)
versicolorTotalPW=float(0)

setosaAvgSL=float(0)
setosaAvgSW=float(0)
setosaAvgPL=float(0)
setosaAvgPW=float(0)

virginicaAvglSL=float(0)
virginicaAvgSW=float(0)
virginicaAvgPL=float(0)
virginicaAvgPW=float(0)

versicolorAvgSL=float(0)
versicolorAvgSW=float(0)
versicolorAvgPL=float(0)
versicolorAvgPW=float(0)

setosaCount=int(0)
virginicaCount=int(0)
versicolorCount=int(0)

count=int(0)



for row in fIris:
    if row["species"]=="setosa":
        
        
        setosaTotalSL=setosaTotalSL+float(row["sepal_length"])
        setosaTotalSW=setosaTotalSW+float(row["sepal_width"])
        setosaTotalPL=setosaTotalPL+float(row["petal_length"])
        setosaTotalPW=setosaTotalPW+float(row["petal_width"])
        
        setosaCount=setosaCount+1

       
        
    
    elif row["species"]=="virginica":
        virginicaTotalSL=virginicaTotalSL+float(row["sepal_length"])
        virginicaTotalSW=virginicaTotalSW+float(row["sepal_width"])
        virginicaTotalPL=virginicaTotalPL+float(row["petal_length"])
        virginicaTotalPW=virginicaTotalPW+float(row["petal_width"])

        virginicaCount=virginicaCount+1
    
    elif row["species"]=="versicolor":
        versicolorTotalSL=versicolorTotalSL+float(row["sepal_length"])
        versicolorTotalSW=versicolorTotalSW+float(row["sepal_width"])
        versicolorTotalPL=versicolorTotalPL+float(row["petal_length"])
        versicolorTotalPW=versicolorTotalPW+float(row["petal_width"])

        versicolorCount=versicolorCount+1
    
    else:
        print("\nInvalid Iris")


 
setosaAvgSL=computeAverage(setosaTotalSL,setosaCount)
setosaAvgSW=computeAverage(setosaTotalSW,setosaCount)
setosaAvgPL=computeAverage(setosaTotalPL,setosaCount)
setosaAvgPW=computeAverage(setosaTotalPW,setosaCount)

virginicaAvgSL=computeAverage(virginicaTotalSL,virginicaCount)
virginicaAvgSW=computeAverage(virginicaTotalSW,virginicaCount)
virginicaAvgPL=computeAverage(virginicaTotalPL,virginicaCount)
virginicaAvgPW=computeAverage(virginicaTotalPW,virginicaCount)

versicolorAvgSL=computeAverage(versicolorTotalSL,versicolorCount)
versicolorAvgSW=computeAverage(versicolorTotalSW,versicolorCount)
versicolorAvgPL=computeAverage(versicolorTotalPL,versicolorCount)
versicolorAvgPW=computeAverage(versicolorTotalPW,versicolorCount)

irisDict={
  "setosa":{"sepal_length":round(setosaAvgSL,2),"sepal_width":round(setosaAvgSW,2),"petal_length":round(setosaAvgPL,2),"petal_width":round(setosaAvgPW,2)},
  "virginica":{"sepal_length":round(virginicaAvgSL,2),"sepal_width":round(virginicaAvgSW,2),"petal_length":round(virginicaAvgPL,2),"petal_width":round(virginicaAvgPW,2)},
  "versicolor":{"sepal_length":round(versicolorAvgSL,2),"sepal_width":round(versicolorAvgSW,2),"petal_length":round(versicolorAvgPL,2),"petal_width":round(versicolorAvgPW,2)}
}  

printPretty(irisDict)
        

        
        
        
        




