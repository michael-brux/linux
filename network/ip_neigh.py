import subprocess
import json
from prettytable import PrettyTable
import argparse

COMMAND = ['ip', '-json', '-pretty', 'neigh', 'show']

def get_ip_neighbours():
    try:
        # Run the `ip` command to get IP neighbors in JSON format
        result = subprocess.run( COMMAND, capture_output=True, text=True, check=True)
        return result.stdout

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the ip command: {e}")

def output_table(neighbours):
    table = PrettyTable()
    table.field_names = ["IP", "Device", "MAC Address"]

    # Group by state
    grouped = {}
    for neighbour in neighbours:
        state = ' '.join(neighbour.get('state', ['UNKNOWN']))
        if state not in grouped:
            grouped[state] = []
        grouped[state].append(neighbour)

    for state, items in grouped.items():
        table.add_row([f"State: {state}", "", ""])
        for item in items:
            table.add_row([item['dst'], item['dev'], item['lladdr']])

    print(table)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get IP neighbors and output in JSON or table format.")
    parser.add_argument('--format', choices=['json', 'table'], default='table', help="Output format: json or table")
    args = parser.parse_args()

    neighbours = get_ip_neighbours()

    if args.format == 'json':
        print(neighbours)
    else:
        output_table(json.loads(neighbours))


    #output_table(json.loads(get_ip_neighbours()))
