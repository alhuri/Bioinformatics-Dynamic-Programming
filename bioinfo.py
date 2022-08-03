def edit_distance(string_x: str, string_y: str) -> list(list()):
    string_x = ' ' + string_x
    string_y = ' ' + string_y
    
	
    len_x = len(string_x)
    len_y = len(string_y)
    
    #Starting the distance matrix
    dist_mat = [[0] * len_y for i in range(len_x)]  
    for i in range(len_x):
        dist_mat[i][0] = i
    for j in range (len_y):
        dist_mat[0][j] = j
    
    #Calculating the distance matrix row by row.
    for j in range(1, len_y):
        for i in range(1, len_x):
            s = 1
            
            if (string_x[i] == string_y[j]):
                s = 0

            dist_mat[i][j] = min(dist_mat[i-1][j] + 1, # insert
                            dist_mat[i][j-1] + 1, # delete
                            dist_mat[i-1][j-1] + s) # substitute
    return dist_mat