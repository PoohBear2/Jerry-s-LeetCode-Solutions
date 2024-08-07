class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        pointer1 = 0
        pointer2 = 0
        result = ''
        max1 = len(word1)
        max2 = len(word2)
        while pointer1 < max1:
            result = result + word1[pointer1]
            if pointer2 < max2:
                result = result + word2[pointer2]
                pointer2 = pointer2 + 1
            pointer1 = pointer1 + 1
        while pointer2 < max2:
            result = result + word2[pointer2]
            pointer2 = pointer2 + 1
        return result
            
        
            
        
                

    
    


        