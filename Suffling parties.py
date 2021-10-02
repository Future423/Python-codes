for i in range(int(input())):
        n = int(input())
        odd =0
        even=0
        a = list(map(int, input().split( )))
        for x in a:
            if x%2==1:
                odd+=1
            else:
                even+=1
        pos = min(even, (n+1)//2 ) + min(odd, n//2)
        print(pos)