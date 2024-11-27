import os
from helper import execute_command

def run(script_path):
    """Run a Python script stored on Windows from WSL."""
    print("Step 3: Running Python script in WSL...")
    # Convert the Windows path to a WSL-compatible path
    script_path_wsl = script_path.replace("\\", "/").replace("C:", "/mnt/c")
    try:
        execute_command(f'wsl python3 {script_path_wsl}')
    except Exception as e:
        print(f"Failed to execute script: {e}")
        raise

if __name__ == "__main__":
    # Define the path to your Python script on Windows
    CURRENT_PATH = os.getcwd()
    script_path = f"{CURRENT_PATH}\display.py"
    try:
        run(script_path)
    except Exception as e:
        print(f"An error occurred: {e}")
