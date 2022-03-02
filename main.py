from game import Game

poseidon_xtreme = Game(RTP=0.99, variance=10.92618497246)
ed_jones = Game(0.99, 24.12)
ed_jones_and_bosx = Game(0.99, 30.1715867)

print(poseidon_xtreme.house_edge())

