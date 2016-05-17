
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
    def __init__(self, board, sprite, color, xpos, ypos):
        self.board     = board
        self.xpos      = xpos
        self.ypos      = ypos
        self.image     = sprite 
        self.color     = color
        self.has_moved = False

    def is_at(self, x, y):
        return self.xpos == x and self.ypos == y

    def about_to_move(self, yes=True):
        self.highlight_for_move = yes

    def legal_moves(self, board):
        return ()

    def move_to(self, x, y):
        self.has_moved = True
        self.board.position_at(self.xpos, self.ypos).piece = None

        self.xpos = x
        self.ypos = y
        self.board.position_at(self.xpos, self.ypos).piece = self

    def _legal_move_in_dir(self, board, count, x, y, xi, yi):
        allowed_moves = []

        for i in range(count):

            if self.board.in_bounds(x, y) and not self.board.position_at(x, y).piece:
                allowed_moves.append((x, y))
                x += xi
                y += yi
            else:
                break 

        return allowed_moves

    def _legal_diagonal_moves(self, board, count=8):
        
        allowed_moves = []

        # NW
        allowed_moves.extend(self._legal_move_in_dir(board, count, self.xpos-1, self.ypos-1, -1, -1))

        # NE
        allowed_moves.extend(self._legal_move_in_dir(board, count, self.xpos+1, self.ypos-1,  1, -1))

        # SW
        allowed_moves.extend(self._legal_move_in_dir(board, count, self.xpos-1, self.ypos+1, -1,  1))

        # SE
        allowed_moves.extend(self._legal_move_in_dir(board, count, self.xpos+1, self.ypos+1,  1,  1))

        return allowed_moves

    def _legal_cardinal_moves(self, board, count=8):

        allowed_moves = []

        # W
        allowed_moves.extend(self._legal_move_in_dir(board, count, self.xpos-1, self.ypos, -1, 0))

        # E
        allowed_moves.extend(self._legal_move_in_dir(board, count, self.xpos+1, self.ypos, 1, 0))

        # N
        allowed_moves.extend(self._legal_move_in_dir(board, count, self.xpos, self.ypos-1, 0, -1))

        # S
        allowed_moves.extend(self._legal_move_in_dir(board, count, self.xpos, self.ypos+1, 0, 1))

        return allowed_moves

    def draw(self, screen, dx, dy):
        screen.blit(self.image, (dx+8, dy+8))

class PawnPiece(Piece):
    def __init__(self, board, color, xpos, ypos):
        spr = SPR_PAWN
        if color == COLOR_BLACK:
            spr += SPR_BLACK
        super().__init__(board, board.piece_sprites[spr], color, xpos, ypos)

    def legal_moves(self, board): 
        allowed_moves = []
        new_y = self.ypos + self.color

        if self.board.in_bounds(self.xpos, new_y):
            allowed_moves.append((self.xpos, new_y))

        if not self.has_moved:
            new_y += self.color
            if self.board.in_bounds(self.xpos, new_y):
                allowed_moves.append((self.xpos, new_y))
        
        return allowed_moves

class KnightPiece(Piece):
    def __init__(self, sprites, color, xpos, ypos):
        spr = SPR_KNIGHT
        if color == COLOR_BLACK:
            spr += SPR_BLACK
        super().__init__(sprites[spr], color, xpos, ypos)

    def legal_moves(self, board): 
        allowed_moves = []
        if self.board.in_bounds(self.xpos-1, self.ypos-2):
            allowed_moves.append((self.xpos-1, self.ypos-2))

        if self.board.in_bounds(self.xpos+1, self.ypos-2):
            allowed_moves.append((self.xpos+1, self.ypos-2))

        if self.board.in_bounds(self.xpos-1, self.ypos+2):
            allowed_moves.append((self.xpos-1, self.ypos+2))

        if self.board.in_bounds(self.xpos+1, self.ypos+2):
            allowed_moves.append((self.xpos+1, self.ypos+2))

        if self.board.in_bounds(self.xpos-2, self.ypos-1):
            allowed_moves.append((self.xpos-2, self.ypos-1))

        if self.board.in_bounds(self.xpos-2, self.ypos+1):
            allowed_moves.append((self.xpos-2, self.ypos+1))

        if self.board.in_bounds(self.xpos+2, self.ypos-1):
            allowed_moves.append((self.xpos+2, self.ypos-1))

        if self.board.in_bounds(self.xpos+2, self.ypos+1):
            allowed_moves.append((self.xpos+2, self.ypos+1))

        return allowed_moves

class RookPiece(Piece):
    def __init__(self, sprites, color, xpos, ypos):
        spr = SPR_ROOK
        if color == COLOR_BLACK:
            spr += SPR_BLACK
        super().__init__(sprites[spr], color, xpos, ypos)

    def legal_moves(self, board): 
        return self._legal_cardinal_moves(board)
        
class BishopPiece(Piece):
    def __init__(self, sprites, color, xpos, ypos):
        spr = SPR_BISHOP
        if color == COLOR_BLACK:
            spr += SPR_BLACK
        super().__init__(sprites[spr], color, xpos, ypos)

    def legal_moves(self, board): 
        return self._legal_diagonal_moves(board)

class QueenPiece(Piece):
    def __init__(self, sprites, color, xpos, ypos):
        spr = SPR_QUEEN
        if color == COLOR_BLACK:
            spr += SPR_BLACK
        super().__init__(sprites[spr], color, xpos, ypos)

    def legal_moves(self, board):
        card = self._legal_cardinal_moves(board)
        diag = self._legal_diagonal_moves(board) 
        card.extend(diag)
        return card

class KingPiece(Piece):
    def __init__(self, sprites, color, xpos, ypos):
        spr = SPR_KING
        if color == COLOR_BLACK:
            spr += SPR_BLACK
        super().__init__(sprites[spr], color, xpos, ypos)

    def legal_moves(self, board):
        card = self._legal_cardinal_moves(board, 1)
        diag = self._legal_diagonal_moves(board, 1) 
        card.extend(diag)
        return card
                

