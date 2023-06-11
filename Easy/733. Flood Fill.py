def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    m, n = len(image), len(image[0])
    val = image[sr][sc]
    if val == color:
        return image

    def traverse(i, j):
        if image[i][j] == val:
            image[i][j] = color
            for (x, y) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= i + x < m and 0 <= j + y < n:
                    traverse(i + x, j + y)

    traverse(sr, sc)
    return image
