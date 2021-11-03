"""Remove solution cells from Jupyter notebook"""

import argparse
import json
import pathlib


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        prog="finalize_exercise.py",
        description='Remove solution cells from Jupyter notebook',
        usage="%(prog)s -f input [-o output]",
        epilog="https://github.com/janjoswig/AlgoSB2021"
        )
    io_arguments = parser.add_argument_group('input/output arguments')
    io_arguments.add_argument(
        '-f', "--file",
        metavar="path",
        nargs='+',
        type=str,
        help=(
            "full input path and filename with extentsion (.ipynb); "
            "multiple arguments possible."
            ),
        required=True
        )
    io_arguments.add_argument(
        '-o', '--output',
        metavar="path",
        nargs='+',
        type=str,
        help=(
            "full output path and filename;  if a list of input files is "
            "provided, a list of output filenames with the same number of "
            "entries should be specified;  the default (None) names the "
            "output following the input."
            ),
        default=None
        )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help="be chatty",
        default=False
        )
    args = parser.parse_args()

    if (args.output is not None) and (len(args.output) != len(args.file)):
        raise ValueError("Number of input and output files does not match")

    for count, fname in enumerate(args.file):
        f = pathlib.Path(fname)

        if not f.is_file():
            if args.verboose:
                print(f"File {f} does not exist.")
            continue

        if args.output is None:
            output = fname.rsplit('.', 1)[0] + "_final.ipynb"
        else:
            output = args.output[count]

        with open(f) as fp:
            file_content = json.load(fp)

        kept_cells = []

        for cell in file_content["cells"]:

            metadata = cell.get("metadata", {})

            is_solution = False
            for string in ["solution", "solution2"]:
                if string in metadata:
                    is_solution = True
                    del metadata[string]

            is_first = False
            for string in ["solution_first", "solution2_first"]:
                if string in metadata:
                    is_first = metadata[string]
                    del metadata[string]

            cell["metadata"] = metadata

            if is_solution and not is_first:
                if args.verbose:
                    print(f'Remove cell: {cell.get("id", "unknown")}')
                continue

            kept_cells.append(cell)

        file_content["cells"] = kept_cells

        if args.verbose:
            print(f'Saving {output}.npy')

        with open(output, "w") as op:
            json.dump(file_content, op, indent=2)
