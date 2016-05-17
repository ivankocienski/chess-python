
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

        self.position_at(3,5).set_piece(PawnPiece, COLOR_WHITE)

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
        #self.pieces = [
                #RookPiece(   self.piece_sprites, COLOR_WHITE, 5, 5),
                #BishopPiece(   self.piece_sprites, COLOR_WHITE, 3, 3),
                #PawnPiece(   self.piece_sprites, COLOR_WHITE, 3, 5),

                #]

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
