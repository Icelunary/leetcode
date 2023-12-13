class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        for r in range(row):
            for c in range((col + 1) // 2):
                image[r][c], image[r][col - c - 1] = image[r][col - c - 1], image[r][c]
                # print(image, image[r][c], image[r][c] ^ 1, "row: ", r, "col: ", c)
                image[r][c] ^= 1
                if c != col - c - 1:
                    image[r][col - c - 1] ^= 1
                
        # print(image)
                    
        return image
        