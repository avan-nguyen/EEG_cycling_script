def create_empty_dataset():
    dataset = {
        "active": {},
        "passive": {},
        "control": {}
    }
    return dataset

def add_subject(dataset, group, subject_id):
    dataset[group][subject_id] = {
        "baseline": {
            "filename": None,
            "raw": None,
            "processed": None,
            "features": {},
            "connectivity": {},
            "metadata": {}
        },
        "post1": {
            "filename": None,
            "raw": None,
            "processed": None,
            "features": {},
            "connectivity": {},
            "metadata": {}
        },
        "post2": {
            "filename": None,
            "raw": None,
            "processed": None,
            "features": {},
            "connectivity": {},
            "metadata": {}
        }
    }

def add_raw_data(dataset, group, subject_id, condition, filename, data, metadata):
    entry = dataset[group][subject_id][condition]

    entry["filename"] = filename
    entry["raw"] = data
    entry["metadata"] = metadata


def add_processed_data(dataset, group, subject_id, condition, processed_data):
    dataset[group][subject_id][condition]["processed"] = processed_data

def add_feature(dataset, group, subject_id, condition, feature_name, feature_data):
    dataset[group][subject_id][condition]["features"][feature_name] = feature_data
