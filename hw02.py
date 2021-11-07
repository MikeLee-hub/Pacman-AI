import math

from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

## Example Agent
class ReflexAgent(Agent):

  def Action(self, gameState):

    move_candidate = gameState.getLegalActions()

    scores = [self.reflex_agent_evaluationFunc(gameState, action) for action in move_candidate]
    bestScore = max(scores)
    Index = [index for index in range(len(scores)) if scores[index] == bestScore]
    get_index = random.choice(Index)

    return move_candidate[get_index]

  def reflex_agent_evaluationFunc(self, currentGameState, action):

    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    oldFood = currentGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    return successorGameState.getScore()



def scoreEvalFunc(currentGameState):

  return currentGameState.getScore()

class AdversialSearchAgent(Agent):

  def __init__(self, getFunc ='scoreEvalFunc', depth ='2'):
    self.index = 0
    self.evaluationFunction = util.lookup(getFunc, globals())

    self.depth = int(depth)

######################################################################################

class MinimaxAgent(AdversialSearchAgent):
  """
    [문제 01] MiniMax의 Action을 구현하시오. (20점)
    (depth와 evaluation function은 위에서 정의한 self.depth and self.evaluationFunction을 사용할 것.)
  """

  def Action(self, gameState):
    ####################### Write Your Code Here ################################

    def minimax_decision(gamestate):
      max_score = None
      max_action = None

      actions = gamestate.getLegalActions()

      if not actions:
        return self.evaluationFunction(gamestate)

      for action in actions:
        next_state = gamestate.generateSuccessor(0, action)
        next_value = min_value(next_state, 1, 1)
        if not max_score:
          max_score = next_value
          max_action = action
        if max_score < next_value:
          max_score = next_value
          max_action = action
      return max_action


    def max_value(gamestate, depth):
      depth += 1
      if depth > self.depth:
        return self.evaluationFunction(gamestate)
      max_score = None

      actions = gamestate.getLegalActions()

      if not actions:
        return self.evaluationFunction(gamestate)

      for action in actions:
        next_state = gamestate.generateSuccessor(0, action)
        next_value = min_value(next_state, depth, 1)
        if not max_score:
          max_score = next_value
        if max_score < next_value:
          max_score = next_value
      return max_score


    def min_value(gamestate, depth, agentIndex):
      min_score = None

      actions = gamestate.getLegalActions(agentIndex)

      if not actions:
        return self.evaluationFunction(gamestate)

      for action in actions:
        next_state = gamestate.generateSuccessor(agentIndex, action)
        if agentIndex == gamestate.getNumAgents()-1:
          next_value = max_value(next_state, depth)
        else:
          next_value = min_value(next_state, depth, agentIndex+1)
        if not min_score:
          min_score = next_value
        if min_score > next_value:
          min_score = next_value
      return min_score


    return minimax_decision(gameState)


class AlphaBetaAgent(AdversialSearchAgent):
  """
    [문제 02] AlphaBeta의 Action을 구현하시오. (25점)
    (depth와 evaluation function은 위에서 정의한 self.depth and self.evaluationFunction을 사용할 것.)
  """
  def Action(self, gameState):
    ####################### Write Your Code Here ################################

    def alpha_beta_decision(gamestate):
      alpha = -math.inf
      beta = math.inf

      max_score = None
      max_action = None

      actions = gamestate.getLegalActions()

      if not actions:
        return self.evaluationFunction(gamestate)

      for action in actions:
        next_state = gamestate.generateSuccessor(0, action)
        next_value = min_value(next_state, 1, 1, alpha, beta)

        if not max_score:
          max_score = next_value
          max_action = action
        if max_score < next_value:
          max_score = next_value
          max_action = action

        if not alpha:
          alpha = max_score
        else:
          alpha = max(alpha, max_score)

      return max_action


    def max_value(gamestate, depth, alpha, beta):
      depth += 1
      if depth > self.depth:
        return self.evaluationFunction(gamestate)
      max_score = None

      actions = gamestate.getLegalActions()

      if not actions:
        return self.evaluationFunction(gamestate)

      for action in actions:
        next_state = gamestate.generateSuccessor(0, action)
        next_value = min_value(next_state, depth, 1, alpha, beta)

        if not max_score:
          max_score = next_value
        if max_score < next_value:
          max_score = next_value

        if beta and max_score >= beta:
          break
        if not alpha:
          alpha = max_score
        else:
          alpha = max(alpha, max_score)

      return max_score


    def min_value(gamestate, depth, agentIndex, alpha, beta):
      min_score = None

      actions = gamestate.getLegalActions(agentIndex)

      if not actions:
        return self.evaluationFunction(gamestate)

      for action in actions:
        next_state = gamestate.generateSuccessor(agentIndex, action)
        if agentIndex == gamestate.getNumAgents() - 1:
          next_value = max_value(next_state, depth, alpha, beta)
        else:
          next_value = min_value(next_state, depth, agentIndex + 1, alpha, beta)

        if not min_score:
          min_score = next_value
        if min_score > next_value:
          min_score = next_value

        if alpha and min_score <= alpha:
          return min_score
        if not beta:
          beta = min_score
        else:
          beta = min(beta, min_score)
      return min_score


    return alpha_beta_decision(gameState)

    ############################################################################



class ExpectimaxAgent(AdversialSearchAgent):
  """
    [문제 03] Expectimax의 Action을 구현하시오. (25점)
    (depth와 evaluation function은 위에서 정의한 self.depth and self.evaluationFunction을 사용할 것.)
  """
  def Action(self, gameState):
    ####################### Write Your Code Here ################################

    def expectimax_decision(gamestate):
      max_score = None
      max_action = None

      actions = gamestate.getLegalActions()

      if not actions:
        return self.evaluationFunction(gamestate)

      for action in actions:
        next_state = gamestate.generateSuccessor(0, action)
        next_value = min_value(next_state, 1, 1)
        if not max_score:
          max_score = next_value
          max_action = action
        if max_score < next_value:
          max_score = next_value
          max_action = action
      return max_action


    def max_value(gamestate, depth):
      depth += 1
      if depth > self.depth:
        return self.evaluationFunction(gamestate)

      score = 0
      actions = gamestate.getLegalActions()

      if not actions:
        return self.evaluationFunction(gamestate)
      probability = 1.0 / len(actions)

      for action in actions:
        next_state = gamestate.generateSuccessor(0, action)
        next_value = min_value(next_state, depth, 1)
        score += next_value * probability
      return score


    def min_value(gamestate, depth, agentIndex):
      score = 0

      actions = gamestate.getLegalActions(agentIndex)

      if not actions:
        return self.evaluationFunction(gamestate)

      probability = 1.0 / len(actions)

      for action in actions:
        next_state = gamestate.generateSuccessor(agentIndex, action)
        if agentIndex == gamestate.getNumAgents()-1:
          next_value = max_value(next_state, depth)
        else:
          next_value = min_value(next_state, depth, agentIndex+1)
        score += next_value * probability
      return score


    return expectimax_decision(gameState)

    ############################################################################
