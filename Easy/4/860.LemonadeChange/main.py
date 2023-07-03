class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        info_err = dict()
        info = dict()
        errs = 0
        flag = False
        for i in range(len(s)):
            x,y = s[i], goal[i]
            if x != y:
                errs += 1
                
                if errs > 2:
                    return False
                elif errs == 2 and  (x not in info_err or info_err[x] !=  y):
                    return False
                info_err[y] = x
            if x not in info:
                info[x] = 0
            info[x] += 1
            if info[x] > 1:
                flag = True
        if errs == 1:
            return False
        
        return True if errs == 2 else flag
        
                
