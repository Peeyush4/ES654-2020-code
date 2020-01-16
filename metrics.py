
def accuracy(y_hat, y):
    """
    Function to calculate the accuracy

    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    Output:
    > Returns the accuracy as float
    """
    """
    The following assert checks if sizes of y_hat and y are equal.
    Students are required to add appropriate assert checks at places to
    ensure that the function does not fail in corner cases.
    """
    assert(y_hat.size == y.size)
    # TODO: Write here
    return sum([1 for i in range(y_hat.size) if y_hat.iloc[i] == y.iloc[i]]) / y.size
    # returns ||y = y_hat|| / ||y||

def precision(y_hat, y, cls):
    """
    Function to calculate the precision

    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    > cls: The class chosen
    Output:
    > Returns the precision as float
    """
    assert(y_hat.size == y.size)
    if sum([1 for i in range(y.size) if y_hat[i] == cls]) != 0: return sum([1 for i in range(y.size) if y_hat[i] == y[i] and y[i] == cls]) / sum([1 for i in range(y.size) if y_hat[i] == cls])
    else: return 0
    # returns ||y = y_hat = cls|| / ||y_hat = cls||

def recall(y_hat, y, cls):
    """
    Function to calculate the recall

    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    > cls: The class chosen
    Output:
    > Returns the recall as float
    """
    assert(y_hat.size == y.size)
    return sum([1 for i in range(y.size) if y_hat[i] == y[i] and y[i] == cls]) / sum([1 for i in range(y.size) if y[i] == cls])
    # returns ||y = y_hat = cls|| / ||y = cls||
    

def rmse(y_hat, y):
    """
    Function to calculate the root-mean-squared-error(rmse)

    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    Output:
    > Returns the rmse as float
    """
    assert(y_hat.size == y.size)
    return (sum([(y_hat.iloc[i] - y.iloc[i])**2 for i in range(y.size)]) / y.size)**(0.5)
    # returns (sum((y_hat[i] - y[i])**2) / N)**(1/2)

def mae(y_hat, y):
    """
    Function to calculate the mean-absolute-error(mae)

    Inputs:
    > y_hat: pd.Series of predictions
    > y: pd.Series of ground truth
    Output:
    > Returns the mae as float
    """
    assert(y_hat.size == y.size)
    return sum([abs(y_hat.iloc[i] - y.iloc[i]) for i in range(y.size)]) / y.size
    # returns sum(|y_hat[i] - y[i]|) / N
