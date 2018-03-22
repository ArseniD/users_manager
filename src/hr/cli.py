from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser(description="""
    managing users on a server based on an 'inventory' JSON file.""")
    parser.add_argument('path', help="the path to the inventory file")
    parser.add_argument('--export', action='store_true', help='export current settings to inventory file')
    return parser


def main():
    from hr import inventory, users

    args = create_parser().parse_args()

    if args.export:
        inventory.dump(args.path)
    else:
        load_data = inventory.load(args.path)
        users.sync(load_data)
