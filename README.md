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

# Assumptions
- The **area threshold used is 300 square meters**. This follows RA 7279, which defines "small property owners" as those whose only real property consists of residential lands NOT EXCEEDING 300 square meters in highly urbanized cities. For the purposes of this exercise, the two other qualifiers ("residential lands" and "highly urbanized cities") are ignored.

# Algorithm:
1. Start
2. Load parcel data from JSON file
3. Convert each record into a Parcel object
4. If no parcels are loaded:
    - Display error message
    - Stop program
5. Initialize the following:
    - `total_active_area` = 0 sqm
    - `threshold_area` = TBD sqm
    - `large_parcels` = empty list
    - `count_per_zone` = emtpy dict
    - `target_zone` = residential or commercial
    - `intersecting_parcels` = empty list
6. For each parcel:
    - If `parcel.is_active` == True &rarr; Calculate new `total_active_area` = `total_active_area` + `parcel.area_sqm`
    - If `parcel.area_sqm` > `threshold_area` &rarr; add parcel to `large_parcels`
    - If `parcel.zone` in keys of `count_per_zone`:
        - Calculate `count_per_zone[zone]` += 1
    - Else: Calculate `count_per_zone[zone]` = 1
    - If `parcel.zone` == `target_zone` &rarr; add parcel to `intersecting_parcels`
7. Display `total_active_area`
8. Display `large_parcels`
9. Display `count_per_zone`
10. Display `intersecting_parcels`

# Pseudocode

BEGIN
LOAD parcels from JSON file
CONVERT parcels into Parcel objects
STORE in parcel_list

IF parcel_list is empty THEN
PRINT "No parcels found."
STOP
END IF

SET total_active_area = 0
SET threshold_area = TBD
SET large_parcels = empty list
SET count_per_zone = empty dict
SET target_zone = residential or commercial
SET intersecting_parcels = empty list

FOR EACH parcel IN parcel_list:
    IF parcel.is_active == True
    SET total_active_area = total_active_area + parcel.area
    END IF

    IF parcel.area_sqm > threshold_area
    APPEND parcel to large_parcels
    END IF

    IF parcel.zone NOT IN count_per_zone.keys()
    SET count_per_zone[parcel.zone] += 1
    ELSE
    SET count_per_zone[parcel.zone] = 1
    END IF

    IF parcel.zone == target_zone
    APPEND parcel to intersecting_parcels
    END IF
END FOR

DISPLAY total_active_area
DISPLAY large_parcels
DISPLAY count_per_zone
DISPLAY intersecting_parcels