import config
from args import get_args

app = config.connex_app


if __name__ == "__main__":
    args = get_args()
    app.run(debug=args.debug, port=args.port)
