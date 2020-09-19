
def longestPalindrome(str):

    start=0
    length=len(str)
    mx=1
    for i in range(1,length):


        low=i-1
        high=i

        while low>=0 and high<length and str[low]==str[high]:
            if high-low+1>mx:
                start=low
                mx=high-low+1
            low-=1
            high+=1

        low=i-1
        high=i+1


        while low>=0 and high<length and str[low]==str[high]:
            if high-low+1>mx:
                start=low
                mx=high-low+1
            low-=1
            high+=1

        
    print(str[start:start+mx])

    print(mx)


longestPalindrome("aaabaacghjk")