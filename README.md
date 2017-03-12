# HEX_AI

Using some techniques learned in the AI course at Universidad EAFIT, a intelligent agent was implemented to play the HEX game.

## Table of contents
  * [Dependencies.](#dependencies)
  * [Clarifications.](#clarifications)
  * [Usage.](#usage)

## Dependencies
- [Python] 3.6.0

## Clarifications
  - The name of the main class is Agente_AlejandroS_AlejandroC.
  - The main class has a method called ``get_action_to_take(state, current_player)``, where the first parameter is the current state of the game and the second one is the player who has to take an action.
  - The state is a list of lists, so that ``state[i][j]`` corresponds to the piece owner for that position. If the value is 0 (zero), that means that there is no piece on that position, a 1 means that the piece on that position belongs to Player 1 and a 2 indicates that Player 2 is the owner of the piece in question.
  - Player 1 has red pieces and he wins vertically, i.e. he wants to connect the bottom and the top of the game board. On the other hand, Player 2 has blue pieces and he wins horizontally, i.e. he wants to connect the left and right sides of the game board.
  -  The method ``get_action_to_take(state, current_player)`` returns a list with two items indicating the position where the ``current_player`` wants to put his piece. For example, if the returned value is ``[4, 5]``, the ``current_player`` wants to put his piece on the intersection between the fourth row and the fifth column.

## Techniques
The agent uses four techniques learnes in the AI course at Universidad EAFIT to improve performance in an strategic way:
  - **MiniMax**: Hex is an adversarial game where every player is trying to occupy the most strategic positions on the board. With every action that Player 1 takes, he is trying to maximize his reward considering the future behavior of  Player 2, who will be trying to negatively affect Player 1 minimizing that reward. In this case, both players are supposed to play optimally. 
  - **Alpha-Beta Pruning**: Due to the time constraint and considering that sometimes it is not necessary to visit all the nodes, this intelligent agent uses Alpha-Beta Pruning. Using this technique it is possible to limit the states that have to be evaluated in order to eliminate branches without analyzing them, because it can be known in advance that they are not going to influence the decisions in the top levels.
  - **Iterative Deepening**: The high branching factor of HEX makes it impossible to visit the whole game tree at once. Thus, a maximum depth was predefined to treat states on the maximum depth as leaves and invoke the evaluation function from there. As the number of turns increments, there are less possible states to analyze. That's why it is good to increment the maximum depth at certain times during the game to take more intelligent actions.
  - **DFS**: This technique was used as the most important part of the evaluation function. DFS allows the agent to explore every path of connected own pieces from a given start position (i.e. a state to evaluate) and let him know the maximum and minimum level that could be reached, according to the game board, following those paths in his win direction. As the difference between the maximum and minimum levels increases, the agent prefers the position in question because he knows that putting a piece there guarantees a larger path that is closer to the victory.

It is needed to use an evaluation function because it is not possible to calculate the MiniMax until the end due to the high branching factor (b = 100) of this particular game. The evaluation function combines: DFS, [Virtual Connections] and Adjacent own pieces.

> When there is a tie for two states (meaning it is the same to the player to select any of both positions), the privileged position is the one that is nearer to the central column (if the agent wins vertically) or to the central row (if the agent wins horizontally).

> A restriction for the agent was to decide the action in less than 5 seconds. Thus, a timeout was used for this purpose to select the best possible action evaluated within the time constraint.

The following link contains an explanation of the techniques used to implement the intelligent agent, telling why they were used and what is the strategic purpose behind: [YouTube Video].

### Usage
This section is specific for the teacher of the AI course at Universidad EAFIT.

1. Copy the file named **"Agente_AlejandroS_AlejandroC"** to the folder where your Jupyter Notebook file is. 

2. In your Jupyter Notebook file, add the following line to your imports on the top.

    ```ssh
    from Agente_AlejandroS_AlejandroC import AgenteAlejandroSAlejandroC
    ```

3. Then, instantiate the variable which is going to be the agent. It is crucial to instantiate it before the game starts, because that one instance is going to be used during the whole game. Like this:

    ```ssh
    agente = AgenteAlejandroSAlejandroC()
    
    Begin of the game
    ... Loop ...
    End of the game
    ```

4. To use the created instance in order to get the action to take from the intelligent agent during the game, invoke the ``get_action_to_take(state, current_player)`` method passing the state of the game and the current player to it as parameters. Like this:

    ```ssh
    accionEj = agente.get_action_to_take(estado, jugadorActual)
    ```

5. Execute your Jupyter Notebook file and see the game progression. It's like **magic**!

[Python]: <https://www.python.org/downloads/>
[Virtual Connections]: <http://www.cs.middlebury.edu/~esarich/HexPaper.pdf>
[YouTube Video]: <https://youtu.be/ckJcKDS26VU>

