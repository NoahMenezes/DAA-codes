solution_count = 0

def NQueens(k,n):
    global solution_count

    for i in range(n):

        if place(k,i):
            x[k] = i
            
            if k == n-1:
                solution_count += 1
                solution_vector = [col + 1 for col in x]
                print(f"Solution{solution_count} : {solution_vector}")
            
                print_board(x,n)

            else:
                NQueens(k+1,n)

def place(k,i):
    for j in range(k):
        if (x[j] == i) or abs(x[j] - i) == abs(j-k):
            return False

    return True

def print_board(x,n):
    board = [['-']*n for _ in range(n)]
    for row in range(n):
        col = x[row]
        board[row][col] = 'Q'

    for row in board:
        print(" ".join(row))

    print("\n")

n = int(input("Enter the No. of Queens: "))
x = [-1]*n
NQueens(0,n)

if solution_count == 0:
    print("No Solution Exists for this COnfiguration\n")
        
        
