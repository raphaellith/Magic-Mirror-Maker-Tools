from matplotlib.colors import LinearSegmentedColormap

def get_greyscale_colormap():
    # Create a custom colormap that goes from black to white
    colors = [(0, 0, 0), (1, 1, 1)]  # Black to white
    cmap_name = 'bw_cmap'
    bw_cmap = LinearSegmentedColormap.from_list(cmap_name, colors, N=256)

    return bw_cmap