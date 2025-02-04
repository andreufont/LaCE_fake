import argparse
# our modules below
from lace_fake import extract_skewers

""" Extract skewers for a given snapshot, using different temperatures. """

# get options from command line
parser = argparse.ArgumentParser()
parser.add_argument('--raw_dir', type=str,
                help='Base directory with raw simulation outputs (crashes if it does not exist)',required=True)
parser.add_argument('--post_dir', type=str,
                help='Base directory with simulation post-processings',required=True)
parser.add_argument('--snap_num', type=int, help='Snapshop number',required=True)
parser.add_argument('--axis', type=int, help='Axis to extract skewers (1,2,3)',required=False)
parser.add_argument('--n_skewers', type=int, default=10, help='Number of skewers per side',required=False)
parser.add_argument('--width_Mpc', type=float, default=0.1, help='Cell width (in Mpc)',required=False)
parser.add_argument('--scales_T0', type=str, default='1.0', help='Comma-separated list of T0 scalings to use.',required=False)
parser.add_argument('--scales_gamma', type=str, default='1.0', help='Comma-separated list of gamma scalings to use.',required=False)
parser.add_argument('--verbose', action='store_true', help='Print runtime information',required=False)
args = parser.parse_args()

scales_T0=[float(scale) for scale in args.scales_T0.split(',')]
scales_gamma=[float(scale) for scale in args.scales_gamma.split(',')]

info=extract_skewers.rescale_write_skewers_z(raw_dir=args.raw_dir,
            post_dir=args.post_dir,
            num=args.snap_num,n_skewers=args.n_skewers,
            width_Mpc=args.width_Mpc,
            axis=args.axis,
            scales_T0=scales_T0,scales_gamma=scales_gamma)

print('DONE')
