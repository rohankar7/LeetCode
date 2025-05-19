# 661. Image Smoother
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        s = [[img[i][j] for j in range(3)] for i in range(3)]
        for i in range(3):
            for j in range(3):
                if i==0 and j==0: img[i][j] = (s[i][j] + s[i+1][j] + s[i][j+1] + s[i+1][j+1])//4
                elif i==0 and j==2: img[i][j] = (s[i][j-1] + s[i][j] + s[i+1][j-1] + s[i+1][j])//4
                elif i==2 and j==0: img[i][j] = (s[i-1][j] + s[i-1][j+1] + s[i][j] + s[i][j+1])//4
                elif i==2 and j==2: img[i][j] = (s[i-1][j-1] + s[i-1][j] + s[i][j-1] + s[i][j])//4
                elif i==0 and j==1: img[i][j] = (s[i][j-1]+s[i][j]+s[i][j+1]+s[i+1][j-1]+s[i+1][j]+s[i+1][j+1])//6
                elif i==1 and j==0: img[i][j] = (s[i-1][j]+s[i-1][j+1]+s[i][j]+s[i][j+1]+s[i+1][j]+s[i+1][j+1])//6
                elif i==1 and j==2: img[i][j] = (s[i-1][j-1]+s[i-1][j]+s[i][j-1]+s[i][j]+s[i+1][j-1]+s[i+1][j])//6
                elif i==2 and j==1: img[i][j] = (s[i-1][j-1]+s[i-1][j]+s[i-1][j+1]+s[i][j-1]+s[i][j]+s[i][j+1])//6
                else: img[i][j] = sum(s[i][j] for j in range(3) for i in range(3))//9
        return img