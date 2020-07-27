class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      nums3=nums1+nums2
      def quicksort(arr,l,r):
            if(l<r):
                p=partition(arr,l,r)
                quicksort(arr,l,p-1)
                quicksort(arr,p+1,r)
      def partition(arr,l,r):
        q=arr[r]
        tp=0
        i=l-1
        for j in range(l,r):
            if(arr[j]<=q):
                i+=1
                tp=arr[j]
                arr[j]=arr[i]
                arr[i]=tp
        tp=arr[i+1]
        arr[i+1]=arr[r]
        arr[r]=tp
        return i+1
      quicksort(nums3,0,len(nums3)-1)
      if(len(nums3)%2==0):
        return (nums3[len(nums3)//2-1]+nums3[len(nums3)//2])/2
      else:
        return nums3[len(nums3)//2]
        
     
                    
                    
                
        
