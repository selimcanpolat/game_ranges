from game import Game


example_game = Game(RTP=0.94, variance=10.92)

print(example_game.house_edge(),
      example_game.max_RTP(1000000),
      example_game.min_RTP(100000))

