from puissance_4  import simulate_moves

import unittest

class TestSimulation(unittest.TestCase):
    def setUp(self):

        self.initial_board = [0] * 7 * 6  
        self.config = {'rows': 6, 'columns': 7, 'inarow': 4}
        self.player = 1
        
        
    def test_possible_moves(self):
        obs = {'board': self.initial_board.copy()}
   
        possible_states = simulate_moves(obs, self.config, self.player) # la fonction a tester
        self.assertEqual(len(possible_states), self.config['columns'])
        
    def test_pas_de_move_dans_une_fulle_col(self):
        obs = {'board': self.initial_board.copy()}
        for i in range(self.config['rows']):
            self.initial_board[i * self.config['columns']] = self.player

       
        
        possible_states = simulate_moves(obs, self.config, self.player)

        for state in possible_states:
            col = state['col']
            # Calculer l'index du haut de la colonne
            top_of_column_index = (self.config['rows'] - 1) * self.config['columns'] + col
            # Vérifier que le haut de la colonne n'est pas égal à self.player
            self.assertNotEqual(state['board'][top_of_column_index], self.player)



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


 
