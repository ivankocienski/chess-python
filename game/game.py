
import pygame as pg
import pygame.gfxdraw as gfx

from game.piece import *
from game.board import *

class Game:

    def __init__(self, app):
        self.app = app 
        self.font = self.app.loader.default_font()
        self.hover_x = -1
        self.hover_y = -1
        self.board = Board(self.app.loader)

        self.move_piece  = None
        self.move_targets = []

    def reset(self):
        self.board.reset()

    def resize(self):
        pass

    def mouse_move(self, xp, yp):
        xp -= 44
        if xp < 0 or xp > 512:
            self.hover_x = -1
            return

        self.hover_x = int(xp / 64)

        yp -= 44
        if yp < 0 or yp > 512:
            self.hover_y = -1
            return

        self.hover_y = int(yp / 64)
        self.app.repaint()

    def mouse_down(self):
        if self.move_piece:

            # deselect selected piece
            if self.move_piece.is_at(self.hover_x, self.hover_y):
                self.move_targets = ()
                self.move_piece.about_to_move(False)
                self.move_piece = None

            else:
                # possibly move selected piece 
                can_move = False
                for mt in self.move_targets:
                    if self.hover_x == mt[0] and self.hover_y == mt[1]:
                        can_move = True
                        break

                if can_move:
                    self.move_piece.move_to(self.hover_x, self.hover_y)
                    self.move_targets = ()
                    self.move_piece.about_to_move(False)
                    self.move_piece = None


        else: # move_piece is None
            piece = self.board.find_piece_at(self.hover_x, self.hover_y)
            if bool(piece):
                self.move_piece = piece
                self.move_targets = piece.legal_moves(self.board)
                print("piece=%s"%piece)
                piece.about_to_move()
            else:
                self.move_piece   = None
                self.move_targets = ()

        
        self.app.repaint()

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

        #pos = 44
        #for x in range(9):
        #    gfx.line(self.app.screen, 44, pos, 556, pos, (150, 150, 150))
        #    gfx.line(self.app.screen, pos, 44, pos, 556, (150, 150, 150))
        #    pos += 64

        for mt in self.move_targets:
            dx = 44 + mt[0] * 64
            dy = 44 + mt[1] * 64

            self.app.screen.fill((4, 144, 110), (dx, dy, 64, 64))


        self.board.draw(self.app.screen)
        
        
        if self.hover_x >= 0 and self.hover_y >= 0:
            self.app.draw_text(self.font, 622, 44, "x=%d y=%d"%(self.hover_x, self.hover_y), (255,255,255))
