def numJewelsInStones(self,J, S):
            num=0
            J = list(J)
            S = list(S)
            for x,s  in enumerate(J):
                for p,q  in enumerate(S):
                    if(J[x]==S[p]):
                        num=num+1
            return num
        
