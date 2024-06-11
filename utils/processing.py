# Description: Preprocess the data
# Contains the following functions:
# - read_excel_init_route: Read the data from the file
# - clean_route: Clean the data. drop nan data
# - convert_to_json: Convert the data to JSON format
# - simplify_route: Simplify the data. use rdp algorithm to simplify the data
# - show_route: Show the route data (simplify and original) on the map. use plotly to show the route data

import pandas as pd
import json
from rdp import rdp
from loguru import logger
import plotly.express as px
from plotly.subplots import make_subplots


def read_excel_init_route(file_path: str):
    """Read the data from the excel. The data is the initial route data.

    two columns are required: "lon" and "lat"

    Args:
        file_path (str): The path to the file.

    Returns:
        pandas.DataFrame: The data read from the file.
    """
    data = pd.read_excel(file_path)
    return data


def clean_route(data: pd.DataFrame):
    """Clean the route data. drop nan data.

    Args:
        data (pandas.DataFrame): The data to be cleaned.

    Returns:
        pandas.DataFrame: The cleaned data.
    """
    data = data.dropna(axis=1, how="all")
    return data


def convert_to_json(data: pd.DataFrame):
    """Convert the data to JSON format.

    Args:
        data (pandas.DataFrame): The data to be converted.

    Returns:
        str: The data in JSON format.
    """
    data_json = data.to_json(orient="records")
    return data_json


def simplify_route(data: pd.DataFrame, epsilon: float = 0.06) -> pd.DataFrame:
    """
    Simplify the route data using the Ramer-Douglas-Peucker (RDP) algorithm.

    This function reduces the number of points (drop the inessential points) in the route
    while maintaining the overall shape of the path.

    Args:
        data (pandas.DataFrame): The data to be simplified, with 'lat' and 'lon' columns.
        epsilon (float): The maximum distance between a point and the simplified path.

    Returns:
        pandas.DataFrame: The simplified data with 'lat' and 'lon' columns.
    """
    # Ensure the data has the required columns
    if not {"lat", "lon"}.issubset(data.columns):
        raise ValueError("Data must have 'lat' and 'lon' columns.")

    # Convert the DataFrame to a NumPy array for the RDP algorithm
    track = data[["lat", "lon"]].values

    # Apply the RDP algorithm to simplify the track
    simplified_track = rdp(track, epsilon=epsilon)

    # Convert the simplified track back to a DataFrame
    simplified_data = pd.DataFrame(simplified_track, columns=["lat", "lon"])

    return simplified_data


def show_route(original_data: pd.DataFrame, simplified_data: pd.DataFrame, accesstoken: str):
    """
    Show the original and simplified route data on the map using Plotly.

    Args:
        original_data (pandas.DataFrame): The original route data with 'lat' and 'lon' columns.
        simplified_data (pandas.DataFrame): The simplified route data with 'lat' and 'lon' columns.
        accesstoken (str): The Plotly access token. You can obtain a access token from the Plotly website.

    Returns:
        None. Displays the map with the routes.
    """
    # Create a DataFrame with a single empty point
    df = pd.DataFrame({"lat": [None], "lon": [None]})  # 空坐标点

    # Create the figure
    fig = px.scatter_mapbox(df, lat="lat", lon="lon", zoom=2)

    # update layout
    fig.update_layout(
        title={"font_color": "#FF0000", "font_size": 25, "x": 0.01, "y": 0.95},
        mapbox={"accesstoken": accesstoken, "center": {"lon": 60, "lat": 0}, "style": "satellite-streets", "zoom": 1},
        margin={"l": 0, "r": 0, "t": 0, "b": 0},
    )

    # Add original route
    fig.add_scattermapbox(lat=original_data["lat"], lon=original_data["lon"], mode="lines+markers", marker_color="#FF0000", marker_opacity=0.7, name="Original Route")

    # Add simplified route
    fig.add_scattermapbox(lat=simplified_data["lat"], lon=simplified_data["lon"], mode="lines+markers", marker_color="#00FF00", marker_opacity=0.7, name="Simplified Route")

    # Show the map
    fig.show()


if __name__ == "__main__":
    accesstoken = '<your plotly accesstoken>'
    # read init route .xlsx data
    init_route = read_excel_init_route("data/CNDJK-BRPDM.xlsx")
    # clean route data (drop total nan columns)
    cleaned_route = clean_route(init_route)
    # log route length before simplification
    logger.info(f"Route length before simplification: {len(cleaned_route)}")
    # use rdp algorithm to simplify the route
    simplified_route = simplify_route(cleaned_route)
    # log route length after simplification
    logger.info(f"Route length after simplification: {len(simplified_route)}")
    # convert to json
    simplified_route_json = convert_to_json(simplified_route)
    # write to file
    with open("data/CNDJK-BRPDM_simplified.json", "w") as f:
        f.write(simplified_route_json)
    # show route on the map
    show_route(cleaned_route, simplified_route, accesstoken)
