import subprocess

def execute_command(command, shell=True):
    """Execute a shell command and print the output."""
    result = subprocess.run(command, shell=shell, text=True, capture_output=True)
    if result.returncode != 0:
        raise Exception(f"Command failed: {command}")