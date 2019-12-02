import math

PIECE_TYPE = ("KING", "ROOK", "BISHOP", "GOLD_GENERAL",
              "SILVER_GENERAL", "KNIGHT", "LANCE", "PAWN")


class ShogiGame:
    def __init__(self):
        super().__init__()
        self.status = 0
        self.current_player = 0
        self.board = self.initialize_board2()

    # When given a position, it returns the name of the piece that should be
    # placed there at the start
    def get_piece_from_position(self, position):
        piece_position = {
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
        return piece_position.get(position, "NONE")

    # Sets up the pieces in the state they should be at the start of the game
    def initialize_board(self):
        board = []

        for row in range(6):
            row_list = []
            for column in range(9):
                piece_type = self.get_piece_from_position(row*9+column)
                if piece_type != "NONE":
                    row_list.append(Piece.create_valid_piece(
                        [row, column], 0, piece_type))
                else:
                    row_list.append(None)
            board.append(row_list)

        for row in range(6, 9):
            row_list = []
            for column in range(9):
                piece_type = self.get_piece_from_position(row*9+column)
                if piece_type != "NONE":
                    row_list.append(Piece.create_valid_piece(
                        [row, column], 1, piece_type))
                else:
                    row_list.append(None)
            board.append(row_list)

        return board

    def initialize_board2(self):
        board = []

        for row in range(6):
            for column in range(9):
                piece_type = self.get_piece_from_position(row*9+column)
                if piece_type != "NONE":
                    board.append(Piece.create_valid_piece(
                        [row, column], 0, piece_type))

        for row in range(6, 9):
            for column in range(9):
                piece_type = self.get_piece_from_position(row*9+column)
                if piece_type != "NONE":
                    board.append(Piece.create_valid_piece(
                        [row, column], 1, piece_type))
        return board

    def draw_board2(self):
        print("   0  1  2  3  4  5  6  7  8")
        print("+-----------------------------+")
        for row in range(9):
            line_string = str(row) + "| "
            for column in range(9):
                piece = next(
                    (x for x in self.board if x.current_position == [row, column]), None)
                if piece != None:
                    string = piece.get_piece_symbol()
                    line_string = line_string + string + " "
                else:
                    line_string = line_string + "   "
            line_string = line_string + "|"
            print(line_string)
        print("+-----------------------------+")
        
        if self.current_player == 0:
            print("=========== White(v) ===========")
        elif self.current_player ==1:
            print("=========== Black(^) ===========")
        

    def draw_board(self):
        print("   0  1  2  3  4  5  6  7  8")
        print("+-----------------------------+")
        for row in range(9):
            line_string = str(row) + "| "
            for column in range(9):
                if self.board[row][column] != None:
                    string = self.board[row][column].get_piece_symbol()
                    line_string = line_string + string + " "
                else:
                    line_string = line_string + "   "
            line_string = line_string + "|"
            print(line_string)
        print("+-----------------------------+")

    def play_turn(self):

        valid_piece = False
        valid_move = False

        while (valid_piece == False or valid_move == False):

            print("Move from?: [row,column]:")
            piece_location = input()
            y1, x1 = piece_location.split(",")
            selected_piece = next(
                x for x in self.board if x.current_position == [int(y1), int(x1)])

            if (selected_piece.current_owner == self.current_player):
                valid_piece = True
                print("To?: [row,column]")
                piece_destination = input()
                y2, x2 = piece_destination.split(",")
                movement_result = selected_piece.move([int(y2), int(x2)])

                if movement_result == [int(y2), int(x2)]:
                    valid_move = True
                else:
                    valid_move = False
                    valid_piece = False
            else:
                print ("That piece doesn't belong to you")

            
        if self.current_player == 0:
            self.current_player = 1
        elif self.current_player == 1:
            self.current_player = 0
        print("========= End of turn ==========")


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

    def calculate_direction(self, first_position, second_position):
        coordinates_difference = [
            second_position[0] -
            first_position[0], second_position[1] - first_position[1]
        ]

        # Position order = Y,X
        if coordinates_difference[0] < 0 and coordinates_difference[1] < 0:
            return "NW"
        if coordinates_difference[0] < 0 and coordinates_difference[1] == 0:
            return "N"
        if coordinates_difference[0] < 0 and coordinates_difference[1] > 0:
            return "NE"
        if coordinates_difference[0] == 0 and coordinates_difference[1] > 0:
            return "W"
        if coordinates_difference[0] > 0 and coordinates_difference[1] > 0:
            return "SW"
        if coordinates_difference[0] > 0 and coordinates_difference[1] == 0:
            return "S"
        if coordinates_difference[0] > 0 and coordinates_difference[1] < 0:
            return "SE"
        if coordinates_difference[0] == 0 and coordinates_difference[1] < 0:
            return "E"

    def calculate_distance(self, first_position, second_position):
        distance = math.sqrt(
            (first_position[0] - second_position[0]) ** 2 + (first_position[1] - second_position[1]) ** 2)
        return distance

    # function that moves the piece according to type
    def move(self, new_position):
        if 0 <= new_position[0] <= 9 or 0 <= new_position[1] <= 9:
            print(str(self.piece_type)+" moved from:" +
                  str(self.current_position))
            movement_direction = self.calculate_direction(
                self.current_position, new_position)
            movement_distance = self.calculate_distance(
                self.current_position, new_position)
            print("Distance: " + str(movement_distance) +
                  " Direction: " + movement_direction)
            if self.piece_type == "KING":
                if 0 > movement_distance <= math.sqrt(2):
                    self.current_position = new_position
            elif self.piece_type == "ROOK":
                if movement_direction == "N" or movement_direction == "W" or movement_direction == "E" or movement_direction == "S":
                    self.current_position = new_position
            elif self.piece_type == "BISHOP":
                if movement_direction == "NW" or movement_direction == "NE" or movement_direction == "SE" or movement_direction == "SW":
                    self.current_position = new_position
            elif self.piece_type == "GOLD_GENERAL":
                if 0 > movement_distance <= math.sqrt(2):
                    if self.current_owner == 0:
                        if movement_direction != "NW" and movement_direction != "NE":
                            self.current_position = new_position
                    elif self.current_owner == 1:
                        if movement_direction != "SW" and movement_direction != "SE":
                            self.current_position = new_position
            elif self.piece_type == "SILVER_GENERAL":
                if 0 > movement_distance <= math.sqrt(2):
                    if self.current_owner == 0:
                        if movement_direction != "E" and movement_direction != "W" and movement_direction != "N":
                            self.current_position = new_position
                    elif self.current_owner == 1:
                        if movement_direction != "E" and movement_direction != "W" and movement_direction != "S":
                            self.current_position = new_position
            elif self.piece_type == "KNIGHT":
                if self.current_owner == 0:
                    if self.current_position[0] - new_position[0] == 2 and self.current_position[1] - new_position[1] == -1 or self.current_position[1] - new_position[1] == 1:
                        self.current_position = new_position
                elif self.current_owner == 1:
                    if self.current_position[0] - new_position[0] == -2 and self.current_position[1] - new_position[1] == -1 or self.current_position[1] - new_position[1] == 1:
                        self.current_position = new_position
            elif self.piece_type == "LANCE":
                if self.current_owner == 0:
                    if movement_direction == "S":
                        self.current_position = new_position
                if self.current_owner == 1:
                    if movement_direction == "N":
                        self.current_position = new_position
            elif self.piece_type == "PAWN":
                if movement_distance <= 1:
                    if self.current_owner == 0:
                        if movement_direction == "S":
                            self.current_position = new_position
                    if self.current_owner == 1:
                        if movement_direction == "N":
                            self.current_position = new_position
            print("to:" + str(self.current_position))
            return self.current_position
        else:
            print("Position out of valid range")
        return self.current_position

    def promote(self):
        print("TODO: piece promoted")

    def get_piece_symbol(self):
        piece_symbol = ""
        if self.piece_type == "KING":
            piece_symbol = piece_symbol + "K"
        elif self.piece_type == "ROOK":
            piece_symbol = piece_symbol + "R"
        elif self.piece_type == "BISHOP":
            piece_symbol = piece_symbol + "B"
        elif self.piece_type == "GOLD_GENERAL":
            piece_symbol = piece_symbol + "G"
        elif self.piece_type == "SILVER_GENERAL":
            piece_symbol = piece_symbol + "S"
        elif self.piece_type == "KNIGHT":
            piece_symbol = piece_symbol + "N"
        elif self.piece_type == "LANCE":
            piece_symbol = piece_symbol + "L"
        elif self.piece_type == "PAWN":
            piece_symbol = piece_symbol + "P"

        if self.current_owner == 0:
            piece_symbol = piece_symbol + "v"
        elif self.current_owner == 1:
            piece_symbol = piece_symbol + "^"

        return piece_symbol


current_game = ShogiGame()
current_game.draw_board2()
while(current_game.status == 0):
    current_game.play_turn()
    current_game.draw_board2()
