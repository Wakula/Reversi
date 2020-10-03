from controller.game_controller import GameController

end_game = False
while not end_game:
    game = GameController()
    game.prepare_game()
    game.run_game()
    end_game = game.end_game()
