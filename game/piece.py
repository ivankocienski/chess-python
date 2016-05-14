
import pygame.gfxdraw as gfx

SPR_PAWN   = 0
SPR_KNIGHT = 1
SPR_ROOK   = 2
SPR_BISHOP = 3
SPR_QUEEN  = 4
SPR_KING   = 5

SPR_WHITE = 0
SPR_BLACK = 6

COLOR_WHITE = -1
COLOR_BLACK = 1

class Piece():
    def __init__(self, image, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.image = image
        self.highlight_for_move = False

    def is_at(self, x, y):
        return self.xpos == x and self.ypos == y

    def about_to_move(self, yes=True):
        self.highlight_for_move = yes

    def legal_moves(self, board):
        return ()

    def move_to(self, x, y):
        self.xpos = x
        self.ypos = y

    def draw(self, screen):
        dx = 44 + self.xpos * 64
        dy = 44 + self.ypos * 64
        
        if self.highlight_for_move:
            gfx.rectangle(screen, (dx, dy, 64, 64), (4, 133, 168))
            gfx.rectangle(screen, (dx+1, dy+1, 62, 62), (4, 133, 168))
            #screen.fill((4, 133, 168), (dx, dy, 64, 64))

        screen.blit(self.image, (dx+8, dy+8))

class PawnPiece(Piece):
    def __init__(self, sprites, color, xpos, ypos):
        spr = SPR_PAWN
        if color == COLOR_BLACK:
            spr += SPR_BLACK
        super().__init__(sprites[spr], xpos, ypos)

class KnightPiece(Piece):
    def __init__(self, sprites, color, xpos, ypos):
        spr = SPR_KNIGHT
        if color == COLOR_BLACK:
            spr += SPR_BLACK
        super().__init__(sprites[spr], xpos, ypos)

class RookPiece(Piece):
    def __init__(self, sprites, color, xpos, ypos):
        spr = SPR_ROOK
        if color == COLOR_BLACK:
            spr += SPR_BLACK
        super().__init__(sprites[spr], xpos, ypos)

    def legal_moves(self, board):
        
        try_left  = (self.xpos-1, self.ypos)
        try_right = (self.xpos+1, self.ypos)
        try_up    = (self.xpos,   self.ypos-1)
        try_down  = (self.xpos,   self.ypos+1)

        allowed_moves = []
        for i in range(8):
            done = True

            if try_up:
                if board.in_bounds(try_up[0], try_up[1]) and not board.find_piece_at(try_up[0], try_up[1]):
                    done = False
                    allowed_moves.append(try_up)
                    try_up = (try_up[0], try_up[1]-1)
                else: 
                    try_up = None 

            if try_down:
                if board.in_bounds(try_down[0], try_down[1]) and not board.find_piece_at(try_down[0], try_down[1]):
                    done = False
                    allowed_moves.append(try_down)
                    try_down = (try_down[0], try_down[1]+1)
                else: 
                    try_down = None 

            if try_left:
                if board.in_bounds(try_left[0], try_left[1]) and not board.find_piece_at(try_left[0], try_left[1]):
                    done = False
                    allowed_moves.append(try_left)
                    try_left = (try_left[0]-1, try_left[1])
                else: 
                    try_left = None 

            if try_right:
                if board.in_bounds(try_right[0], try_right[1]) and not board.find_piece_at(try_right[0], try_right[1]):
                    done = False
                    allowed_moves.append(try_right)
                    try_right = (try_right[0]+1, try_right[1])
                else: 
                    try_right = None 
            
            if done:
                break 

        return allowed_moves

class BishopPiece(Piece):
    def __init__(self, sprites, color, xpos, ypos):
        spr = SPR_BISHOP
        if color == COLOR_BLACK:
            spr += SPR_BLACK
        super().__init__(sprites[spr], xpos, ypos)

    def legal_moves(self, board):
        
        try_left_up    = (self.xpos-1, self.ypos-1)
        try_right_up   = (self.xpos+1, self.ypos-1)
        try_left_down  = (self.xpos-1, self.ypos+1)
        try_right_down = (self.xpos+1, self.ypos+1)

        allowed_moves = []
        for i in range(8):
            done = True

            if try_left_up:
                if board.in_bounds(try_left_up[0], try_left_up[1]) and not board.find_piece_at(try_left_up[0], try_left_up[1]):
                    done = False
                    allowed_moves.append(try_left_up)
                    try_left_up = (try_left_up[0]-1, try_left_up[1]-1)
                else: 
                    try_left_up = None 

            if try_right_up:
                if board.in_bounds(try_right_up[0], try_right_up[1]) and not board.find_piece_at(try_right_up[0], try_right_up[1]):
                    done = False
                    allowed_moves.append(try_right_up)
                    try_right_up = (try_right_up[0]+1, try_right_up[1]-1)
                else: 
                    try_right_up = None 

            if try_left_down:
                if board.in_bounds(try_left_down[0], try_left_down[1]) and not board.find_piece_at(try_left_down[0], try_left_down[1]):
                    done = False
                    allowed_moves.append(try_left_down)
                    try_left_down = (try_left_down[0]-1, try_left_down[1]+1)
                else: 
                    try_left_down = None 

            if try_right_down:
                if board.in_bounds(try_right_down[0], try_right_down[1]) and not board.find_piece_at(try_right_down[0], try_right_down[1]):
                    done = False
                    allowed_moves.append(try_right_down)
                    try_right_down = (try_right_down[0]+1, try_right_down[1]+1)
                else: 
                    try_right_down = None 
            
            if done:
                break 

        return allowed_moves

class QueenPiece(Piece):
    def __init__(self, sprites, color, xpos, ypos):
        spr = SPR_QUEEN
        if color == COLOR_BLACK:
            spr += SPR_BLACK
        super().__init__(sprites[spr], xpos, ypos)

class KingPiece(Piece):
    def __init__(self, sprites, color, xpos, ypos):
        spr = SPR_KING
        if color == COLOR_BLACK:
            spr += SPR_BLACK
        super().__init__(sprites[spr], xpos, ypos)

    def legal_moves(self, board):
        moves = [
                (self.xpos-1, self.ypos-1),
                (self.xpos  , self.ypos-1),
                (self.xpos+1, self.ypos-1),
                (self.xpos-1, self.ypos),
                (self.xpos+1, self.ypos),
                (self.xpos-1, self.ypos+1),
                (self.xpos  , self.ypos+1),
                (self.xpos+1, self.ypos+1)]

        allowed_moves = []
        for m in moves:
            if not board.in_bounds(m[0], m[1]):
                continue
            allowed_moves.append(m)

        return allowed_moves
                

