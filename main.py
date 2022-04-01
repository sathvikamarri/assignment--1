#assignment-1
#Name-Sathvikamarri
#Roll number-aibtech11020
#ICSE 2019 CLASS 10
#Question 6(a)
#given problem:
#(a) In the given figure, ∠PQR = ∠PST = 90o, PQ = 5 cm and PS = 2 cm.
#(i) Prove that ΔPQR ~ ΔPST.
#(ii) Find Area of ΔPQR: Area of quadrilateral SRQT


#case-1 : python program for proving similarity of two triangles PQR & PST
#case-2 : python program to find the ratio of traingle PQR and quadrilateral SQRT.

#case-1
# Function for AAA similarity
def simi_aaa(a1,a2):            
    a1 = [float(i) for i in a1]
    a2 = [float(i) for i in a2]
    a1.sort()
    a2.sort()
     
    # Check for AAA
    if a1[0] == a2[0] and a1[1] == a2[1] and a1[2] == a2[2]:
        return 1
    return 0

#driver code
#intializing  values of the angles

a1=[60,90,30]
a2=[30,90,60] 

# function call for AAA similarity
aaa = simi_aaa(a1,a2)

#checking whether the triangles are similar or not by AAA criterion
print("the triangles are "),
if aaa: print ("similar by AAA")
else: print("not similar")

#case-2
#ratio of area of triangle PQR and area of quadrilateral SQRT
#part 1 of the problem - to find the area of the triangle PQR
b = int(input("Input PQ : "))
h = int(input("Input QR : "))
area = b*h/2
print("area = ", area)

#part 2 of the problem - to find the area of quadrilateral SQRT
#area of quadrilateral= area of triangle PQR-area of triangle PST
#area of triangle PST
b = int(input("Input PS : "))
h = int(input("Input ST : "))
area = b*h/2
print("area = ", area)

#area of quadrilateral SQRT,
A1 = float(input("input area of triangle PQR: ")) #area of triangle PQR
PQR = float("%s" % A1)
print(PQR)

A2 = float(input("input area of triangle PST: ")) #area of triangle PST
PST = float("%s" % A2)
print(PST)

#area of quadrilateral SQRT = Area of triangle PQR - Aea of triangle PST
SQRT =  PQR - PST
print("SQRT: ",SQRT)

#ratio of area of triangle PQR and area of quadrilateral SQRT
ratio= PQR/SQRT
print("ratio: ",ratio)

