from typing import Any


class QueueSecond:

    def __init__(self):
        self.head = None
        self.tail = None

    
    class DataNode:
        
        def __init__(self, value: Any, next = None) -> None:
            self.value = value
            self.next = next

    def add(self, value: Any) -> None:
        if self.head is None:
            self.head = self.tail = self.DataNode(value=value)
            return 
        
        data_node = self.tail

        self.tail = data_node.next = self.DataNode(value=value)

    def pull(self) -> Any:
        required_data = self.head
        self.head = self.head.next        
        return required_data.value
    
    def show(self) -> None:

        data_node = self.head
        
        try:
            print(data_node.value)
            while data_node.next:            
                data_node = data_node.next
                print(data_node.value)

        except AttributeError:
            print('No elements in queue')


def t_1():
    q = QueueSecond()
    q.add(2)
    q.show()
    assert q.pull() == 2 




t_1()

    





        

        
    
