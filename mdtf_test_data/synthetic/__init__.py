""" Module for generating synthetic datasets """

from .synthetic import (
    dataset_stats,
    generate_daily_time_axis,
    generate_hourly_time_axis,
    generate_monthly_time_axis,
    generate_synthetic_dataset,
    generate_random_array,
    gfdl_vertical_coord,
    gfdl_plev19_vertical_coord,
    ncar_hybrid_coord,
    write_to_netcdf,
)
