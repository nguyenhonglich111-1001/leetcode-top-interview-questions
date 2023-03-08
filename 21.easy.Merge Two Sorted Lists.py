# NOTE 62.17%
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # This solution is about the recursive of the pointer of next in node

        # Assume the we are in current state, which node is greater is the chosen one of previous node.
        # And the pointer *next of this node will be calc the function calc next time.
        def solve(list1,list2):
            if not list1:
                return list2
            elif not list2:
                return list1
            else: 
                
                val = 0
                if list1.val > list2.val:
                    val = list2.val
                    list2 = list2.next
                else:
                    val = list1.val
                    list1 = list1.next

                return ListNode(val, self.mergeTwoLists(list1,list2))

        return solve(list1, list2)
        


            