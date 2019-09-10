from argparse import ArgumentParser as Parser

args = Parser(
    description = "A translater of codes, maked especialy for you porte the codes from some language to some language",
    prog = "Translater"
)


args.add_argument('-j', '--joao', action='append_const',
                    dest='const_collection',
                    const=True,
                    default=[],
                    help='Add different values to list')

j = args.parse_args()

print( j.const_collection )
