class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        answer = '1'
        if n == 1:
            return answer
        for i in range(n-1):
            new_el = []
            temp = answer[0]
            temp_number = 0
            for x in answer:
                if x == temp:
                    temp_number +=1
                else:
                    new_el.append('{}{}'.format(temp_number, temp))
                    temp_number = 1
                    temp = x

            new_el.append('{}{}'.format(temp_number, temp))
            answer = ''.join(new_el)
        return answer
