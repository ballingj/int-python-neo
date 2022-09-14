"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
from models import NearEarthObject, CloseApproach
from helpers import cd_to_datetime, datetime_to_str


def write_to_csv(results, filename):
    # the next five lines were used for debug lines as part of development
    # print(results)
    # # ex output: (CloseApproach(time='2020-01-01 00:54', distance=0.02, velocity=5.62, 
    #             neo=NearEarthObject(designation='2020 AY1', name=None, diameter=nan, hazardous=False)),
    #    
    # for elem in results:
    #    print(f'{datetime_to_str(elem.time)},{elem.distance},{elem.velocity}, ' \
    #          f'{elem.neo.designation},{elem.neo.name if True else ""}, ' \
    #          f'{elem.neo.diameter if not "nan" else ""},{elem.neo.hazardous}')

    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous'
    )
    # Write the results to a CSV file, following the specification in the instructions.
    # ref: https://realpython.com/python-csv/

    with open(filename, 'w') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for elem in results:
            writer.writerow(
                {'datetime_utc': datetime_to_str(elem.time), 
                'distance_au': elem.distance, 'velocity_km_s': elem.velocity, 
                'designation': elem.neo.designation, 
                'name': elem.neo.name if not None else "", 
                'diameter_km': elem.neo.diameter if not "nan" else "", 
                'potentially_hazardous': elem.neo.hazardous})


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # Write the results to a JSON file, following the specification in the instructions.
    # ref: https://learn.udacity.com/nanodegrees/nd303/parts/cd0010/lessons/ \
    # 139fb4d5-8def-4d89-9fff-018eda53dfdf/concepts/987b0316-c804-4eea-85ee-800100802c29

    results_list = []
    for elem in results:
        results_list.append(
            {'datetime_utc': datetime_to_str(elem.time), 
            'distance_au': elem.distance, 
            'velocity_km_s': elem.velocity, 
            'neo': {'designation': elem.neo.designation,
            'name': elem.neo.name if not None else "", 
            'diameter_km': elem.neo.diameter if not "nan" else float("NaN"), 
            'potentially_hazardous': elem.neo.hazardous}})

    with open(filename, 'w') as outfile:
        json.dump(results_list, outfile, indent=2)
