# Loading the libraries
import sympy as sp

#-------------------limit function -------------------#
def limit_calculation(function_str, var_str, value, direction='+-'):
    # Defining the variables and the function from the strings
    var =sp.symbols(var_str)
    function_ = sp.sympify(function_str)
    
    ## Showing the original function
    print(f"Original function: {function_str}")

    ## Simplify the function if it is possible and show the result
    simplified_function = sp.simplify(function_)
    print(f"Simplified function: {simplified_function}")

    ## Calculating the limit of the function on the given point
    limit = sp.limit(simplified_function, var, value, direction)

    # Showing the sustitution process
    print(f"\nSubstitution process:")
    print(f"Replace {var_str} = {value} in the simplified function:")
    print(f"{simplified_function} -> {limit}")

    return limit, var_str, function_str, simplified_function, value

funcion = "sin(x)/x"
variable = "x"
valor_punto = 0

limit = limit_calculation(function_str=funcion, var_str=variable, value=valor_punto)
print(f"The limit is: {limit[0]}")