# A chess game that runs in a Terminal window.
# Created 12.25.2017 by CB Fay

class chess:

    def __init__(self):
        """Constructor"""
        self.board = [[False for x in range(8)] for y in range(8)]
        self.w = '#' # white
        self.b = '$' # black
        self.e = '.' # empty
    
    def __repr__(self):
        """Return a string representation of a chess object"""
        display = ''
        rank = '8'
        display += '\n'.ljust(8)
        for file in range(65, 73):
            display += str(chr(file)).ljust(5)
        display += '\n\n\n'
        for y in self.board:
            display += rank.ljust(7)
            rank = str(int(rank)-1)
            for x in y:
                if not x:
                    display += self.e.ljust(5)
                else:
                    display += x.sym.ljust(5)
            display += '\n\n'
        return display
    
    def deusx(self, ay, ax, by, bx, swap=False):
        """Perform an arbitrary piece movement"""
        if swap:
            self.board[by][bx], self.board[ay][ax] = \
            self.board[ay][ax], self.board[by][bx]
        else:
            self.board[by][bx] = self.board[ay][ax]
            self.board[ay][ax] = None    
        
    def setboard(self):
        """Create and position piece objects according
        to the standard chess ruleset"""
        w_A = self.createpiece(pawn, 6, 0, self.w)
        w_B = self.createpiece(pawn, 6, 1, self.w)
        w_C = self.createpiece(pawn, 6, 2, self.w)
        w_D = self.createpiece(pawn, 6, 3, self.w)
        w_E = self.createpiece(pawn, 6, 4, self.w)
        w_F= self.createpiece(pawn, 6, 5, self.w)
        w_G = self.createpiece(pawn, 6, 6, self.w)
        w_H = self.createpiece(pawn, 6, 7, self.w)
        w_A_R = self.createpiece(rook, 7, 0, self.w)
        w_B_N = self.createpiece(knight, 7, 1, self.w)
        w_C_B = self.createpiece(bishop, 7, 2, self.w)
        w_K = self.createpiece(queen, 7, 3, self.w)
        w_K = self.createpiece(king, 7, 4, self.w)
        w_F_B = self.createpiece(bishop, 7, 5, self.w)
        w_G_N = self.createpiece(knight, 7, 6, self.w)
        w_H_R = self.createpiece(rook, 7, 7, self.w)
        
        b_A = self.createpiece(pawn, 1, 0, self.b)
        b_B = self.createpiece(pawn, 1, 1, self.b)
        b_C = self.createpiece(pawn, 1, 2, self.b)
        b_D = self.createpiece(pawn, 1, 3, self.b)
        b_E = self.createpiece(pawn, 1, 4, self.b)
        b_F= self.createpiece(pawn, 1, 5, self.b)
        b_G = self.createpiece(pawn, 1, 6, self.b)
        b_H = self.createpiece(pawn, 1, 7, self.b)
        b_A_R = self.createpiece(rook, 0, 0, self.b)
        b_B_N = self.createpiece(knight, 0, 1, self.b)
        b_C_B = self.createpiece(bishop, 0, 2, self.b)
        b_K = self.createpiece(queen, 0, 3, self.b)
        b_K = self.createpiece(king, 0, 4, self.b)
        b_F_B = self.createpiece(bishop, 0, 5, self.b)
        b_G_N = self.createpiece(knight, 0, 6, self.b)
        b_H_R = self.createpiece(rook, 0, 7, self.b)

        
    def createpiece(self, piecetype, y, x, color):
        """Return a new piece object"""
        newpiece = piecetype(color)
        newpiece.pos = (y,x)
        self.board[y][x] = newpiece
        return newpiece

class piece:
    pass
    
class pawn(piece):
    def __init__(self, color):
        self.pos = None
        self.col = color
        self.sym = color

class rook(piece): 
    def __init__(self, color):
        self.pos = None
        self.col = color
        self.sym = color + 'R'

class knight(piece): 
    def __init__(self, color):
        self.pos = None
        self.col = color
        self.sym = color + 'N'
        
class bishop(piece): 
    def __init__(self, color):
        self.pos = None
        self.col = color
        self.sym = color + 'B'
        
class queen(piece): 
    def __init__(self, color):
        self.pos = None
        self.col = color
        self.sym = color + 'Q'
        
class king(piece): 
    def __init__(self, color):
        self.pos = None
        self.col = color
        self.sym = color + 'K'

game = chess()
game.setboard()
print(game)
