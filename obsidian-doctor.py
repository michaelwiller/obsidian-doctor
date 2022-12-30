#!/usr/bin/env python3
import argparse
import argcomplete


def obsidian_doctor(args):
    if args.listTag:
        print("Searching for tag\t\t{}".format(args.listTag))
    print("Invert list\t\t\t{}".format("yes" if args.invert else "no"))
    print("Include linked resources\t{}".format("no" if args.nolink else "yes"))




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process Obsidian markdown')
    parser.add_argument('-t', '--listTag',
                        nargs='?',
                        help='Find all files that have the provided tag')
    parser.add_argument('-i', '--invert',
                        action='store_true',
                        help='Invert search criteria')
    parser.add_argument('-l', '--nolink',
                        action='store_true',
                        help='Exclude linked resources like images etc. (default: include)')
    args = parser.parse_args()
    argcomplete.autocomplete(parser)
    obsidian_doctor(args)
