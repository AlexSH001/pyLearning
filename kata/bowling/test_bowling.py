import unittest
from bowling import Game


class TestBowlingGame(unittest.TestCase):
	def all_spare(self):
		game = Game()
		for i in range(10):
			game.play(5)
			game.play(5)
		game.play(5)
		self.assertEqual(game.score, 150)

	def all_strike(self):
		game = Game()
		for i in range(10):
			game.play(10)
		game.play(10)
		game.play(10)
		self.assertEqual(game.score, 300)

	def miss_frame(self):
		game = Game()
		for i in range(10):
			game.play(9)
			game.play(0)
		self.assertEqual(game.score, 90)


if __name__ == '__main__':
	unittest.main()