from pycsvschema.checker import Validator
from pycsvschema.exceptions import ValidationError

import pandas
import codecs


def test_validated_orthoindy():
    schema = {
        'fields': [
            {
                "name": "Room",
                "type": "string",
                "pattern": "OR.OR\d{2}",
                'nullable': False,
            },
            {
                'name': 'Date',
                'type': 'string',
                'format': 'datetime',
                'datetimePattern': '%m/%d/%Y'
            },
            {
                'name': 'Service',
                'type': 'string',
                'nullable': False,
            },            
            {
                'name': 'Surgeon/Provider',
                'type': 'string',
                'nullable': False,
            },
            {
                'name': 'Procedures',
                'type': 'string',
                'nullable': False,
            },
            {
                'name': 'Actual Start',
                'type': 'string',
                'format': 'datetime',
                'datetimePattern': '%H:%M'
            },
            {
                'name': 'Actual End',
                'type': 'string',               
                'format': 'datetime',
                'datetimePattern': '%H:%M'
            },
            {
                'name': 'Trays by Procedure',
                'type': 'string',     
                'nullable': False,          
            },
        ]
    }

    csvfile='/Users/craigmerchant/code/PyCSVSchema/tests/test_data/OrthoIndy July 24th_28th.csv'
    csv_dataframe = pandas.read_csv(csvfile)
    
    v = Validator(dataframe=csv_dataframe, csvfile=None, schema=schema, errors='coerce')
    try:
      v.validate()
      v.output
    except ValidationError as ex:
       print(ex)

    v = Validator(dataframe=None, csvfile=csvfile, schema=schema, errors='coerce')
    try:
      v.validate()
      v.output
    except ValidationError as ex:
       print(ex)
