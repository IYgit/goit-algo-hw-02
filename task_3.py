def are_parentheses_balanced(s):
    stack = []
    opening = "({["
    closing = ")}]"
    pairs = {"(": ")", "{": "}", "[": "]"}
    
    for char in s:
        if char in opening:
            stack.append(char)
        elif char in closing:
            if not stack:
                return "Несиметрично"
            last_opening = stack.pop()
            if pairs[last_opening] != char:
                return "Несиметрично"
    
    if stack:
        return "Несиметрично"
    else:
        return "Симетрично"

# Приклади використання програми
print(are_parentheses_balanced("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Симетрично
print(are_parentheses_balanced("( 23 ( 2 - 3);"))           # Несиметрично
print(are_parentheses_balanced("( 11 }"))                   # Несиметрично
