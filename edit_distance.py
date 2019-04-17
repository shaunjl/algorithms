"""
int EditDistance(char s[1..m], char t[1..n])
   // For all i and j, d[i,j] will hold the Levenshtein distance between
   // the first i characters of s and the first j characters of t.
   // Note that d has (m+1) x (n+1) values.
   let d be a 2-d array of int with dimensions [0..m, 0..n]
  
   for i in [0..m]
     d[i, 0] ← i // the distance of any first string to an empty second string
                 // (transforming the string of the first i characters of s into
                 // the empty string requires i deletions)
   for j in [0..n]
     d[0, j] ← j // the distance of any second string to an empty first string
  
   for j in [1..n]
     for i in [1..m]
       if s[i] = t[j] then  
         d[i, j] ← d[i-1, j-1]        // no operation required
       else
         d[i, j] ← minimum of
                    (
                      d[i-1, j] + 1,  // a deletion
                      d[i, j-1] + 1,  // an insertion
                      d[i-1, j-1] + 1 // a substitution
                    )
  
   return d[m,n]
   """

def edit_distance(s, t):
    """
    Wagner-Fischer dynamic programming (bottom up) approach
    s: word 1
    t: word 2
    return: distance between s and t
    """

    distances = [[0 for __ in range(len(s) + 1)] for _ in range(len(t) + 1)]

    for i in range(len(distances[0])):
        distances[0][i] = i

    for j in range(len(distances)):
        distances[j][0] = j

    for j in range(1, len(t) + 1):
        for i in range(1, len(s) + 1):
            if s[i - 1] == t[j - 1]:
                distances[j][i] = distances[j - 1][i - 1]
            else:
                deletion = distances[j - 1][i] + 1
                insertion = distances[j][i - 1] + 1
                substition = distances[j - 1][i - 1] + 1
                distances[j][i] = min(deletion, insertion, substition)

    return distances[-1][-1]

print(edit_distance('kitten', 'sitting'))
