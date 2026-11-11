# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # Initializing the stack and visited set
    stack = util.Stack()
    visited = set()

    # Pushing the start state onto the stack
    stack.push((problem.getStartState(), []))

    # Loop until the stack is empty
    while not stack.isEmpty():
        # Pop the top state from the stack along with the actions taken to reach that state
        state, actions = stack.pop()

        # Check if the current state is the goal state
        if problem.isGoalState(state):
            return actions

        # Add the current state to the visited set
        visited.add(state)

        # Expand the current state and push the child states onto the stack
        for child_state, action, _ in problem.expand(state):
            if child_state not in visited:
                stack.push((child_state, actions + [action]))

    return []


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Initializing the queue and visited set
    frontier = util.Queue()

    startNode = (problem.getStartState(), 0, [])  # start contains node, cost, and path

    frontier.push(startNode)

    expanded = set()



    while not (frontier.isEmpty()):

        (node, cost, path) = frontier.pop()

        if problem.isGoalState(node):

            return path

        if not (node in expanded):

            expanded.add(node)

            for next_node, next_action, next_cost in problem.expand(node):

                totalCost = cost + next_cost

                totalPath = path + [next_action]

                totalState = (next_node, totalCost, totalPath)

                frontier.push(totalState)




    util.raiseNotDefined()



def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Initialize the priority queue with start state and cost 0
    queue = util.PriorityQueue()
    queue.push((problem.getStartState(), [], 0), 0)
    
    # Initialize visited set
    visited = set()
    
    while not queue.isEmpty():
        state, actions, cost = queue.pop()
        
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.add(state)
            
            for child_state, action, step_cost in problem.expand(state):
                new_actions = actions + [action]
                new_cost = cost + step_cost
                queue.push((child_state, new_actions, new_cost), new_cost)
    
    return []


def heuristic(state, problem):
    """
    A heuristic function that estimates the cost from the current state to the nearest goal.
    In this example, we can assume the problem provides a method called 'getGoalState'
    to retrieve the goal state.
    """
    goal_state = problem.getGoalState()
    # Calculate the heuristic value based on the state and the goal state
    heuristic_value = ...  # Calculate the heuristic value here
    return heuristic_value

def aStarSearch(problem, heuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    # Initialize the priority queue with start state and cost 0
    queue = util.PriorityQueue()
    start_state = problem.getStartState()
    queue.push((start_state, [], 0), 0 + heuristic(start_state, problem))  # Total cost = g + h
    
    # Initialize visited set
    visited = set()
    
    while not queue.isEmpty():
        state, actions, cost = queue.pop()
        
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.add(state)
            
            for child_state, action, step_cost in problem.expand(state):
                new_actions = actions + [action]
                new_cost = cost + step_cost
                total_cost = new_cost + heuristic(child_state, problem)  # Total cost = g + h
                queue.push((child_state, new_actions, new_cost), total_cost)
    
    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
