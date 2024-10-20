def calculate_lift_rounds(n, capacity):
    """
    Function to calculate the number of rounds the lift needs to cover.
    
    Parameters:
    n (int): Total number of people.
    capacity (int): Maximum number of people the lift can carry in one round.
    
    Returns:
    int: The number of rounds required to transport all people to the top floor.
    """
    # Your code here
    carry_capacity=n//capacity
    if n%capacity!=0:
        return carry_capacity+1
    else:
        return carry_capacity

print(calculate_lift_rounds(10,3))