# DC Roadway Attribution
This project contains a script to compute the surface area of roadway artifacts in order to conceptualize the breadth of space given to various vehicles.

## methodology
Some notes on methodology are in comments in the code, but they'll be detailed here at some point.

## results
Findings as they stand (I'm sure these are more sigfigs than justifed):

- total bike_lanes length (mi): `106.98426966545586`
- total bike_lanes area (sq mi): `0.15778325802311755`
- total roadway_block length (mi): `1199.1203256650842`
- total roadway_block area (sq mi): `8.2635984754191`
- total protected_bike_lanes length (mi): `33.419663255045464`
- total protected_bike_lanes area (sq mi): `0.050998458607486516`
- percent of roadway length with bike lanes: `0.08921896107975463%`
- percent of roadway length with protected bike lanes: `0.027870149925537678%`
- percent of bike lane length with protection: `0.31237922509122235%`
- percent of roadway area comprised of bike lane area: `0.01909377113281334%`
- percent of roadway area comprised of protected bike lane area: `0.006171458930293689%`

## source datasets
|dataset|description|file date|
|---|---|---|
|[Roadway Block](https://opendata.dc.gov/datasets/roadway-block)|Information about block by block roadway segments in DC|6/8/23|
|[Bicycle Lanes](https://opendata.dc.gov/datasets/bicycle-lanes)|Information about various kinds of bike lanes in DC|6/1/23|
<!--|[Alleys and Parking](https://opendata.dc.gov/datasets/alleys-and-parking)|Information about alleyways and parking easements/lots in DC|6/8/23|-->

## usage
To run:
1. download the `GeoJSON`-formatted files for the above datasets, and place them in a `data` folder in the repo.
2. either use the included conda environment (requires Anaconda or [miniconda](https://docs.conda.io/en/latest/miniconda.html)) to pull package dependencies through an environment:

   ```shell
   conda env create
   conda activate dc-roadway-attribution
   ```

   or use `pip` (assumes python is already installed)

   ```shell
   pip install geopandas
   ```

3. run `compute.py`

   ```shell
   python compute.py
   ```
   
   or, within a Python terminal:

   ```python
    exec(open('compute.py').read())
    ```
