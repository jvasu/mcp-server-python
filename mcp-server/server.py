from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

# Create MCP server instance with a custom name
mcp = FastMCP("Demo Server")

# Add a calculator tool: a simple function to add two numbers
@mcp.tool()
def add(a: int, b:int) -> int:
    '''
    Docstring for add
    
    :param a: Description
    :type a: int
    :param b: Description
    :type b: int
    :return: Description
    :rtype: int
    '''
    return a+b

#Expose a greeting resource that dynamically construct a personalized gretting
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    '''
    Docstring for get_greeting
    
    :param name: Description
    :type name: str
    :return: Description
    :rtype: str
    '''
    return f"Hello, {name}"

# Adding prompts
@mcp.prompt()
def review_code(code: str) -> str:
    '''
    provide template for reviewing code
    
    :param code: code to review
    :return: A promt that asks the LLM to review the code
    
    '''
    return f"Please review this code:\n\n{code}"


if __name__ == "__main__":
    # Run the server over stdio so it can be used as a subprocess by the client
    mcp.run("stdio")