
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

class BishopPiece(Piece):
    def __init__(self, sprites, color, xpos, ypos):
        spr = SPR_BISHOP
        if color == COLOR_BLACK:
            spr += SPR_BLACK
        super().__init__(sprites[spr], xpos, ypos)

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

