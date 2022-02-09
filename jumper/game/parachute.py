

class Parachute:
    """Where we create and change the tiers of the parachute
    
    """
    def __init__(self):
        """Constructs the parachute"""

        self._parachutes = 0
        self._parachute = 0


    def show_parachute(self, tries):
        stages = [  # final state: No parachute left 
            """
             x 
            /|\ 
            / \ 
       ^^^^^^^^^^^^^
            """,
            # Small strings (1 attempt left)
            """
            \ /
             O
            /|\ 
            / \ 

       ^^^^^^^^^^^^^
            """,
            # Medium strings (2 attempts left)
            """
           \   /
            \ /
             O
            /|\ 
            / \ 

       ^^^^^^^^^^^^^
            """,
            # Long strings (3 attempts left)
            """
          \     /
           \   /
            \ /
             O
            /|\ 
            / \ 

       ^^^^^^^^^^^^^
            """,
            # middle of chute (4 attempts left)
            """
          /_____\ 
          \     /
           \   /
            \ /
             O
            /|\ 
            / \ 

       ^^^^^^^^^^^^^
            """,
            # Initial state (5 attempts)
            """
           _____
          /_____\ 
          \     /
           \   /
            \ /
             O
            /|\ 
            / \ 

       ^^^^^^^^^^^^^
            """,
            ]
        return print(stages[tries])
