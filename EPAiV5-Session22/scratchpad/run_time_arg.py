import argparse

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Process runtime arguments.")

    # Add arguments
    parser.add_argument("arg1", type=int, help="sv_amp_ch1")
    parser.add_argument("arg2", type=int, help="sv_amp_ch2")
    parser.add_argument("arg3", type=int, help="j_amp_ch1")
    parser.add_argument("arg4", type=int, help="j_amp_ch2")

    # Parse arguments
    args = parser.parse_args()

    # Display the arguments
    print(f"Argument 1: {args.arg1}")
    print(f"Argument 2: {args.arg2}")
    print(f"Argument 3: {args.arg3}")
    print(f"Argument 4: {args.arg4}")

if __name__ == "__main__":
    main()