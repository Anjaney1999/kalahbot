import numpy as np
from MCTS.environment.side import Side


class Agent(object):
    def produce_action(self, state: np.array, action_mask: np.array, side_to_move: Side) -> int:
        raise NotImplementedError("produce_action method is not implemented")


class RandomAgent(Agent):
    def produce_action(self, state: np.array, action_mask: np.array, side_to_move: Side) -> int:
        legal_moves = []
        for move, _ in enumerate(action_mask):
            if action_mask[move] == 1:
                legal_moves.append(move)
        action = np.random.choice(legal_moves)
        return action