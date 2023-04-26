# 9 Flood Fill

# An image is represented by an m x n integer grid image where image[i][j]
# represents the pixel value of the image.

# You are also given three integers sr, sc, and color.
# You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel,
# plus any pixels connected 4-directionally to the starting pixel of the same color
# as the starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color), and so on. Replace the color of all of
# the aforementioned pixels with color.

# Return the modified image after performing the flood fill.

# Example 1:
# Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel),
# all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels)
# are colored with the new color.
# Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

# Example 2:
# Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
# Output: [[0,0,0],[0,0,0]]
# Explanation: The starting pixel is already colored 0,
# so no changes are made to the image.

def floodFill(image, sr, sc, newColor):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type newColor: int
    :rtype: List[List[int]]
    """
    # Check if the starting pixel has the same color as the new color
    if image[sr][sc] == newColor:
        return image

    # Define a helper function to perform the flood fill recursively
    def dfs(r, c):
        # Check if the current pixel is within the bounds of the image
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
            return
        # Check if the current pixel has the same color as the starting pixel
        if image[r][c] == startColor:
            # Update the color of the current pixel
            image[r][c] = newColor
            # Recursively perform the flood fill on the adjacent pixels
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

    # Get the starting color of the image
    startColor = image[sr][sc]
    # Perform the flood fill starting from the specified pixel
    dfs(sr, sc)
    # Return the modified image
    return image


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2
print(floodFill(image, sr, sc, color))
image1 = [[0, 0, 0], [0, 0, 0]]
sr1 = 0
sc1 = 0
color1 = 0
print(floodFill(image1, sr1, sc1, color1))
