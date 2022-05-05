from game import Directions
import busters
from wekaI import Weka

def chooseAction2(self, gameState):
    # code for automatic agent
    action = Directions.STOP
    legal = gameState.getLegalActions(0)
    pacmanX = gameState.getPacmanPosition()[0]
    pacmanY = gameState.getPacmanPosition()[1]
    ghostPositions = gameState.getGhostPositions()
    ghost1X = ghostPositions[0][0]
    ghost1Y = ghostPositions[0][1]
    ghost2Y = ghostPositions[1][1]
    ghost3Y = ghostPositions[2][1]

    x = [pacmanX, pacmanY, ghost1X, ghost1Y, ghost2Y,
         ghost3Y, gameState.getNumFood(), gameState.getScore(), 'Action']
    action = self.weka.predict('Tutorial1Agent_Wrapper.model',
                               x, 'training_tutorial1_wrapper.arff')
    #if action not in legal:
    #    action = self.chooseAction(gameState) #or 'Stop'
    return action
