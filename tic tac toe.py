import time

plane_matrix = [[" "," "," "],[" "," "," "],[" "," "," "]]

def check_winner():
    result = ""

    j = 0
    while 3 > j:
        ref = plane_matrix[j][0]
        count = 0
        for i in plane_matrix[j]:
            if ref == " ":
                ref = ""
            if i != ref:
                pass
            else:
                count += 1
        if count == 3:
            result = ref + " Win!"
            return result
        j += 1
    if result == "":
        j = 0
        i = 0
        while 3 > j:
            ref = plane_matrix[0][j]
            count = 0
            while 3 > i:
                if ref == " ":
                    ref = ""
                if plane_matrix[i][j] != ref:
                    pass
                else:
                    count += 1
                i += 1
            if count == 3:
                result = ref + " Win!"
                return result
            j += 1
    ref1 = " "
    count1 = 0
    for i in plane_matrix:
        for j in i:
            if j != ref1:
                count1 += 1
    if count1 == 9:
        result = "Draw"
        return result
    return result

def print_plane(plane_matrix):
    print(f"""
     {plane_matrix[0][0]} | {plane_matrix[0][1]} | {plane_matrix[0][2]}
    -----------
     {plane_matrix[1][0]} | {plane_matrix[1][1]} | {plane_matrix[1][2]}
    -----------
     {plane_matrix[2][0]} | {plane_matrix[2][1]} | {plane_matrix[2][2]}
     """)


def check(row, column):
    if plane_matrix[row][column] == " ":
        return True
    else:
        return False

def play(row, column, value):
    if check(row, column):
        plane_matrix[row][column] = value
        result = check_winner()
        if len(result) > 0:
            print_plane(plane_matrix)
            print(result)
            exit()
        else:
            if value == "X":
                player2()
            else:
                player1()
    else:
        print("""

 {!}: Invalid Position!

        """)
        if value == "X":
            player1()
        else:
            player2()



def print_msg_with_delay(msg):
    time.sleep(2)
    print(msg)

def player1():
    print_plane(plane_matrix)
    print("""Player1:
    """)
    row = int(input(" Row > "))
    if row > 3 or row < 1:
        print("Invalid Input!")
        player1()
    column = int(input(" Column > "))
    if column > 3 or column < 1:
        print("Invalid Input!")
        player1()
    play(row-1, column-1, "X")

def player2():
    print_plane(plane_matrix)
    print("""Player2:
    """)
    row = int(input(" Row > "))
    if row > 3 or row < 1:
        print("Invalid Input!")
        player2()
    column = int(input(" Column > "))
    if column > 3 or column < 1:
        print("Invalid Input!")
        player2()
    play(row-1, column-1, "O")


print("\n")
print("This game is for two players. Bring someone to play with!")
print_msg_with_delay("Here we are! Let's get started!")
print_msg_with_delay("""

Game Instructions:
------------------
- Every player will choose row and column in each turn
- Then, the plane would be updated for you
- Diagonals aren't being treated as a winning
""")

player1()
