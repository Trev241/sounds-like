import re
import h5py


def h5_to_dict(file):
    """Returns the data stored in a HDF5 file as a dictionary"""
    data = {}

    def populate(name, obj):
        if isinstance(obj, h5py.Group):
            # Ignore groups
            return

        if obj.attrs["CLASS"] == b"TABLE":
            # Object is a table
            values = obj[:]
            for k, v in obj.attrs.items():
                # We can use the index in the field name to access the correct value in the array
                match = re.match(r"FIELD_(\d+)_NAME", k)
                if match:
                    idx = int(match.group(1))
                    val = values[0][idx]
                    try:
                        # Attempt to convert to string
                        val = val.decode("utf-8")
                    except:
                        pass
                    data[f"{name}/{v.decode("utf-8")}"] = val
        else:
            # Object is a basic array
            data[name] = obj[:]

    with h5py.File(file, "r") as f:
        f.visititems(populate)

    return data
