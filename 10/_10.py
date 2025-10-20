#*-* coding: cp1251 *-*
from tkinter import *
from tkinter import messagebox

CELL, PAD = 100, 10
WIDTH, HEIGHT = 350, 350

curr_pl = "X"
game_over = False
board = [None] * 9
lines = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

def click(event):
    c, r = (event.x - PAD) // CELL, (event.y - PAD) // CELL    
    if 0 <= c < 3 and 0 <= r < 3:
        position = c + r * 3
        draw_move(position)
        move = ai()
        if curr_pl == "O" and move != -1:
                draw_move(move)


def draw_field():
    canvas.delete("all")
    for i in range(1, 3):
        canvas.create_line(CELL * i, PAD, CELL * i, CELL * 3 - PAD, width=3)
        canvas.create_line(PAD, CELL * i, CELL * 3 - PAD, CELL * i, width=3)


def ai():
    for l in lines:
        win_check = [board[i] for i in l]
        if win_check.count("O") == 2 and win_check.count(None) == 1:
            return l[win_check.index(None)]
    for l in lines:
        win_check = [board[i] for i in l]
        if win_check.count("X") == 2 and win_check.count(None) == 1:
            return l[win_check.index(None)]
    if board[4] is None:
        return 4
    for corner in [0, 2, 6, 8]:
        if board[corner] is None:
            return corner
    for i in range(9):
        if board[i] is None:
            return i
    return -1


def draw_move(pos):
    global curr_pl, game_over
    if board[pos] is not None: return
    board[pos] = curr_pl    
    
    if curr_pl == "X" and game_over == False:
        canvas.create_line(pos % 3 * CELL + PAD, pos // 3 * CELL + PAD, (pos % 3 + 1) * CELL - PAD, (pos // 3 + 1) * CELL - PAD, width=3)
        canvas.create_line(pos % 3 * CELL + PAD, (pos // 3 + 1) * CELL - PAD, (pos % 3 + 1) * CELL - PAD, pos // 3 * CELL + PAD, width=3)
    elif curr_pl == "O" and game_over == False:
        canvas.create_oval(pos % 3 * CELL + PAD, pos // 3 * CELL + PAD, (pos % 3 + 1) * CELL - PAD, (pos // 3 + 1) * CELL - PAD, width=3)

    curr_pl = "O" if curr_pl == "X" else "X"

    for l in lines:
        win_check = [board[i] for i in l]
        if win_check.count("O") == 3 or win_check.count("X") == 3 and game_over == False:
            if l == [0, 4, 8]:
                canvas.create_line(l[0] % 3 * CELL + PAD, l[0] // 3 * CELL + PAD, (l[2] % 3 + 1) * CELL - PAD, (l[2] // 3 + 1) * CELL - PAD, width=2)
            if l == [2, 4, 6]:
                canvas.create_line(l[2] % 3 * CELL + PAD, (l[2] // 3 + 1) * CELL - PAD, (l[0] % 3 + 1) * CELL - PAD, l[0] // 3 * CELL + PAD, width=2)
            if l in [[0,1,2],[3,4,5],[6,7,8]]:
                canvas.create_line(0, l[0] // 3 * CELL + CELL // 2, CELL * 3, l[0] // 3 * CELL + CELL // 2, width=2)
            if l in [[0,3,6],[1,4,7],[2,5,8]]:
                canvas.create_line(l[0] % 3 * CELL + CELL // 2, 0, l[0] % 3 * CELL + CELL // 2, CELL * 3, width=2)

            root.after(100, lambda: messagebox.showinfo("Èãðà îêîí÷åíà", f"Ïîáåäèë {"X" if curr_pl == "O" else "O" }"))
            game_over = True

    if not game_over and None not in board:
        root.after(100, lambda: messagebox.showinfo("Èãðà îêîí÷åíà", "Íè÷üÿ!"))
        game_over = True


def restart():
    global curr_pl, board, game_over
    curr_pl = "X"
    game_over =  False
    board = [None] * 9
    draw_field()

root = Tk()
root.title("Êðåñòèêè-íîëèêè")
main = Frame(root)
main.pack(padx=10,pady=10)
canvas = Canvas(main, width=WIDTH, height=HEIGHT)
canvas.pack(side=LEFT, padx=10)
canvas.bind("<ButtonPress-1>", click)
info = Frame(main)
info.pack(side=RIGHT, fill=X)
label = Label(info, text="Èãðà ïðîòèâ êîìïüþòåðà")
label.pack(side=TOP, pady=10)
btn = Button(info, text="Íà÷àòü èãðó çàíîâî", command=restart)
btn.pack(pady=8,fill=X)
draw_field()

root.mainloop()
