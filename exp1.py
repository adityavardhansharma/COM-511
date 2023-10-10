# Type checking of various data types
var_str = "Hello, World!"
var_int = 42
var_float = 3.14159
var_list = [1, 2, 3, 4, 5]
var_dict = {'name': 'John', 'age': 30}
var_bool = True
var_none = None

# Function to demonstrate type checking and built-in functions
def demonstrate_types_and_functions(value):
    print(f"Value: {value}")
    
    # Type checking using type()
    data_type = type(value)
    print(f"Type: {data_type}")
    
    # Using built-in functions
    if data_type == str:
        # Using len() for strings
        print(f"Length: {len(value)}")
        # Using isalnum() for strings
        print(f"Is Alphanumeric: {value.isalnum()}")
    elif data_type == int or data_type == float:
        # Using abs() for numbers
        print(f"Absolute Value: {abs(value)}")
        # Using round() for floats
        if data_type == float:
            print(f"Rounded Value: {round(value, 2)}")
    elif data_type == list:
        # Using len() for lists
        print(f"Number of Elements: {len(value)}")
        # Using min() for lists
        print(f"Minimum Value: {min(value)}")
    elif data_type == dict:
        # Using len() for dictionaries
        print(f"Number of Key-Value Pairs: {len(value)}")
    elif data_type == bool:
        print(f"Boolean Value: {value}")
    elif data_type == None:
        print("None Type")
    else:
        print("Unknown Type")

# Demonstrate the types and functions for each variable
demonstrate_types_and_functions(var_str)
print("\n")
demonstrate_types_and_functions(var_int)
print("\n")
demonstrate_types_and_functions(var_float)
print("\n")
demonstrate_types_and_functions(var_list)
print("\n")
demonstrate_types_and_functions(var_dict)
print("\n")
demonstrate_types_and_functions(var_bool)
print("\n")
demonstrate_types_and_function
