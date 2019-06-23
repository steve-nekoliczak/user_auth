import argparse

from config import connex_app


def get_args():
    ap = argparse.ArgumentParser('Handle user data for DieFehlendeWoerter.')

    # Add args
    ap.add_argument('-d', '--debug',
                    action='store_true',
                    help="Enable debugging mode.")

    ap.add_argument('-p', '--port', type=int,
                    help="Port number to run this service on.",
                    default=5014)

    a = ap.parse_args()

    return a


if __name__ == "__main__":
    args = get_args()

    connex_app.run(debug=args.debug, port=args.port)

