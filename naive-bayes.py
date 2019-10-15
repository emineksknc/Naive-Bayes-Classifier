import statistics
import numpy as np

def prediction(A,B,C):
    normalization = A + B + C
    first = A/normalization
    second = B/normalization
    third = C/normalization
    
    if (first > second and first >third):
        print("Class of object:Iris-Versicolor")
        
    elif (second > first and second > third):
        print("Class of object:Iris-Setosa")
        
    else:
         print("Class of object:Iris-virginica")
       
        
    
 
    
    
    
def probability(special,total):
    probability = len(special)/total
    return probability
 
    
#gauss normal distribution for continous value
def gauss_normal_distribution(x,mu,sigma):
    normaldist = 1/(sigma * np.sqrt(2 * np.pi)) *np.exp( - (x - mu)**2 / (2 * sigma**2) )
   
    return normaldist

#calculate variance
def variance(list):
    count = 0
    for i in list:
        i = float(i)
        count += i
    mean = count / len(list)

    variance = (statistics.variance(list))
    return mean,variance
    
    
#parsing file to lists
def  parse_file(file,num):
    Iris_Setosa = []
    Iris_versicolor = []
    Iris_virginica = []

    for info in file:
        info = info.split(",")
        if (info[4] == "Iris-versicolor\n"):
            Iris_versicolor.append(float(info[num]))

        if (info[4] == "Iris-setosa\n"):
            Iris_Setosa.append(float(info[num]))

        if (info[4] == "Iris-virginica\n"):
            Iris_virginica.append(float(info[num]))

    return Iris_versicolor,Iris_Setosa,Iris_virginica

def train(st, nd, rd, th):
    
    #read file
    file = open("iris.txt","r")
    file = file.readlines()     

    #iv = iris-versicolor, is = iris-setosa ivi = iris-virginica                
    #calculation mean and variance for 1st attribute
    iv1,is1,ivi1 = parse_file(file,0)  
    mean_iv1 , variance_iv1 = variance(iv1)
    mean_is1 , variance_is1 = variance(is1)
    mean_ivi1 , variance_ivi1 = variance(ivi1)
    
 
    
    #calculation mean and variance for 2nd attribute
    iv2,is2,ivi2 = parse_file(file,1) 
    mean_iv2 , variance_iv2 = variance(iv2)
    mean_is2 , variance_is2 = variance(is2)
    mean_ivi2 , variance_ivi2 = variance(ivi2)
  
   

    #calculation mean and variance for 3rd attribute
    
    iv3,is3,ivi3 = parse_file(file,2) 
    mean_iv3 , variance_iv3 = variance(iv3)
    mean_is3 , variance_is3 = variance(is3)
    mean_ivi3 , variance_ivi3 = variance(ivi3)
  
    #calculation mean and variance for 4th attribute
        
    iv4,is4,ivi4 = parse_file(file,3)   
    mean_iv4 , variance_iv4 = variance(iv4)
    mean_is4 , variance_is4 = variance(is4)
    mean_ivi4 , variance_ivi4 = variance(ivi4)
    
    total = len(iv1)+len(is1)+len(ivi1)
    #probabilities of class
    p_ivtotal = probability(iv1,total)
    p_istotal = probability(is1,total)
    p_ivitotal = probability(ivi1,total)
    
    #probabilities of 1st class for attributes
    p_iv1 = gauss_normal_distribution(st,mean_iv1 , variance_iv1)
    p_iv2 = gauss_normal_distribution(nd,mean_iv2 , variance_iv2)
    p_iv3 = gauss_normal_distribution(rd,mean_iv3 , variance_iv3)
    p_iv4 = gauss_normal_distribution(th,mean_iv4 , variance_iv4)
    
    
    #probabilities of 2nd class for attributes
    p_is1 = gauss_normal_distribution(st,mean_is1 , variance_is1)
    p_is2 = gauss_normal_distribution(nd,mean_is2 , variance_is2)
    p_is3 = gauss_normal_distribution(rd,mean_is3 , variance_is3)
    p_is4 = gauss_normal_distribution(th,mean_is4 , variance_is4)
    
    
    #probabilities of 3rd class for attributes
    p_ivi1 = gauss_normal_distribution(st,mean_ivi1 , variance_ivi1)
    p_ivi2 = gauss_normal_distribution(nd,mean_ivi2 , variance_ivi2)
    p_ivi3 = gauss_normal_distribution(rd,mean_ivi3 , variance_ivi3)
    p_ivi4 = gauss_normal_distribution(th,mean_ivi4 , variance_ivi4)
    
    A =  p_ivtotal*p_iv1*p_iv2*p_iv3*p_iv4
    B =  p_istotal*p_is1*p_is2*p_is3*p_is4
    C =  p_ivitotal*p_ivi1*p_ivi2*p_ivi3*p_ivi4

    print(A,B,C)
    prediction(A,B,C)
    
    

def Main():
    
    print("please enter attribute values:")
    first_attribute = float(input("1st:"))
    second_attribute = float(input("2nd:"))
    third_attribute = float(input("3rd:"))
    fourth_attribute = float(input("4th:"))
    
    train(first_attribute,second_attribute,third_attribute,fourth_attribute)

Main()