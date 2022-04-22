# Author: Tomomi Watanabe Hudspath
# GitHub username: tomomiWH
# Date: 3/11/2022
# Description: The program simulates board game called Battleship. Two players play. Each player places ships on their
# own board (10x10). First player fire a torpedo to opponent's grid square by indicating location of coordinate,
# for example B7. If there is a ship on that grid, it is a hit, other wise it is a miss. Second player fire a torpedo
# to opponent's grid square evaluates to see if it is a hit or miss. Repeat the process by player alternatively
# take their turns by firing torpedo until opponent's all the squares hit and wins the game (a player sink
# their opponent's final ship, they win.


class ShipGame:
    """
    Class represents a ShipGame. Users placing ships on their own board (10x10 grid board).
    place_ship method checks if a ship is valid to place a ship on their grid or not.
    Player first starts first. fire_torpedo method evaluates if it is a player's turn or valid move or winner already
    exits or not. If valid, records the move, updates the turn, updates the current state, and returns True.
    """
    def __init__(self):
        """
        Represents init method. Initializes private data members to use in methods to keep track things
        """

        # initialize lists for setting up board, also used to evaluate whether a entire ship can fit on player's board
        self._alpha_row = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        self._num_column = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        # hold list of coordinates, will be a key for a dictionary, used at method: setting_up_squares_for_board
        self._list_of_coordinates_for_setting_up_board = list()

        self._board = {}

        # call method to setting up board at init
        self.setting_up_squares_for_board()

        # dictionary {100 of coordinates as a key: "its respective value as empty str"}
        self._first_player_board = self.setting_up_squares_for_board()
        self._second_player_board = self.setting_up_squares_for_board()

        self._tracks_first_player_ships_on_board = {"ships on board": list()}
        self._tracks_first_player_sunken_ships_on_board = {"sunken ships": list()}

        self._tracks_second_player_ships_on_board = {"ships on board": list()}
        self._tracks_second_player_sunken_ships_on_board = {"sunken ships": list()}

        # hold list of whole piece of ship squares based on coordination, used to
        # store first or second player's ships on board dictionary at finding_squares_horizontally or vertically
        self._ship_squares = []

        self._is_subset_row = False     # check row if pieces of ship sqaures fit eintirely on the row, used at check_row method
        self._is_subset_col = False     # check column if pieces of ship saures fit eintirely on the col,  used at check_col method

        self._current_state = "UNFINISHED"
        self._whose_turn = "first"

    def setting_up_squares_for_board(self):
        """
        Purpose: The purpose of this method is to setting up 10x10 empty squares for board return as a dictionary
        return: self._board    dictionary contains 100 of coordinates as a kye and its value as empty string
        """
        alpha = self._alpha_row
        num = self._num_column
        self._list_of_coordinates_for_setting_up_board = [a + str(n) for a in alpha for n in num]
        self._board = dict.fromkeys(self._list_of_coordinates_for_setting_up_board, "")
        return self._board

    def finding_squares_horizontally(self, length_of_ship, coordinates, orientation):
        """
        Parameters:  length_of_ship - same length passes in from place_ship method
                        coordinates - same coordinates passes in from place_ship method
                        orientation - same orientation passes in from place_ship method
        Purpose: The purpose of this method is to find squares horizontally according to the length_of_ship,
        coordinates, orientation passed in from parameter
        return: self._ship_squares     ship (list of horizontal squares)
        """
        empty_squares = self._list_of_coordinates_for_setting_up_board   # list contains 100 of coordinates for squares
        count_squares = 1

        for i in range(len(empty_squares)):
            if coordinates in empty_squares[i]:
                self._ship_squares.append(coordinates)
                if orientation == "R":                                   # horizontal squares: alpha changes
                    next_square_index = i
                    while count_squares < length_of_ship:
                        next_square_index = next_square_index + 1
                        self._ship_squares.append(empty_squares[next_square_index])
                        count_squares += 1
                # print("ship R orientation", length_of_ship, coordinates, self._ship_squares)
                return self._ship_squares

    def finding_squares_vertically(self, length_of_ship, coordinates, orientation):
        """
        Parameters:  length_of_ship - same length passes in from place_ship method
                        coordinates - same coordinates passes in from place_ship method
                        orientation - same orientation passes in from place_ship method
        Purpose: The purpose of this method is to find squares vertically according to the length_of_ship,
        coordinates, orientation passed in from parameter
        return: self._ship_squares    ship (list of vertical squares)
        """
        empty_squares = self._list_of_coordinates_for_setting_up_board    # list contains 100 of coordinates for squares
        count_squares = 1

        for i in range(len(empty_squares)):
            if coordinates in empty_squares[i]:
                self._ship_squares.append(coordinates)
                if orientation == "C":                                    # vertical squares: num changes
                    next_square_index = i
                    while count_squares < length_of_ship:
                        next_square_index = next_square_index + 10
                        self._ship_squares.append(empty_squares[next_square_index])
                        count_squares += 1
                # print("ship C orientation", length_of_ship, coordinates, self._ship_squares)
                return self._ship_squares

    def check_row(self, list_squares_of_a_ship, coordinates):
        """
        Parameter - list_squares_of_a_ship  - list of coordinates of entire ship
                               coordinates  - same coordinates passes in from place_ship method
        Purpose: The purpose of this method is to evaluate if entire ship can fit on grids horizontally, orientation of R
        return: issubset returns True or False
                True  - if ship is in a row, that means ship can fit horizontally entirely (within grids)
                False - if ship is not in a row, does not entirely fit horizontally
        """
        string_coordinates = coordinates
        ship = list_squares_of_a_ship
        whole_list_of_coordinates = self._list_of_coordinates_for_setting_up_board

        a_row = whole_list_of_coordinates[0:10]
        b_row = whole_list_of_coordinates[10:20]
        c_row = whole_list_of_coordinates[20:30]
        d_row = whole_list_of_coordinates[30:40]
        e_row = whole_list_of_coordinates[40:50]
        f_row = whole_list_of_coordinates[50:60]
        g_row = whole_list_of_coordinates[60:70]
        h_row = whole_list_of_coordinates[70:80]
        i_row = whole_list_of_coordinates[80:90]
        j_row = whole_list_of_coordinates[90:100]

        # print("sliced rows", a_row, b_row, c_row, d_row, e_row, f_row, g_row, h_row, i_row, j_row)
        # print("check row for", string_coordinates, ship)
        set_ship = set(ship)

        # checks if list (ship) is a subset of another list (each row)
        if string_coordinates in a_row:
            set_row = set(a_row)
            self._is_subset_row = set_ship.issubset(set_row)
            return self._is_subset_row
        if string_coordinates in b_row:
            set_row = set(b_row)
            self._is_subset_row = set_ship.issubset(set_row)
            return self._is_subset_row
        if string_coordinates in c_row:
            set_row = set(e_row)
            self._is_subset_row = set_ship.issubset(set_row)
            return self._is_subset_row
        if string_coordinates in d_row:
            set_row = set(d_row)
            self._is_subset_row = set_ship.issubset(set_row)
            return self._is_subset_row
        if string_coordinates in e_row:
            set_row = set(e_row)
            self._is_subset_row = set_ship.issubset(set_row)
            return self._is_subset_row
        if string_coordinates in f_row:
            set_row = set(f_row)
            self._is_subset_row = set_ship.issubset(set_row)
            return self._is_subset_row
        if string_coordinates in g_row:
            set_row = set(g_row)
            self._is_subset_row = set_ship.issubset(set_row)
            return self._is_subset_row
        if string_coordinates in h_row:
            set_row = set(h_row)
            self._is_subset_row = set_ship.issubset(set_row)
            return self._is_subset_row
        if string_coordinates in i_row:
            set_row = set(i_row)
            self._is_subset_row = set_ship.issubset(set_row)
            return self._is_subset_row
        if string_coordinates in j_row:
            set_row = set(j_row)
            self._is_subset_row = set_ship.issubset(set_row)
            return self._is_subset_row

    def check_column(self, list_squares_of_a_ship, coordinates):
        """
        parameter - list_squares_of_a_ship  - list of coordinates of entire ship
        Purpose: The purpose of this method is to evaluate if a entire ship can fit on grids vertically, orientation of C
        :return: issubset returns True or False
                 True  - if each squares of a ship is in a column, that means ship can fit vertically entirely (within grids)
                 False - if ship is not in a column, does not entirely fit vertically
        """
        string_coordinates = coordinates
        ship = list_squares_of_a_ship
        whole_list_of_coordinates = self._list_of_coordinates_for_setting_up_board

        first_col = whole_list_of_coordinates[::10]
        second_col = whole_list_of_coordinates[1::10]
        third_col = whole_list_of_coordinates[2::10]
        fourth_col = whole_list_of_coordinates[3::10]
        fifth_col = whole_list_of_coordinates[4::10]
        sixth_col = whole_list_of_coordinates[5::10]
        seventh_col = whole_list_of_coordinates[6::10]
        eighth_col = whole_list_of_coordinates[7::10]
        ninth_col = whole_list_of_coordinates[8::10]
        tenth_col = whole_list_of_coordinates[9::10]

        # print(first_col, second_col, third_col, fourth_col, fifth_col, sixth_col, seventh_col, eighth_col, ninth_col, tenth_col)
        # print("check col for", string_coordinates, ship)
        set_ship = set(ship)

        # checks if list (ship) is a subset of another list (each row)
        if string_coordinates in first_col:
            set_col = set(first_col)
            self._is_subset_col = set_ship.issubset(set_col)
            return self._is_subset_col
        if string_coordinates in second_col:
            set_col = set(second_col)
            self._is_subset_col = set_ship.issubset(set_col)
            return self._is_subset_col
        if string_coordinates in third_col:
            set_col = set(third_col)
            self._is_subset_col = set_ship.issubset(set_col)
            return self._is_subset_col
        if string_coordinates in fourth_col:
            set_col = set(fourth_col)
            self._is_subset_col = set_ship.issubset(set_col)
            return self._is_subset_col
        if string_coordinates in fifth_col:
            set_col = set(fifth_col)
            self._is_subset_col = set_ship.issubset(set_col)
            return self._is_subset_col
        if string_coordinates in sixth_col:
            set_col = set(sixth_col)
            self._is_subset_col = set_ship.issubset(set_col)
            return self._is_subset_col
        if string_coordinates in seventh_col:
            set_col = set(seventh_col)
            self._is_subset_col = set_ship.issubset(set_col)
            return self._is_subset_col
        if string_coordinates in eighth_col:
            set_col = set(eighth_col)
            self._is_subset_col = set_ship.issubset(set_col)
            return self._is_subset_col
        if string_coordinates in ninth_col:
            set_col = set(ninth_col)
            self._is_subset_col = set_ship.issubset(set_col)
            return self._is_subset_col
        if string_coordinates in tenth_col:
            set_col = set(tenth_col)
            self._is_subset_col = set_ship.issubset(set_col)
            return self._is_subset_col

    def place_ship(self, player, length_of_ship, coordinates, orientation):
        """
        Parameters:
            player           - player (first or second) places a ship
            length_of_ships  - length of ship (integer)
            coordinates      - location on board user wanting ship to be placed on that player's board
            orientation      - direction of ship user wanting to be placed on that player's board 'R' row or 'C' column

        Purpose:  The purpose of this method is to placing ships, user (each player) to place their own ships with
        the location (horizontally 'R' or vertically 'C'). Evaluates if the ship can be placed on that player's board or not.
        The method will be called before any other methods besides init.

        Returns:
            False - if a ship does not entirely fit on that player's grid, or
                    if a ship overlaps from previously placed ships, or
                    if the length of ship is less than 2
             True - (if above condition did not meet)
                    ship should be added to that player's board
        """
        list_of_coordinates = self._list_of_coordinates_for_setting_up_board
        if coordinates not in list_of_coordinates:
            return False

        if length_of_ship < 2:
            return False

        if orientation == "R":
            # HORIZONTAL ORIENTATION process
            self.finding_squares_horizontally(length_of_ship, coordinates, orientation)
            # method to checks entire ship can fit on the board horizontally
            self.check_row(self._ship_squares, coordinates)
            if not self._is_subset_row:
                return False
            else:
                # print("ship would fit entirely on the row", self._is_subset_row)
                if player == "first":
                    for each_ship_square_coordinates in self._ship_squares:
                        # evaluate if each ship square key exits on board AND not previously placed
                        if each_ship_square_coordinates in self._first_player_board.keys() and \
                                self._first_player_board[each_ship_square_coordinates] != "X":
                            # update dictionary coordinates as key and with its value "X"
                            self._first_player_board.update({each_ship_square_coordinates: "X"})
                        else:
                            return False
                    # data structures to track only ships on board
                    adding_to_a_dictionary = dict.fromkeys(self._ship_squares, "X")
                    self._tracks_first_player_ships_on_board["ships on board"].append(adding_to_a_dictionary)
                    # print("tracks entire ship first player", self._tracks_first_player_ships_on_board, "\n")
                    self._ship_squares = []
                    return True

                if player == "second":
                    for each_ship_square_coordinates in self._ship_squares:
                        # method to checks entire ship can fit on the board horizontally
                        if each_ship_square_coordinates in self._second_player_board.keys() and \
                                self._second_player_board[each_ship_square_coordinates] != "X":
                            # update dictionary coordinates as key and with its value "X"
                            self._second_player_board.update({each_ship_square_coordinates: "X"})
                        else:
                            return False
                    # data structures to track only ships on board
                    adding_to_a_dictionary = dict.fromkeys(self._ship_squares, "X")
                    self._tracks_second_player_ships_on_board["ships on board"].append(adding_to_a_dictionary)
                    # print("tracks entire ship second player", self._tracks_second_player_ships_on_board, "\n")
                    self._ship_squares = []
                    return True

        elif orientation == "C":
            # VERTICAL ORIENTATION process
            self.finding_squares_vertically(length_of_ship, coordinates, orientation)
            self.check_column(self._ship_squares, coordinates)
            if not self._is_subset_col:
                return False
            else:
                # print("ship would fit entirely on the col", self._is_subset_col)
                if player == "first":
                    for each_ship_square_coordinates in self._ship_squares:
                        # evaluate if each ship square key exits on board AND not previously placed
                        if each_ship_square_coordinates in self._first_player_board.keys() and \
                                self._first_player_board[each_ship_square_coordinates] != "X":
                            # update dictionary coordinates as key and with its value "X"
                            self._first_player_board.update({each_ship_square_coordinates: "X"})
                        else:
                            return False
                    adding_to_a_dictionary = dict.fromkeys(self._ship_squares, "X")
                    self._tracks_first_player_ships_on_board["ships on board"].append(adding_to_a_dictionary)
                    # print("tracks entire ship first player", self._tracks_first_player_ships_on_board, "\n")
                    self._ship_squares = []
                    return True

                if player == "second":
                    for each_ship_square_coordinates in self._ship_squares:
                        # evaluate if each ship square key exits on board AND not previously placed
                        if each_ship_square_coordinates in self._second_player_board.keys() and \
                                self._second_player_board[each_ship_square_coordinates] != "X":
                            # update dictionary coordinates as key and with its value "X"
                            self._second_player_board.update({each_ship_square_coordinates: "X"})
                        else:
                            return False
                    adding_to_a_dictionary = dict.fromkeys(self._ship_squares, "X")
                    self._tracks_second_player_ships_on_board["ships on board"].append(adding_to_a_dictionary)
                    # print("tracks entire ship second player", self._tracks_second_player_ships_on_board, "\n")
                    self._ship_squares = []
                    return True

    def get_current_state(self):
        """
        Parameter: no parameter
        Purpose: The purpose of this method is to return current state of the game
        (self._current_state_of_the_game) which contains values 'FIRST_WON', 'SECOND_WON', or 'UNFINISHED'.
        """
        return self._current_state

    def switch_players_turn(self):
        """
        PARAMETER -  no parameter
        Purpose: The purpose of this method is if firing torpedo was done, switch player's turn
        return: not returning anything
        called by method - fire_torpedo   only firing torpedo is successful call this method at fire_torpedo
        """
        if self._whose_turn == "first":
            self._whose_turn = "second"

        elif self._whose_turn == "second":
            self._whose_turn = "first"

    def fire_torpedo(self, player_firing, coordinates_of_the_target_square):
        """
        Parameters:
            player_firing - which player (first or second) firing
            coordinates_of_the_target_square - coordinates on the opponent's grids that player is firing torpedo to

        Purpose:  The purpose of this method is to evaluate if player's turn to firing torpedo or not,
        evaluates that if game has already won or not,
        evaluates if coordinate of the target square is hit or miss if it is a hit record the move,
        update whose turn it is and update the current state.
        place_ship will not be called after firing of the torpedo has started.

        Returns:
            False - If it's not that player's turn, or
                    if the game has already been won,
            True  - (if above condition did not meet)
                    it should record the move,
                    update whose turn it is,
                    update the  current state (if this turn sank the opponent's final ship),
                    If that player has fired on that square before, that's not illegal - it just wastes a turn.
        Notes to remember: Check coordination, if player firing the coordinates where ship does not exits, still return True
        """
        if self._whose_turn == "first" and player_firing == "first":
            if coordinates_of_the_target_square in self._second_player_board.keys():
                # print(self._whose_turn, player_firing, "fired torpedo to second's board ", coordinates_of_the_target_square)
                # update the dictionary board with value "H"
                self._second_player_board.update({coordinates_of_the_target_square: "H"})
                for key, val_list_of_ship in self._tracks_second_player_ships_on_board.items():
                    for inner_dictionary_ship in val_list_of_ship:
                        if coordinates_of_the_target_square in inner_dictionary_ship:
                            inner_dictionary_ship[coordinates_of_the_target_square] = "H"
                            # print("inner dict values", inner_dictionary_ship.values()) # evaluate all values are "H"
                            if all(all_values_of_ship == "H" for all_values_of_ship in inner_dictionary_ship.values()):
                                self._tracks_second_player_sunken_ships_on_board["sunken ships"].append(inner_dictionary_ship)
                                for index in range(len(val_list_of_ship)):
                                    if coordinates_of_the_target_square in val_list_of_ship[index]:
                                        #print("second player's ships on board list \n", "index to remove", index, val_list_of_ship[index],  "from", self._tracks_second_player_ships_on_board)
                                        del val_list_of_ship[index]
                                        break
                                # print("updated after removal", self._tracks_second_player_ships_on_board)
                                self._current_state = "FIRST_WON"
                                return False
            self.switch_players_turn()  # update whose turn it is
            return True

        elif self._whose_turn == "second" and player_firing == "second":
            # print(self._whose_turn, player_firing, "player hitting first board", coordinates_of_the_target_square)
            if coordinates_of_the_target_square in self._first_player_board.keys():
                # print(self._whose_turn, player_firing, "fired torpedo to first's board ", coordinates_of_the_target_square)
                # update the dictionary board with value "H"
                self._first_player_board.update({coordinates_of_the_target_square: "H"})
                for key, val_list_of_ship in self._tracks_first_player_ships_on_board.items():
                    for inner_dictionary_ship in val_list_of_ship:
                        if coordinates_of_the_target_square in inner_dictionary_ship:
                            inner_dictionary_ship[coordinates_of_the_target_square] = "H"
                            # print("inner dict values", inner_dictionary_ship.values()) # evaluate all values are "H"
                            if all(all_values_of_ship == "H" for all_values_of_ship in inner_dictionary_ship.values()) is True:
                                self._tracks_first_player_sunken_ships_on_board["sunken ships"].append(inner_dictionary_ship)
                                for index in range(len(val_list_of_ship)):
                                    if coordinates_of_the_target_square in val_list_of_ship[index]:
                                        # print("first player's ships on board list \n", "index to remove",  index, val_list_of_ship[index],  coordinates_of_the_target_square, "from", self._tracks_first_player_ships_on_board)
                                        del val_list_of_ship[index]
                                        break
                                # print("updated after removal", self._tracks_first_player_ships_on_board)
                                self._current_state = "SECOND_WON"
                                return False
            self.switch_players_turn()     # update whose turn it is
            return True
        else:
            # print("return FALSE, not that player's turn or the game has already been won")
            return False

    def get_num_ships_remaining(self, player):
        """
        Parameters: player - first or second
        Purpose:  The purpose of this method is to return how many ships the specified player has left
        Return: number of ships left of that player
        """
        if player == "first":
            list_remaining_ships_first_player = self._tracks_first_player_ships_on_board["ships on board"]
            num_first_remaining_ship = len(list_remaining_ships_first_player)
            # print("first player remaining ships",  num_first_remaining_ship, "\n", "tracks first player's ships on board ", self._tracks_first_player_ships_on_board)
            return num_first_remaining_ship

        elif player == "second":
            list_remaining_ships_second_player = self._tracks_second_player_ships_on_board["ships on board"]
            num_second_remaining_ship = len(list_remaining_ships_second_player)
            # print("second player remaining ships", num_second_remaining_ship, "\n", "tracks second player's ships on board", self._tracks_second_player_ships_on_board )
            return num_second_remaining_ship

def main():
    # Test Code
    game = ShipGame()
    # game.setting_up_empty_squares_for_board()
    # game.finding_squares_vertically('first', 5, 'B2', 'C')
    # game.finding_squares_horizontally('first', 4, 'I8', 'R')
    game.place_ship('first', 5, 'B2', 'C')
    game.place_ship('first', 2, 'I8', 'R')
    game.place_ship('second', 3, 'H2', 'C')
    game.place_ship('second', 2, 'A1', 'C')
    game.place_ship('first', 8, 'H2', 'R')

    game.fire_torpedo('first', 'H3')
    game.fire_torpedo('second', 'A1')

    game.fire_torpedo('first', 'A8')
    game.fire_torpedo('second', 'I8')
    # game.fire_torpedo('first', 'J2')
    # game.fire_torpedo('second', 'D3')
    # game.fire_torpedo('first', 'A1')
    # game.fire_torpedo('second', 'D4')
    # game.fire_torpedo('first', 'B1')

    print(game.get_current_state())

    game.get_num_ships_remaining('first')
    game.get_num_ships_remaining('second')


if __name__ == "__main__":
    main()

