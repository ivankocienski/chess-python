
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

    def draw(self, screen):
        screen.blit(self.image, (56 + self.xpos * 64, 56 + self.ypos * 64))

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

