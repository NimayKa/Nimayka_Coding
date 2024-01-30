def calculate_grades(score):
    if score >= 90:
        grade ='A'
    elif score >= 80 and score < 90:
        grade ='B'
    elif score >= 70 and score <80:
        grade ='C'
    elif score >= 60 and score <50:
        grade ='D'
    else:
        grade = 'F'

    return grade

score_input = input("Please enter your scores. ").split(',')
scores = [int(score) for score in score_input]
print (scores)

i = 0
print ("Your average score is",round(sum(scores) / len(scores)))
while i < len(scores):
    print ('Your Grade is ',calculate_grades(scores[i]))
    i +=1