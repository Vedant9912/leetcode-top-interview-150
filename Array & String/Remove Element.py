class Solution:
    def removeElement(self, arr: List[int], elem: int) -> int:
        write=0
        for read in range(len(arr)):
            if arr[read]!=elem:
                arr[write]=arr[read]
                write+=1
        return write
