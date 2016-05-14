
from game.piece import *

class Board:
    def __init__(self, loader):

        self.piece_sprites = [
                loader.load_image("piece-w-pawn.png"),
                loader.load_image("piece-w-knight.png"),
                loader.load_image("piece-w-rook.png"),
                loader.load_image("piece-w-bishop.png"),
                loader.load_image("piece-w-queen.png"),
                loader.load_image("piece-w-king.png"),

                loader.load_image("piece-b-pawn.png"),
                loader.load_image("piece-b-knight.png"),
                loader.load_image("piece-b-rook.png"),
                loader.load_image("piece-b-bishop.png"),
                loader.load_image("piece-b-queen.png"),
                loader.load_image("piece-b-king.png")]
        pass

    def reset(self):

        #self.pieces = [
                #PawnPiece(   self.piece_sprites, COLOR_WHITE, 0, 0),
                #KnightPiece( self.piece_sprites, COLOR_WHITE, 1, 0),
                #RookPiece(   self.piece_sprites, COLOR_WHITE, 2, 0),
                #BishopPiece( self.piece_sprites, COLOR_WHITE, 3, 0),
                #QueenPiece(  self.piece_sprites, COLOR_WHITE, 4, 0),
                #KingPiece(   self.piece_sprites, COLOR_WHITE, 5, 0),

                #PawnPiece(   self.piece_sprites, COLOR_BLACK, 0, 1),
                #KnightPiece( self.piece_sprites, COLOR_BLACK, 1, 1),
                #RookPiece(   self.piece_sprites, COLOR_BLACK, 2, 1),
                #BishopPiece( self.piece_sprites, COLOR_BLACK, 3, 1),
                #QueenPiece(  self.piece_sprites, COLOR_BLACK, 4, 1),
                #KingPiece(   self.piece_sprites, COLOR_BLACK, 5, 1),
                #]
        self.pieces = [
                #RookPiece(   self.piece_sprites, COLOR_WHITE, 5, 5),
                #BishopPiece(   self.piece_sprites, COLOR_WHITE, 3, 3),
                KnightPiece(   self.piece_sprites, COLOR_WHITE, 3, 5),

                ]

    def find_piece_at(self, xpos, ypos):
        for p in self.pieces:
            if p.is_at(xpos, ypos):
                return p
        return None

    def in_bounds(self, xpos, ypos):
        if xpos < 0 or xpos > 7:
            return False

        if ypos < 0 or ypos > 7:
            return False

        return True

    def draw(self, screen):
        for piece in self.pieces:
            piece.draw(screen)
