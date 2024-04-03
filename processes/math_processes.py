def check_integer(number):
    """_summary_: The function receives a string, tries to convert it to an integer, if it cannot, it            returns false

    Args:
        number (String): string that you want to convert to integer

    Returns:
        Integer: If you can convert
        False:   If you cannot convert
    """    
    try:
        number=int(number)
        return number
    except ValueError:
          
          return False