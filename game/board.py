
from game.piece import *

class Board:

    class Position:
        def __init__(self, board, x, y):
            self.piece = None
            self.xpos  = x
            self.ypos  = y
            self.board = board
            self.move_target = False
            self.highlight_for_move = False

        def set_piece(self, piece_class, color):
            self.piece = piece_class(self.board, color, self.xpos, self.ypos)

        def is_at(self, x, y):
            return self.xpos == x and self.ypos == y

        def clear_marker(self):
            self.move_target = False
            self.highlight_for_move = False

        def draw(self, screen, dx, dy):

            if self.move_target: 
                if self.piece:
                    color = (168,61,1)
                else:
                    color = (4, 144, 110)
                screen.fill(color, (dx, dy, 64, 64))

            elif (self.xpos&1)^(self.ypos&1)==1:
                # chequered BG
                screen.fill((0, 38, 58), (dx, dy, 64, 64))
            
            if self.highlight_for_move:
                gfx.rectangle(screen, (dx, dy, 64, 64), (4, 133, 168))
                gfx.rectangle(screen, (dx+1, dy+1, 62, 62), (4, 133, 168))
                
            if self.piece:
                self.piece.draw(screen, dx, dy)

    def __init__(self, loader):

        self.board = []

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

        self.board = [Board.Position(self, x, y) for y in range(8) for x in range(8)]

        array = (RookPiece, KnightPiece, BishopPiece, QueenPiece, 
                KingPiece, BishopPiece, KnightPiece, RookPiece)

        for i in range(8):
            self.position_at(i,0).set_piece(array[i],  COLOR_BLACK)
            self.position_at(i,1).set_piece(PawnPiece, COLOR_BLACK)

            self.position_at(i,6).set_piece(PawnPiece, COLOR_WHITE)
            self.position_at(i,7).set_piece(array[i],  COLOR_WHITE)

    def in_bounds(self, xpos, ypos):
        if xpos < 0 or xpos > 7:
            return False

        if ypos < 0 or ypos > 7:
            return False

        return True

    def position_at(self, xpos, ypos):
        if self.in_bounds(xpos, ypos):
            return self.board[(ypos*8)+xpos]
        return None 

    def clear_markers(self):
        for p in self.board:
            p.clear_marker()

    def draw(self, screen):

        xpos = 44
        ypos = 44
        for p in self.board:
            p.draw(screen, xpos, ypos)

            xpos += 64
            if xpos > 555:
                ypos += 64
                xpos  = 44
