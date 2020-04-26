'''
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
'''

if __name__ == '__main__':
    students = []
    scorelist=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        scorelist+=[score]        
    #srtd = sorted(students, key = lambda x: x[1]) 
    #lowestscore = min(srtd, key=lambda x:x[1])
    #following creates a dictionary with unique values only, removes the repititve elements out
    #in its place we can also use b=sorted(list(set(scorelist)))[1] 
    scorelist = list(dict.fromkeys(scorelist))
    b=sorted(scorelist)[1] #taking out the second element coz it has no repeats
    #print(scorelist)
    #o/p: [21.0, 31.0, 41.0]
    #print(dict)
    #o/p: <class 'dict'>
    #print(str(dict))
    #o/p: <class 'dict'>
    for k,v in sorted(students):
        if v==b:
            print(k)