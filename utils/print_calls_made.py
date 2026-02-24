from utils.print_header import print_header


def print_calls_made(calls_made: list[dict]) -> None:
    print_header("CALL LOG")
    print("Calls made:")
    for index, call in enumerate(calls_made, start=1):
        print(f"{index}. {call}")
