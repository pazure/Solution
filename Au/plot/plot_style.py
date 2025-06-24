
import matplotlib.pyplot as plt
from cycler import cycler

def set_plot_style(
    general=True,
    font=True,
    lines=True,
    colors=True,
    grid=True,
    ticks=True,
    legend=True,
    save_quality=True,
    dpi=150

):
    params = {}

    if general:
        params.update({
            'figure.dpi': dpi,
            'figure.figsize': (8, 5)       # (6.4, 4.8)
        })

    if font:
        params.update({
            'font.size': 12,              # General font size
            'axes.labelsize': 14,         # Font size for axis labels
            'axes.titlesize': 16,         # Font size for plot titles
            'xtick.labelsize': 12,        # Font size for x-axis tick labels
            'ytick.labelsize': 12,        # Font size for y-axis tick labels
            'legend.fontsize': 10,        # Font size for legends
            # 'font.family': 'serif',       # Use a serif font (e.g., Times New Roman)
            # 'text.usetex': False          # LaTeX-style text rendering
        })

    if lines:
        params.update({
            'lines.linewidth': 1.5,        # Line width for plot lines
            'lines.markersize': 4,         # Marker size for points in plots
            'axes.linewidth': 0.8,          # Thickness of the plot box (spines)
            'lines.markeredgecolor': 'k',        # the default marker edge color
            'lines.markeredgewidth': 0.3,         # the line width around the marker symbol
        })

    if colors:
        # https://www.molecularecologist.com/2020/04/23/simple-tools-for-mastering-color-in-scientific-figures/
        params.update({
            'axes.prop_cycle': cycler('color', [
            "#FF1F5B",
			"#009ADE",
			"#F28522",
			"#AF58BA",
			"#FFC61E",
			"#00CD6C",
			"#A0B1BA",
			"#A6761D",
			"#E9002D",
			"#FFAA00",
			"#00B000",
			"#C40F5B",
			"#FD8D3C",
			"#089099"
            ])  # Colorblind-friendly palette
        })

        # # https://stats.stackexchange.com/a/407715/193048
        # params.update({
        #     'axes.prop_cycle': cycler('color', [
        #     "#E69F00", "#56B4E9", "#009E73", "#F0E442",
        #     "#0072B2", "#D55E00", "#CC79A7", "#000000"])  # Colorblind-friendly palette
        # })

    if grid:
        params.update({
            'axes.grid': True,             # Enable grid lines
            'grid.color': 'gray',          # Set grid line color
            'grid.linestyle': ':',        # Use dashed grid lines
            'grid.alpha': 0.5,
            'grid.linewidth': 0.5,
        })

    if ticks:
        s_maj = 6
        s_min = 3
        w_maj = 0.8
        w_min = 0.6
        params.update({
            'xtick.major.width': w_maj,      # Width of major ticks on x-axis
            'ytick.major.width': w_maj,      # Width of major ticks on y-axis
            'xtick.minor.width': w_min,      # Width of minor ticks on x-axis
            'ytick.minor.width': w_min,      # Width of minor ticks on y-axis
            'xtick.major.size': s_maj,         # Length of major ticks
            'ytick.major.size': s_maj,         # Length of major ticks
            'xtick.minor.size': s_min,         # Length of minor ticks
            'ytick.minor.size': s_min,         # Length of minor ticks
            'xtick.direction': 'in',
            'ytick.direction': 'in',
            'xtick.minor.visible': True,
            'ytick.minor.visible': True,
            'xtick.top': True,
            'ytick.right': True,

        })

    if legend:
        params.update({
            'legend.frameon': True,       # Add a box around the legend
            'legend.framealpha': 1,       # Make the legend box opaque
            'legend.loc': 'best',         # Place the legend at the best location automatically
            'legend.borderaxespad': 0.5,  # Padding between the legend and axes
        })

    if save_quality:
        params.update({
            'savefig.dpi': 300,           # Save figures at 300 DPI for publications
            'savefig.format': 'png',      # Default file format (can be 'pdf', 'svg', etc.)
            'savefig.bbox': 'tight',      # Reduce whitespace around the saved figure
            'svg.fonttype': 'path',
        })

    # Apply the collected parameters to rcParams
    plt.rcParams.update(params)
