# BIODS253 Assignment 1
# Original Author: Eashan M.
# Modified by: Gustavo A. Araújo R.

from math import comb
import argparse
import matplotlib.pyplot as plt
import timeit

def pascal_triangle(n):
    for i in range(n):
        for j in range(n-i+1):
            print(end=" ")
        for j in range(i+1):
            print(comb(i,j), end=" ")
        print("\n")

if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser(description="Print `n_rows` lines from Pascal's triangle and optionally time how long it takes to generate it.")
    parser.add_argument('n_rows', metavar='n_rows', type=int, nargs="?", default=15,
                    help="number of lines to print from Pascal's triangle")
    parser.add_argument('--plot_timings', metavar='n', type=int, nargs="?", default=0,
                    help="generate plot with the time taken to print Pascal's triangle up to `n` lines")
    args = parser.parse_args()
    parser.print_help()    
    
    # Print lines
    print(f"\nOutput: These are the first {args.n_rows} lines of Pascal's triangle ")
    pascal_triangle(args.n_rows)

    # Create plot with timings
    if args.plot_timings > 0:
        N_REPEAT = 30 # number of samples for Pascal's triangle
        all_timings = []
        n = args.plot_timings
        fig, ax = plt.subplots(layout="constrained")
        
        # Time results for `x` lines of Pascal's triangle, with 1 <= x <= n
        x_step = max((n + 19) // 20, 1)
        x_values = range(0, n + 1, x_step)
        for x in x_values:
            timings_x = []
            for j in range(N_REPEAT):
                res = timeit.timeit(f"pascal_triangle({x})", setup="from __main__ import pascal_triangle", number=1)
                timings_x.append(res)
            all_timings.append(timings_x)
        
        # Plot results
        viol = ax.violinplot(all_timings, showmeans=False, showmedians=True, showextrema=True)
        
        viol["cmedians"].set_label("medians")
        viol["cmedians"].set_color("black")
        viol["cmedians"].set_linewidth(2)
        
        viol["cmins"].set_label("extrema")
        for property in ["cmins", "cmaxes", "cbars"]:
            viol[property].set_color("gray")
            viol[property].set_linewidth(1)

        viol["bodies"][0].set_label("timing distributions")
        for body in viol["bodies"]:
            body.set_color("gray")

        ax.set_xticks([x + 1 for x in range(len(all_timings))], labels=x_values)
        ax.set_xlabel("Number of lines")
        ax.set_ylabel("Time (s)")
        ax.legend()
        plt.show()
    
        fig.savefig("pascal_timings.pdf")
    
    else:
        print("\nTo generate plot with timings, run `python Assignment1.py --plot_timings [n]`, \
              \nwith [n] being the max number of lines to be used in the benchmark (e.g. n = 50).")
