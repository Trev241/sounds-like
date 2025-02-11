import h5py
import pandas as pd

from pathlib import Path


def h5_to_pandas(path: str) -> pd.DataFrame:
    """
    Recursively converts all HDF5 files into a pandas dataframe.

    :param path: Path containing HDF5 files to be converted.
    :returns dataframe: A pandas dataframe where each row represents one HDF5 file.
    """

    col_names = []
    col_names_filled = False
    rows = []

    # Extract data
    for curr_path, _, files in Path(path).walk():
        for file in files[:1]:
            with h5py.File(curr_path.joinpath(file)) as f:
                values = []

                def populate(name, obj: h5py.Dataset):
                    if not isinstance(obj, h5py.Group):
                        if not col_names_filled:
                            col_names.append(name)
                        values.append(f[name][:])

                f.visititems(populate)
                rows.append(values)
                col_names_filled = True

    return pd.DataFrame(rows, columns=col_names)
