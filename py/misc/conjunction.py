"""
Take a series of True or False and compute conjunction 
T : True, F : False
conjunction : x AND y AND z ...

Overall True when ALL are True
-->Overall False when any of one them is False
"""
import sys
values = sys.argv[1:]
result = True
count = 0
for v in values:
    count += 1
    if (v == 'F'):
        result = False
        break

print("Result : {0}, \nNubmer of checks : {1}".
        format(result, count))




































"""

Gender : Male, Female
Age    : Child, Adult

Gender       Age          Combination
---------+-------------+--------------
Male         Child         MC-V1
Male         Adult         MA-V1
Female       Child         FC-V1
Female       Adult         FA-V1

MC-V1 : (Gender == Male) AND (Age = Child)
FA-V1 : (Gender == Female)  AND (Age == Adult)
MA-V1 : (Gender == Male) AND (Age = Adult)

"""

"""
Gender       Age          Combination
---------+-------------+--------------
Male         Child         MrC-V2
Male         Adult         MrC-V2
Female       Child         MrC-V2
Female       Adult         FA-V2

Age ? Child

MrC-V2 = (Age == Child)

Age ? Adult 

MrC-V2 = (Age == Adult) AND (Gender == Male)
FA-V2 = (Age == Adult) AND (Gender == Female)

"""








"""
Gender       Age         Dose      Vaccine
---------+-------------+---------+--------------
Male         Child       1          M1
Male         Adult       1          M1
Female       Child       1          F1
Female       Adult       1          F1
Male         Child       2          M2
Male         Adult       2          M2
Female       Child       2          F2
Female       Adult       2          F2

Gender , Age, Dose     - Works. But ...

Age, Dose              - Not sufficient. We need Gender

Gender, Dose
    Male, 1 = M1
    Male, 2 = M2
    Female, 1 = F1
    Female, 2 = F2
"""

"""
Kuchipudi Dance
Eligibility Crieteria :

Gender   Age          Eligibility
--------+-----------+-------------
Male     Child        Yes
Male     Adult        No
Female   Child        Yes
Female   Adult        Yes

Either Female or Children are eligible
    if( Gender == Female ) OR ( Age = Child ):
        Eligibility = True
    else:
        Eligibility = False

"""

"""
Everest Expedition 
Eligibility Crieteria :

Gender   Age          Eligibility
--------+-----------+-------------
Male     Child        No
Male     Adult        Yes
Female   Child        No
Female   Adult        Yes

Either Male or Female are eligible - Not correct


--> Either Male Adult or Female Adult are eligible. - Correct but not precise.

    Male Adult = Male AND Adult = (Gender == Male) AND (Age == Adult)
    Female Adult = Female AND Adult = (Gender == Female) AND (Age == Adult)

    "Male Adult" OR "Female Adult" =
        (Gender == Male) AND (Age == Adult)
        OR
        (Gender == Female) AND (Age == Adult)
            
   
   if (( Gender == Male) AND (Age == Adult)) OR
      (( Gender == Female) AND (Age == Adult)):
        Eligibility = True
   else:
        Eligibility = False
    


--> All adults are eligible. - Correct

    if(Age == Adult):
        Eligibility = True
    else:
        Eligibility = False


"""








