# Developer:
# Kareem Mohamed Wardany
# ----------------------------------------

# Global Variables
Letters = []
matrix = []
scores = {}
# End of Global Variables

def createMatrix(size):
    # This Function Creates the matrix with "-" in each cell
    matrix = [] # make the matrix empty
    # the nested for loops creates the matrix and add "-" in each cell
    for i in range(size + 1):
        matrix2 = []
        for j in range(size + 1):
            matrix2.append("-")
        matrix.append(matrix2)
    return matrix

def GetLetters(size):
    # This Function gets the Letters from the user and add them to Letters List
    for i in range(1, size + 1):
        id = str(i)
        x = input("Enter Letter at " + id + " : ").upper()
        Letters.append(x)


def Addletters(size):
    # This Function adds the Letters to top and left of the Matrix
    for j in range(1, size + 1):
        matrix[0][j] = Letters[j - 1]
        matrix[j][0] = Letters[j - 1]


def ZeroDia(size):
    # This Function adds zeros in Diagonal
    for i in range(1, size + 1):
        matrix[i][i] = 0


def intializeMatrix(size):
    # This Function gets the distance between each two letters from the user
    for i in range(1, size + 1):
        for j in range(1, i):
            if i == j:
                continue
            else:
                y = float(input("Enter Value of " + matrix[i - i][j] + "," + matrix[i][j - j] + " : "))
                matrix[i][j] = y


def GetMin(size):
    # This Function gets the min value in the matrix and return its indices and min value
    min = 10000000
    for i in range(1, size + 1):
        for j in range(1, i):
            if matrix[i][j] < min:
                min = matrix[i][j]
                t1 = i
                t2 = j
    return t1, t2, min


def UpdateLetter(s1, s2):
    # This Function gets the index of first Letter in Letters List and add the combination between min value of letters at that index and then remove Two letters from Letters List
    index = Letters.index(s1)
    combine = s1+s2
    Letters.insert(index, combine)
    Letters.remove(s1)
    Letters.remove(s2)


def PrintMatrix():
    # This Function prints the Matrix in the terminal
    for z in range(len(matrix)):
        print(matrix[z])


def GetScores(size):

    # The Following nested loops fully fill in the matrix 
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if matrix[j][i] == '-':
                matrix[j][i] = matrix[i][j]
    # The Following nested loops saves the two letters as key and distance as value in dic       
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if i == j:
                continue
            else:
                scores.update({(matrix[i - i][j], matrix[i][j - j]): matrix[i][j]})


def updateMatrix(size, s1, s2):
    temp = {} # New dic that will hold the updated distances to be added to the new Matrix 
    # This loop gets the new distance and adds it to temp dic of the combinated Letters with other letters
    for i in Letters:
        if s1 in i and s2 in i : # Skip getting the distance of combination of two letters with two separate Letters 
            continue
        else:
            sum = scores[(i, s1)] + scores[(i, s2)]
            avg = sum / 2
            temp.update({(s1 + s2, i): avg})
    # This loop gets the distance of unchanged Letters and adds it to temp dic
    for i in Letters:
        for j in range(1, len(Letters)):
            if i == Letters[j]:
                continue
            else:
                try:
                    x = scores[(i, Letters[j])]
                    temp.update({(i, Letters[j]): x})
                except:
                    continue
    # This nested two loops add updated letters to the new matrix
    i = 0
    for j in range(1, size+1):
        if i < len(Letters):
            matrix[0][j] = Letters[i]
            matrix[j][0] = Letters[i]
            i += 1
    # This nested two loops add the distance of each Letter with other Letters
    for i in range(1, size):
        for j in range(1, i):
            if i == j:
                continue
            else:
                if matrix[i - i][j] == matrix[i][j - j]:
                    y = 0
                else:
                    try:
                        y = temp[(matrix[i - i][j], matrix[i][j - j])]
                    except:
                        y = temp[(matrix[i][j-j], matrix[i-i][j])]
                matrix[i][j] = y


if __name__ == '__main__':
    n = int(input("Enter Matrix Size : "))
    GetLetters(n)
    matrix = createMatrix(n)
    Addletters(n)
    ZeroDia(n)
    intializeMatrix(n)
    print("\n")
    print("This Your Matrix:")
    PrintMatrix()   
    counter = 1
    while n > 2:
        c1, c2, min = GetMin(n)
        mstr = str(min)
        print("Minimum: " +mstr)
        print("Tree:")
        print(Letters)
        temp1 = matrix[c1 - c1][c2]
        temp2 = matrix[c1][c2 - c2]
        UpdateLetter(temp1, temp2)
        GetScores(n)
        matrix = createMatrix(n-1)
        ZeroDia(n-1)
        updateMatrix(n, temp1, temp2)
        c = str(counter)
        print("\n")
        print("This Matrix after iteration "+ c +" : ")
        PrintMatrix()
        n -= 1
        counter += 1
    print("Tree:")
    print(Letters)