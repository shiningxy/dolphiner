# Description: This file contains the functions that are used to model the data and predict the speed of the ship.
# Contains the following functions:
# - get_ship_base_info_by_mmsi: Get the base information of the ship by MMSI
# - get_ship_performance_by_mmsi: Get the sailing performance data of the ship by MMSI

import pandas as pd


def get_ship_base_info_by_mmsi(mmsi: int) -> pd.DataFrame:
    """Get the base information of the ship by MMSI from excel.

    Args:
        mmsi (int): The MMSI of the ship.

    Returns:
        pandas.DataFrame: The base information of the ship.

    Return columns:
        - mmsi: The MMSI of the ship.
        - imo: The IMO of the ship.
        - callsign: The callsign of the ship.
        - name_en: The English name of the ship.
        - name_cn: The Chinese name of the ship.
        - flag_ctry: The flag country of the ship.
        - registry_port: The registry port of the ship.
        - build_year: The build year of the ship.
        - deadweight: The deadweight of the ship.
        - grt: The Gross Register Tonnage of the ship.
        - net: The Net Tonnage of the ship.
        - length: The length of the ship.
        - width: The width of the ship.
        - height: The height of the ship.
        - draught: The draught of the ship.
        - max_speed: The max speed of the ship.
        - manage_body: The management body of the ship.
        - owner_body: The owner body of the ship.
    """
    # Read the data from the file
    data = pd.read_excel("data/ship_base_info.xlsx")
    # Filter the data by MMSI
    data = data[data["mmsi"] == mmsi]
    return data


def get_ship_performance_by_mmsi(mmsi: int) -> pd.DataFrame:
    """Get ship performance data by MMSI.

    This function reads ship performance data from an Excel file and filters it based on the provided MMSI.

    Args:
        mmsi (int): The MMSI (Maritime Mobile Service Identity) of the ship.

    Returns:
        pd.DataFrame: A DataFrame containing ship performance data for the specified MMSI.

    Columns in the returned DataFrame:
        - 'mmsi': The MMSI of the ship.
        - 'name_cn': The Chinese name of the ship.
        - 'name_en': The English name of the ship.
        - 'engine_speed': The engine speed of the ship.
        - 'screw_pitch': The screw pitch of the ship.
        - 'theory_speed': The theoretical speed of the ship.
        - 'full_load_actual_speed': The actual speed of the ship at full load.
        - 'full_load_main_engine_oil': The main engine oil consumption of the ship at full load.
        - 'full_load_auxiliary_oil': The auxiliary engine oil consumption of the ship at full load.
        - 'ballast_actual_speed': The actual speed of the ship in ballast condition.
        - 'ballast_main_engine_oil': The main engine oil consumption of the ship in ballast condition.
        - 'ballast_auxiliary_oil': The auxiliary engine oil consumption of the ship in ballast condition.
        - 'main_engine_oil_type': The type of main engine oil used by the ship.
        - 'auxiliary_oil_type': The type of auxiliary engine oil used by the ship.
    """
    # Read the data from the file
    data = pd.read_excel("data/ship_performance_info.xlsx")
    # Filter the data by MMSI
    data = data[data["mmsi"] == mmsi]
    return data


if __name__ == "__main__":
    # Test the function
    mmsi = 563045200
    data = get_ship_performance_by_mmsi(mmsi)
    print(data)
