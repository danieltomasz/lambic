from operator import itemgetter

from fooof.sim.gen import gen_freqs, gen_group_power_spectra



def generate_example_spectra(sparams: dict = None):
    """Generate example power spectra for testing and demo purposes.
    """
    if sparams is None:
        sparams = {
            "n_spectra": 2,
            "freq_range": [1.5, 50],
            "aperiodic_params": [[0.5, 1], [1, 1.5]],
            "periodic_params": [[10, 0.4, 1], [10, 0.2, 1, 22, 0.1, 3]],
            "nlvs": 0.02,
            "return_params":True,
        }
    freqs, powers, sim_params = gen_group_power_spectra(**sparams)
    # type: ignore
    return freqs, powers, sim_params

def filter_xarray(psd_concat, coordinate : str, contains):
    def filter_substring(string, substr):
        return [str for str in string if
                any(sub in str for sub in substr)]
    # Driver code
    roi_values = psd_concat.coords[coordinate].values.tolist()
    print(filter_substring(roi_values, contains))
    filtered_roi = filter_substring(roi_values, contains)
    roi_names_set = psd_concat.sel(roi_names=filtered_roi)
    return roi_names_set

