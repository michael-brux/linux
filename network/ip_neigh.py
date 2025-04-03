import subprocess
import json
COMMAND = ['ip', '-json', '-pretty', 'neigh', 'show']

def get_ip_neighbours():
    try:
        # Run the `ip` command to get IP neighbors in JSON format
        result = subprocess.run( COMMAND, capture_output=True, text=True, check=True)
        return result.stdout

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the ip command: {e}")

if __name__ == "__main__":
    print(get_ip_neighbours())