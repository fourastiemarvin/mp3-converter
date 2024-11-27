from helper import execute_command

def setup_wsl():
    """Set up WSL and install Ubuntu if not already installed."""
    print("Step 1: Checking if WSL is installed...")
    try:
        execute_command("wsl --list --online")  # Check available distributions
    except Exception:
        print("WSL not installed. Attempting to install...")
        execute_command("wsl --install")
        print("WSL installation triggered. Please restart and rerun this script.")
    print("WSL is already installed.")

def install_python():
    """Install Python in WSL."""
    print("Step 2: Installing Python in WSL...")
    try:
        # Update package list and install Python
        execute_command('wsl sudo apt update')
        execute_command('wsl sudo apt install -y python3 python3-pip')
        print("Python installed successfully in WSL.")
    except Exception as e:
        print(f"Failed to install Python in WSL: {e}")
        raise

def install_yt_dlp():
    """Install yt-dlp in WSL."""
    print("Step 2: Installing yt-dlp in WSL...")
    try:
        execute_command('wsl pip install yt-dlp')
        print("yt-dlp installed successfully in WSL.")
    except Exception as e:
        print(f"Failed to install yt-dlp in WSL: {e}")
        raise

def install_dependencies():
    """Run a Python script stored on Windows from WSL."""
    print("Step 3: Running Python script in WSL...")
    # Convert the Windows path to a WSL-compatible path
    try:
        execute_command('wsl pip install -r requirements.txt')
        print("Requirements installed successfully in WSL.")
    except Exception as e:
        print(f"Failed to install requirements: {e}")
        raise

if __name__ == "__main__":
    try:
        setup_wsl()
        install_python()
        install_dependencies()
    except Exception as e:
        print(f"An error occurred: {e}")
