class grade_calculator ():
    def __init__(self):
        self.mark =[]
        self.grade =[]
        self.size = 0
    
    def insertmark(self,mark):
        self.mark.append(mark)
          
    def display (self):
        i = 0
        while i <= len(self.mark) -1:
            print ('Student',i,self.mark[i])
            i+=1
    
    def displaygrade (self):
        i = 0
        while i < len(self.mark) -1:
            print ('Student',i,self.grade[i])
            i+=1
            
    def recursive(self,index=0):
        if index == len(self.mark)-1:
            return self.mark[index]
        else:
            value = self.mark[index]
            if value < 70 :
                grade= 'F'
            elif value >= 70 and value <80:
                grade= 'C'
            elif value >= 80 and value <90:
                grade= 'B'
            elif value >= 80 and value <=100:
                grade= 'A'     
            else:
                grade= 'MEMBAUTA'
            self.grade.append(grade) 
            return self.recursive(index+1)
    
Grade=grade_calculator()            
Grade.insertmark(50)
Grade.insertmark(80)
Grade.insertmark(40.99)
Grade.insertmark(10.99)
Grade.insertmark(91)
Grade.insertmark(70)
Grade.insertmark(701)
print ('\nDisplay Mark Only')
Grade.display()
print ('\nDisplay Grade Only')
Grade.recursive()
Grade.displaygrade()
    
        