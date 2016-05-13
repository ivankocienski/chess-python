
import pygame as pg
import pygame.gfxdraw as gfx

from game.piece import *

class Game:

    def __init__(self, app):
        self.app = app 
        self.piece_sprites = [
                self.app.loader.load_image("piece-w-pawn.png"),
                self.app.loader.load_image("piece-w-knight.png"),
                self.app.loader.load_image("piece-w-rook.png"),
                self.app.loader.load_image("piece-w-bishop.png"),
                self.app.loader.load_image("piece-w-queen.png"),
                self.app.loader.load_image("piece-w-king.png"),

                self.app.loader.load_image("piece-b-pawn.png"),
                self.app.loader.load_image("piece-b-knight.png"),
                self.app.loader.load_image("piece-b-rook.png"),
                self.app.loader.load_image("piece-b-bishop.png"),
                self.app.loader.load_image("piece-b-queen.png"),
                self.app.loader.load_image("piece-b-king.png")]


    def reset(self):
        self.pieces = [
                PawnPiece(   self.piece_sprites, COLOR_WHITE, 0, 0),
                KnightPiece( self.piece_sprites, COLOR_WHITE, 1, 0),
                RookPiece(   self.piece_sprites, COLOR_WHITE, 2, 0),
                BishopPiece( self.piece_sprites, COLOR_WHITE, 3, 0),
                QueenPiece(  self.piece_sprites, COLOR_WHITE, 4, 0),
                KingPiece(   self.piece_sprites, COLOR_WHITE, 5, 0),

                PawnPiece(   self.piece_sprites, COLOR_BLACK, 0, 1),
                KnightPiece( self.piece_sprites, COLOR_BLACK, 1, 1),
                RookPiece(   self.piece_sprites, COLOR_BLACK, 2, 1),
                BishopPiece( self.piece_sprites, COLOR_BLACK, 3, 1),
                QueenPiece(  self.piece_sprites, COLOR_BLACK, 4, 1),
                KingPiece(   self.piece_sprites, COLOR_BLACK, 5, 1),
                ]
        pass

    def resize(self):
        pass

    def mouse_move(self, xp, yp):
        pass

    def mouse_down(self):
        pass 

    def mouse_up(self): 
        pass

    def key_down(self, key):
        pass

    def draw(self):
        self.app.screen.fill((4, 97, 144))
        self.app.screen.fill((4, 113, 168), (600, 0, 200, 600))

        xpos = 44
        ypos = 44
        for y in range(8):
            for x in range(8):
                if (x&1)^(y&1)==1:
                    self.app.screen.fill((0, 38, 58), (xpos, ypos, 64, 64))

                xpos += 64

            ypos += 64
            xpos  = 44

        pos = 44
        for x in range(9):
            gfx.line(self.app.screen, 44, pos, 556, pos, (150, 150, 150))
            gfx.line(self.app.screen, pos, 44, pos, 556, (150, 150, 150))
            pos += 64

        for piece in self.pieces:
            piece.draw(self.app.screen)

