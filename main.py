import sys
from cli.interface import FreelancerAnalysisCLI

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <data_csv_path> [command]")
        return

    data_path = sys.argv[1]
    cli = FreelancerAnalysisCLI(data_path)

    # Remove the data_path from args so argparse works correctly
    sys.argv = [sys.argv[0]] + sys.argv[2:]
    cli.run_cli()


if __name__ == "__main__":
    main()