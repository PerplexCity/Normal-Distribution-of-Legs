# Normal Distribution of Legs
These are simulation scripts and subsequent data used for all analysis done in the "Normal Distribution of Legs" article on perplex.city.

The [manspreading.py](../master/manspreading.py) script simulates 10,000 trials of men and women filling a subway car, printing final male passengers, final female passengers, maximum female passengers (upon rearrangement), real total, and adjusted total for each simulation.

The results of running this script once is found in [seats.csv](../master/seats.csv) and is converted to histograms using [manspreading_hist.R](../master/manspreading_hist.R).

Meanwhile, [splitseats.py](../master/splitseats.py) simulates dividing cars by gender, printing 5,000 trials of all women totals and then 5,000 trials of all men totals. One such run of this script is found in [splitseats.csv](../master/splitseats.csv), which can be fed into [splitseats.R](../master/splitseats.R) to get the graphs.
