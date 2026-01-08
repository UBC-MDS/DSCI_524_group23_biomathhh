def calculate_pH(hydronium_concentration): 
	"""
    Calculate pH scale for a given hydronium concentration.
    
    This function computes pH value using the formula:
    pH = -log(hydronium concentration)
    
    Parameters:
    -----------
        hydronium_concentration (float): the concentration of hydronium.
	        Must be a positive number.
    
    Returns:
    --------
        float: The calculated pH value.
    
    
    Examples:
        >>> calculate_pH(1e-7)
        7.0
        
        >>> exponential_growth(6.31e-8)
        7.2

    """