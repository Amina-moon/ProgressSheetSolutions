class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        m=len(image)
        n=len(image[0])
        flipped_image=[[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                flipped_image[i][j] = image[i][n - j - 1] 
                if flipped_image[i][j] == 0:
                    flipped_image[i][j]=1
                elif flipped_image[i][j] == 1:
                    flipped_image[i][j] = 0
        return flipped_image
