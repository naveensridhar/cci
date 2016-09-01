# We will split the matrix into layers(outer square, inner square and so on)
# Then we will take one layer at a time and move top left to top right, top right to bottom right
# bottom right to bottom left and so on. Then we will take the second element in the layer and 
# do the same. Complexity will be n2
# Try it later

def rotate_matrix(input):
    n = len(input)/2
    for layer in range(0, n):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top_left = input[first][i]
             
            input[first][i] = input[last - offset][first]
            input[last - offset][first] = input[last][last - offset]
            input[last][last - offset] = input[i][last]
            input[i][last] = top_left
