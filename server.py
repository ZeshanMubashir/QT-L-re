import os
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("Qt-Helper")

@mcp.tool()
def create_qt_widget(name: str):
    """Generates a basic Qt Widget class (header and source)."""
    header_content = f"""#pragma once
#include <QWidget>

class {name} : public QWidget {{
    Q_OBJECT
public:
    explicit {name}(QWidget *parent = nullptr);
}};
"""
    cpp_content = f"""#include "{name}.h"

{name}::{name}(QWidget *parent) : QWidget(parent) {{
    setWindowTitle("{name}");
}}
"""
    
    with open(f"{name}.h", "w") as f:
        f.write(header_content)
    with open(f"{name}.cpp", "w") as f:
        f.write(cpp_content)
        
    return f"Created {name}.h and {name}.cpp"

@mcp.tool()
def add_to_cmake(filename: str):
    """Adds a source file to the CMakeLists.txt executable."""
    with open("CMakeLists.txt", "r") as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        if "add_executable" in line and filename not in line:
            line = line.replace(")", f" {filename})")
        new_lines.append(line)
        
    with open("CMakeLists.txt", "w") as f:
        f.writelines(new_lines)
    
    return f"Added {filename} to CMakeLists.txt"

if __name__ == "__main__":
    mcp.run()
