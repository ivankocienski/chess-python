
import pygame as pg
import pygame.gfxdraw as gfx

from game.piece import *
from game.board import *

class Game:

    def __init__(self, app):
        self.app       = app 
        self.font      = self.app.loader.default_font()
        self.hover_x   = -1
        self.hover_y   = -1
        self.board     = Board(self.app.loader)

        self.move_from_pos = None

        self.white_move_count    = 0
        self.white_capture_count = 0
        self.black_move_count    = 0
        self.black_capture_count = 0

    def reset(self):
        self.current_player = COLOR_WHITE
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
        if self.move_from_pos:

            move_to_pos = self.board.position_at(self.hover_x, self.hover_y)
            if move_to_pos:

                if move_to_pos.move_target and move_to_pos != self.move_from_pos:

                    if move_to_pos.piece:
                        if self.current_player == COLOR_WHITE:
                            self.white_capture_count += 1
                        else:
                            self.black_capture_count += 1

                    self.move_from_pos.piece.move_to(self.hover_x, self.hover_y)

                    if self.current_player == COLOR_WHITE:
                        self.white_move_count += 1
                    else:
                        self.black_move_count += 1

                self.current_player = -self.current_player
                self.board.clear_markers()
                self.move_from_pos = None

        else: # move_piece is None
            from_pos = self.board.position_at(self.hover_x, self.hover_y)
            if bool(from_pos.piece) and from_pos.piece.color == self.current_player:
                self.move_from_pos = from_pos
                self.move_from_pos.highlight_for_move = True

                piece = from_pos.piece
                for mt in piece.legal_moves(self.board):
                    to_pos = self.board.position_at(mt[0], mt[1])
                    if to_pos.piece and to_pos.piece.color == from_pos.piece.color:
                        # can't capture own pieces
                        continue

                    to_pos.move_target = True
                    
                print("piece=%s"%from_pos.piece)
            else:
                self.board.clear_markers()
                self.move_from_pos = None

        
        self.app.repaint()

    def mouse_up(self): 
        pass

    def key_down(self, key):
        pass

    def draw(self):
        self.app.screen.fill((4, 97, 144))
        self.app.screen.fill((4, 113, 168), (600, 0, 200, 600))

        self.board.draw(self.app.screen) 
        
        #if self.hover_x >= 0 and self.hover_y >= 0:
        #    self.app.draw_text(self.font, 622, 44, "x=%d y=%d"%(self.hover_x, self.hover_y), (255,255,255))

        if self.current_player == COLOR_WHITE:
            self.app.draw_text(self.font, 622, 300, "White turn", (255,255,255))
        else:
            self.app.draw_text(self.font, 622, 300, "Black turn", (255,255,255))

        self.app.draw_text(self.font, 622, 100, "Black Moves %d"    % self.black_move_count, (255,255,255))
        self.app.draw_text(self.font, 622, 120, "Black Captures %d" % self.black_capture_count, (255,255,255))

        self.app.draw_text(self.font, 622, 500, "White Moves %d"    % self.white_move_count, (255,255,255))
        self.app.draw_text(self.font, 622, 520, "White Captures %d" % self.white_capture_count, (255,255,255))
        
