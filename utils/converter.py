import h5py

from pathlib import Path


def extract_file(file):
    """Returns the data stored in a HDF5 file as a dictionary"""

    with h5py.File(Path(file), "r") as f:
        song_data = {
            "artist_mbid": f["metadata/songs"]["artist_mbid"][0].decode("utf-8"),
            "artist_mbtags": [
                tag.decode("utf-8") for tag in f["musicbrainz/artist_mbtags"]
            ],
            "artist_mbtags_count": list(f["musicbrainz/artist_mbtags_count"]),
            "artist_name": f["metadata/songs"]["artist_name"][0].decode("utf-8"),
            "artist_playmeid": int(f["metadata/songs"]["artist_playmeid"][0]),
            "artist_terms": [
                term.decode("utf-8") for term in f["metadata/artist_terms"]
            ],
            "artist_terms_freq": list(f["metadata/artist_terms_freq"]),
            "artist_terms_weight": list(f["metadata/artist_terms_weight"]),
            "audio_md5": f["analysis/songs"]["audio_md5"][0].decode("utf-8"),
            "danceability": float(f["analysis/songs"]["danceability"][0]),
            "duration": float(f["analysis/songs"]["duration"][0]),
            "end_of_fade_in": float(f["analysis/songs"]["end_of_fade_in"][0]),
            "energy": float(f["analysis/songs"]["energy"][0]),
            "key": int(f["analysis/songs"]["key"][0]),
            "key_confidence": float(f["analysis/songs"]["key_confidence"][0]),
            "loudness": float(f["analysis/songs"]["loudness"][0]),
            "mode": int(f["analysis/songs"]["mode"][0]),
            "mode_confidence": float(f["analysis/songs"]["mode_confidence"][0]),
            "release": f["metadata/songs"]["release"][0].decode("utf-8"),
            "release_7digitalid": int(f["metadata/songs"]["release_7digitalid"][0]),
            "song_hotttnesss": float(f["metadata/songs"]["song_hotttnesss"][0]),
            "song_id": f["metadata/songs"]["song_id"][0].decode("utf-8"),
            "start_of_fade_out": float(f["analysis/songs"]["start_of_fade_out"][0]),
            "tempo": float(f["analysis/songs"]["tempo"][0]),
            "time_signature": int(f["analysis/songs"]["time_signature"][0]),
            "time_signature_confidence": float(
                f["analysis/songs"]["time_signature_confidence"][0]
            ),
            "title": f["metadata/songs"]["title"][0].decode("utf-8"),
            "track_7digitalid": int(f["metadata/songs"]["track_7digitalid"][0]),
            "track_id": f["analysis/songs"]["track_id"][0].decode("utf-8"),
            "year": int(f["musicbrainz/songs"]["year"][0]),
        }

    return song_data
