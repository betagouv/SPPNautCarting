# Copyright (c), 2016-2020, SISSA (International School for Advanced Studies).
# All rights reserved.
# This file is distributed under the terms of the MIT License.
# See the file 'LICENSE' in the root directory of the present
# distribution, or http://opensource.org/licenses/MIT.
#
# @author Davide Brunato <brunato@sissa.it>
#
# type: ignore
"""Command Line Interface"""
import argparse
import os
import sys
from urllib.error import URLError

import xmlschema
from xmlschema import XMLSchema11, iter_errors

PROGRAM_NAME = os.path.basename(sys.argv[0])

CONVERTERS_MAP = {
    "unordered": xmlschema.UnorderedConverter,
    "parker": xmlschema.ParkerConverter,
    "badgerfish": xmlschema.BadgerFishConverter,
    "abdera": xmlschema.AbderaConverter,
    "jsonml": xmlschema.JsonMLConverter,
    "columnar": xmlschema.ColumnarConverter,
}


def xsd_version_number(value):
    if value not in ("1.0", "1.1"):
        raise argparse.ArgumentTypeError("%r is not a valid XSD version" % value)
    return value


def defuse_data(value):
    if value not in ("always", "remote", "never"):
        raise argparse.ArgumentTypeError("%r is not a valid value" % value)
    return value


def main():
    parser = argparse.ArgumentParser(
        prog=PROGRAM_NAME, add_help=True, description="validate a set of XML files."
    )
    parser.usage = (
        "%(prog)s [OPTION]... [FILE]...\n" "Try '%(prog)s --help' for more information."
    )
    parser.add_argument(
        "-v",
        dest="verbosity",
        action="count",
        default=0,
        help="increase output verbosity.",
    )
    parser.add_argument(
        "files", metavar="[XML_FILE ...]", nargs="+", help="XML files to be validated."
    )

    args = parser.parse_args()

    schema_class = XMLSchema11

    tot_errors = 0
    schema = [
        open(
            "./sources/S-123/S-123 App_D-1 GMLFormat 1.0.0/S123/1.0/20170831/S123.xsd"
        ),
        open(
            "./sources/S-123/S-123 App_D-1 GMLFormat 1.0.0/S100_3_0_0/S100GML/20170505/S100_gmlProfile.xsd"
        ),
        open(
            "./sources/S-123/S-123 App_D-1 GMLFormat 1.0.0/S100_3_0_0/S100GML/20170505/S100_gmlProfileExt.xsd"
        ),
        open(
            "./sources/S-123/S-123 App_D-1 GMLFormat 1.0.0/S100_3_0_0/S100GML/20170505/S100_gmlProfileLevels.xsd"
        ),
        open(
            "./sources/S-123/S-123 App_D-1 GMLFormat 1.0.0/S100_3_0_0/S100GML/20170505/s100gmlbase.xsd"
        ),
        open(
            "./sources/S-123/S-123 App_D-1 GMLFormat 1.0.0/S100_3_0_0/S100GML/20170505/s100gmlbaseExt.xsd"
        ),
        open("./sources/S-127-1.0.0 SampleData/schemas/S127/1.0.0/20181129/S127.xsd"),
    ]

    for filepath in args.files:
        try:
            errors = list(
                iter_errors(
                    filepath,
                    schema=schema,
                    cls=schema_class,
                )
            )
        except (xmlschema.XMLSchemaException, URLError) as err:
            tot_errors += 1
            print(str(err))
            continue
        else:
            if not errors:
                print("\n {} is valid".format(filepath))
            else:
                tot_errors += len(errors)
                print("\n {} is not valid \n".format(filepath))
                print(errors)

    sys.exit(tot_errors)


if __name__ == "__main__":
    sys.exit(main())
