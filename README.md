# Project Title
GmE 205 - Laboratory Exercise 4

# How to set up the virtual environment
1. Create a folder on your computer and open it in your IDE (e.g., VS Code)
2. Open the terminal then create the virtual environment by running the following:
    ```
    py -m venv .venv
    .\.venv\Scripts\activate
    ```
3. Press ```Ctrl + Shift + P``` in VS Code, search for *Python: Select Interpreter*, then choose the interpreter inside the ```.venv``` folder
4. Install the required packages by running the following in the terminal:
    ```
    python -m pip install --upgrade pip
    pip install pandas matplotlib
    ```
5. (Recommended) List the installed packages via:
    ```
    pip freeze > requirements.txt
    ```

# How to run Python scripts

In the terminal, ensuring that ```(.venv)``` is present in the prompt, run the following:
    ```
    python <folder/script_name.py>
    ```

# Questions for Lab Exercise

1. What is the total area of all active parcels?
2. Which parcels exceed a threshold area?
3. How many parcels are there per zone?
4. Which parcels intersect a proposed development boundary? (Only using the `zone` information, e.g., which parcels are residential/commercial and thus suitable for development.)

# Algorithm:
1. Start
2. Load parcel data from JSON file
3. Convert each record into a Parcel object
4. If no parcels are loaded:
    - Display error message
    - Stop program
5. Initialize the following:
    - `total_area` = 0 sqm
    - `threshold_area` = TBD sqm
    - `large_parcels` = empty list
    - `unique_zones` = list of unique zone types
    - `count_per_zone` = emtpy dict
    - `target_zone` = residential or commercial
    - `intersecting_parcels` = empty list
6. For each parcel:
    - Calculate new `total_area` = `total_area` + `parcel.area`
    - If `parcel.area` > `threshold_area` &rarr; add parcel to `large_parcels`
    - For each zone in `unique_zones`:
        - Initialize `count_in_zone`
        - If `parcel.zone` == zone &rarr; calculate new `count_in_zone` = `count_in_zone` + 1
        - Add `zone: count_in_zone` to `count_per_zone`
    - If `parcel.area` == `target_zone` &rarr; add parcel to `intersecting_parcels`
7. Display `total_area`
8. Display `large_parcels`
9. Display `count_per_zone`
10. Display `intersecting_parcels`