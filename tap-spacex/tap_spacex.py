import pandas as pd
import numpy as np
import singer

LOGGER = singer.get_logger()

schema = {
    'properties': {
        'id': {'type': 'string'},
        'name': {'type': 'string'},
        'date_utc': {'type': 'string', 'format': 'date-time'}
    }
}

def main():
    url = 'https://api.spacexdata.com/v4/launches'
    df = pd.read_json(url)

    # Replace NaN values with None for JSON compatibility
    df = df.replace({np.nan: None})

    # Convert to list of dicts
    records = df.to_dict(orient='records')

    # Emit schema
    singer.write_schema('launches', schema, 'id')

    # Emit records
    for record in records:
        singer.write_record('launches', record)

if __name__ == '__main__':
    main()
