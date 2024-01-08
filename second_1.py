from dataclasses import dataclass, field
from typing import Any, List, Union

@dataclass
class QueueFirst:

    _stack: List[Any] = field(default_factory=list)
    deep_queue: int = 5
    

    def _check_size(self) -> bool:
        """Сверка глубины и фактической длины очереди"""
        return self._size_queue() < self.deep_queue
    
        
    def _size_queue(self) -> int:
        return len(self._stack)
    
    def show(self) -> List[Any]:
        return self._stack
    
    def pull(self) -> Union[Any, None]:
        try:
            return self._stack.pop(0)
        
        except IndexError:
            raise IndexError('No elements in queue')

            
    def add(self, element: Any) -> None:
        """Перед постановкой в очередь будет осуществлена проверка на возможность добавления в очередь. В случае невозможности будет предложено расширение размера очереди."""
        if self._check_size():
            self._stack.append(element)
        else:
            raise MemoryError('Queue is full')
                

def test_1():
    q = QueueFirst()
    q.add(3)
    q.add(4)
    q.add(5)
    q.show()
    assert q.pull() == 3

def test_2(deep):
    q = QueueFirst(deep_queue=deep)    
    q.show()
    assert q.pull() == IndexError

def test_3(deep):
    q = QueueFirst(deep_queue=deep)  
    q.add(3)
    q.add(4)      
    q.show()
    assert q.add(5) == MemoryError
    

test_1()
test_2(3)
test_3(2)


    
    



        
    
