import unittest
from kata.bowling.bowling import Game


class TestBowlingGame(unittest.TestCase):
	def test_all_spare(self):
		game = Game()
		for i in range(10):
			game.play(5)
			game.play(5)
		game.play(5)
		self.assertEqual(150, game.score)

	def test_all_strike(self):
		game = Game()
		for i in range(10):
			game.play(10)
		game.play(10)
		game.play(10)
		self.assertEqual(300, game.score)

	def test_miss_frame(self):
		game = Game()
		for i in range(10):
			game.play(9)
			game.play(0)
		self.assertEqual(90, game.score)


if __name__ == '__main__':
	unittest.main()