import Q02P02Class as Queue
class CounterManager:
    def __init__(self):
        self.counter = {1:Queue.Queue(),2:Queue.Queue()}
    
    def enqueue1(self,customer,counter_num):
        print (counter_num,customer)
        self.counter[counter_num].enqueue(customer)


counter_queue_manager = CounterManager()
for customer in range(3):
        
    counter=int(input("Enter Number"))
    counter_queue_manager.enqueue1(customer,counter)

