import os

def create_directory(path):
    """Creates a directory if it doesn't exist."""
    try:
        os.makedirs(path, exist_ok=True)  # exist_ok=True prevents error if directory exists
    except OSError as e:
        print(f"Error creating directory {path}: {e}")

# Project Root Directory
project_root = "project_root"
create_directory(project_root)

# Directories to create (using a more compact nested loop)
base_dirs = ["massivemind"]
sub_dirs = {
    "massivemind": ["backend", "frontend"],
    "backend": ["models", "routes", "controllers", "middleware", "config", "tests"],
    "tests": ["unit", "integration"],
    "frontend": ["src", "tests"],
    "src": ["components", "styles", "utils", "assets"],
    "components": ["Header", "Footer", "TaskList"]
}

for base in base_dirs:
    create_directory(os.path.join(project_root, base))
    for sub in sub_dirs.get(base, []):
        create_directory(os.path.join(project_root, base, sub))
        for subsub in sub_dirs.get(sub, []):
            create_directory(os.path.join(project_root, base, sub, subsub))

print("Project structure created.")
