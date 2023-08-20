import Q02P02Class as Q

class CounterQueueManager:
    def __init__(self):
        self.counter_queues = {1: Q.Queue(), 2: Q.Queue()}
    
    def enqueue(self, customer, counter_number):
        self.counter_queues[counter_number].enqueue(customer)
    
    def display_queues(self):
        for counter_number, queue in self.counter_queues.items():
            print(f"Counter {counter_number} queue order:", end=" ")
            queue.print_queue()



counter_queue_manager = CounterQueueManager()

for i in range(3):
    num = int(input("Counter Selection"))
    counter_queue_manager.enqueue(f"Customer {i+1}", num)

counter_queue_manager.display_queues()
