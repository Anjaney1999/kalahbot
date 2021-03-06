from MCTS.environment.move import Move
import numpy as np
from random import choice
from MCTS.environment.kalah import KalahEnvironment
from MCTS.agent.tree import utilities
from MCTS.agent.tree.node import Node


class MonteCarloA3CPolicies:
    def simulate(self, root: Node) -> KalahEnvironment:
        node = Node.clone(root)
        while not node.is_leaf_node():
            legal_moves = node.state.get_valid_moves()
            move_indices = []
            for move in legal_moves:
                move_indices.append(move.index)
    
            next_move = int(np.random.choice(move_indices))
            node.state.do_move(Move(side=node.state.side_to_play, index=next_move))
    
        return node.state
    
    def backpropagate(self, root: Node, final_state: KalahEnvironment):
        node = root
        while node is not None:
            side = node.parent.state.side_to_play if node.parent is not None else node.state.side_to_play  # root node
            node.update(final_state.get_reward_for_winning(side))
            node = node.parent
    
    def select(self, node: Node) -> Node:
        while not node.is_leaf_node():
            if not node.is_explored():
                return self.expand(node)
            else:
                node = utilities.select_child(node)
        return node
    
    def expand(self, parent: Node) -> Node:
        child_expansion_move = choice(tuple(parent.unexplored_moves))
        child_state = KalahEnvironment.clone(parent.state)
        child_state.do_move(child_expansion_move)
        child_node = Node(state=child_state, move=child_expansion_move, parent=parent)
        parent.put_child(child_node)
        return child_node




