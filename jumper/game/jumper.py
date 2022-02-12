class Jumper:       # Done  -  Does not need any more edits in this file

    """A service that handles terminal operations. 
    Similar to the 'teminal service' file from 'seeker' assignment
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """

    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_number(self, prompt):
        """Gets numerical input from the terminal. Directs the user with the given prompt.

        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.

        Returns:
            float: The user's input as a number.
        """
        return float(input(prompt))
        
    def write_text(self, text):
        """Displays the given text on the terminal. 

        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)
class Jumper:       # Done  -  Does not need any more edits in this file

    """A service that handles terminal operations. 
    Similar to the 'teminal service' file from 'seeker' assignment
    
    The responsibility of a TerminalService is to provide input and output operations for the 
    terminal.
    """

    def read_text(self, prompt):
        """Gets text input from the terminal. Directs the user with the given prompt.
        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.
        Returns:
            string: The user's input as text.
        """
        return input(prompt)

    def read_number(self, prompt):
        """Gets numerical input from the terminal. Directs the user with the given prompt.
        Args: 
            self (TerminalService): An instance of TerminalService.
            prompt (string): The prompt to display on the terminal.
        Returns:
            float: The user's input as a number.
        """
        return float(input(prompt))
        
    def write_text(self, text):
        """Displays the given text on the terminal. 
        Args: 
            self (TerminalService): An instance of TerminalService.
            text (string): The text to display.
        """
        print(text)