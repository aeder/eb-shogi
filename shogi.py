PIECE_TYPE = ("KING", "ROOK", "BISHOP", "GOLD_GENERAL",
              "SILVER_GENERAL", "KNIGHT", "LANCE", "PAWN")


class ShogiGame:
    def __init__(self):
        super().__init__()
        self.status = 0
        self.board = self.initialize_board()

    # When given a position, it returns the name of the piece that should be 
    # placed there at the start
    def get_piece_from_position(self, position):
        piece_postion = {
            0: "LANCE",
            1: "KNIGHT",
            2: "SILVER_GENERAL",
            3: "GOLD_GENERAL",
            4: "KING",
            5: "GOLD_GENERAL",
            6: "SILVER_GENERAL",
            7: "KNIGHT",
            8: "LANCE",
            10: "BISHOP",
            16: "BISHOP",
            18: "PAWN",
            19: "PAWN",
            20: "PAWN",
            21: "PAWN",
            22: "PAWN",
            23: "PAWN",
            24: "PAWN",
            25: "PAWN",
            26: "PAWN",
            54: "PAWN",
            55: "PAWN",
            56: "PAWN",
            57: "PAWN",
            58: "PAWN",
            59: "PAWN",
            60: "PAWN",
            61: "PAWN",
            62: "PAWN",
            64: "BISHOP",
            70: "BISHOP",
            72: "LANCE",
            73: "KNIGHT",
            74: "SILVER_GENERAL",
            75: "GOLD_GENERAL",
            76: "KING",
            77: "GOLD_GENERAL",
            78: "SILVER_GENERAL",
            79: "KNIGHT",
            80: "LANCE"
        }
        return piece_postion.get(position,"NONE")

    # Sets up the pieces in the state they should be at the start of the game
    def initialize_board(self):
        board = []
        
        for row in range(6):
            row_list = []
            for column in range(9):
                piece_type = self.get_piece_from_position(row*9+column)
                if piece_type != "NONE":
                    row_list.append(Piece([row, column], 0, piece_type))
                else:
                    row_list.append(None)
            board.append(row_list)

        for row in range(6,9):
            row_list = []
            for column in range(9):
                piece_type = self.get_piece_from_position(row*9+column)
                if piece_type != "NONE":
                    row_list.append(Piece([row, column], 1, piece_type))
                else:
                    row_list.append(None)
            board.append(row_list)

        return board 

    def draw_board(self):
        print("0 1 2 3 4 5 6 7 8")
        for row in range(9):
            line_string = " "
            for column in range(9):
                if self.board[row][column] != None:
                    string =self.board[row][column].piece_type
                    line_string = line_string + string
                else:
                    line_string = line_string + " - "
            print(line_string)
                
class Player:
    def __init__(self):
        super().__init__()


class Piece:
    def __init__(self, initial_position, owner, piece_type):
        super().__init__()
        self.current_position = initial_position
        self.current_owner = owner
        self.piece_type = piece_type

    @classmethod
    def create_valid_piece(cls, initial_position, owner, piece_type):
        return cls(initial_position, owner, piece_type)

    def move(self, new_position):
        print("piece moved from: to:")
        return self.current_position

    def promote(self):
        print("piece promoted")


current_game = ShogiGame()
current_game.draw_board()
