"""A heap is a binary tree with the following property:-
    1] It should be complete, i.e. every node should have atleast 2 leafs
    2] Min heap: Every nodes value will be smaller than or equal to its children node value
       Max heap: Every nodes value will be greater than or equal to its children node value
    3] Heap is not sorted
    4] Root is always smallest or greatest
    5] Heap can be presented as conventional array with property chileOne --> 2i+1 and chileTwo --> 2i+2
    time: buildHeap - O(n), space : O(1)
          sift - O(log(n)) | O(1)    
"""
import random

lst = [9,12,23,17,31,30,44,102,18]
random.shuffle(lst)


class MinHeap:
    def __init__(self, array):
        self.heap = self.create_heap(array)
        
    def create_heap(self,lst_int):
        heap = [None for i in lst_int]
        heap[0] = lst_int[0]
        current_idx = 1
        for ele in lst_int[1:]:
            heap[current_idx] = ele
            self.sift_up(heap,current_idx)
            current_idx += 1
        return heap
        
    def sift_up(self,current_idx):
        subs =1 if current_idx%2!=0 else 2
        root_index = (current_idx-subs)//2
        print(f"**************** current_idx : {current_idx}")
        print(f"**************** root_index : {root_index}")
        print(f"**************** heap : {self.heap}")
        print(f"**************** heap[root_index] : {self.heap[root_index]}")
        print(f"**************** heap[current_idx] : {self.heap[current_idx]}")
        while (current_idx>0) and (self.heap[root_index]>self.heap[current_idx]):
            self.heap[root_index],self.heap[current_idx] = self.heap[current_idx],self.heap[root_index]
            current_idx = root_index
            subs =1 if current_idx%2!=0 else 2
            root_index = (current_idx-subs)//2
    
    def sift_down(self,currentIdx,endIdx):
        childOneIdx = currentIdx * 2 + 1
        while childOneIdx <= endIdx:
            childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if childTwoIdx!=-1 and self.heap[childTwoIdx]<self.eap[childOneIdx]:
                idxToSwap = childTwoIdx
            else:
                idxToSwap = childOneIdx
            
            if self.heap[idxToSwap] < self.heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, self.heap)
                self.heap[currentIdx],self.heap[idxToSwap]=self.heap[idxToSwap],self.heap[currentIdx]
                currentIdx = idxToSwap
                childOneIdx = currentIdx * 2 + 1
            else:
                break
    
    def find_node(self,ele):
        next_ele_idx = 0
        while (self.heap[next_ele_idx]!=ele):
            next_ele_idx1 = 2 * next_ele_idx + 1
            next_ele_idx2 = 2 * next_ele_idx + 2
            
            if self.heap[next_ele_idx1]==ele:
                return next_ele_idx1
            
            if self.heap[next_ele_idx2]==ele:
                return next_ele_idx2
            
            if self.heap[next_ele_idx1]
            
            
    def peek(self):
        return self.heap[0]        
            
    def remove(self):
        hp_last_idx = len(self.heap) - 1
        self.heap[hp_last_idx],self.heap[0] = self.heap[0],self.heap[hp_last_idx]
        valueToRemove = self.heap.pop()
        self.siftDown(0,len(self.heap) - 1)
        return valueToRemove
        
       
if __name__ == "__main__":
    print(f"create_heap({lst})") 
    print(f"create_heap({lst}) : {create_heap(lst)}")