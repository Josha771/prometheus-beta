import sys
import time

class ProgressBar:
    """
    A dynamic progress bar logger that can be used to track progress of operations.
    
    Attributes:
        total (int/float): Total number of items/steps to process
        prefix (str): Prefix text before the progress bar
        suffix (str): Suffix text after the progress bar
        decimals (int): Number of decimal places for percentage
        length (int): Character length of the progress bar
        fill (str): Bar fill character
        print_end (str): End character (e.g. "\r" for overwriting)
    """
    def __init__(self, total, prefix='Progress:', suffix='Complete', 
                 decimals=1, length=50, fill='█', print_end="\r"):
        """
        Initialize the progress bar.
        
        Args:
            total (int/float): Total number of iterations expected
        """
        self.total = total
        self.prefix = prefix
        self.suffix = suffix
        self.decimals = decimals
        self.length = length
        self.fill = fill
        self.print_end = print_end
        self.current = 0

    def update(self, current=None):
        """
        Update the progress bar.
        
        Args:
            current (int/float, optional): Current iteration. 
                                           If None, increment by 1.
        """
        if current is not None:
            self.current = current
        else:
            self.current += 1

        # Prevent overflow
        self.current = min(self.current, self.total)

        # Calculate percentages
        percent = ("{0:." + str(self.decimals) + "f}").format(
            100 * (self.current / float(self.total)))
        
        # Calculate filled length
        filled_length = int(self.length * self.current // self.total)
        
        # Create bar string
        bar = self.fill * filled_length + '-' * (self.length - filled_length)
        
        # Print bar
        print(f'\r{self.prefix} |{bar}| {percent}% {self.suffix}', 
              end=self.print_end, flush=True)
        
        # Print new line on completion
        if self.current >= self.total:
            print()

    def __iter__(self):
        """
        Allow using the progress bar in a for loop.
        
        Yields:
            int: Current iteration
        """
        self.current = 0
        for i in range(int(self.total)):
            yield i
            self.update()

def log_with_progress(iterable, prefix='Progress:', **kwargs):
    """
    Wrap an iterable with a progress bar.
    
    Args:
        iterable (iterable): Iterable to track progress for
        prefix (str, optional): Prefix for progress bar
        **kwargs: Additional arguments for ProgressBar
    
    Returns:
        ProgressBar: A progress bar wrapping the iterable
    """
    return ProgressBar(len(iterable), prefix=prefix, **kwargs)