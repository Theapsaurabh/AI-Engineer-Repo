"""Tests validating the worked numerical examples documented in:

- 1.Math/C.Statistics_&_Probability/1.Statistics.md
- 1.Math/C.Statistics_&_Probability/Descriptive_Statistics.md

These files are Markdown reference guides containing hand-computed examples
(mean/median/variance/std-dev, five-number summaries, IQR-based outlier
fences, covariance and Pearson correlation). Since the guides present exact
numeric results, these tests re-derive the same figures independently (using
only the Python standard library, so they need no extra dependencies) to
guard against silent regressions/typos if the documented examples are ever
changed or reused elsewhere (e.g. extracted into example code).
"""
import statistics
import pytest


# ---------------------------------------------------------------------------
# Helpers (kept local/pure-stdlib to avoid any dependency on external
# packages such as numpy/pandas which are not required to validate the
# documented arithmetic).
# ---------------------------------------------------------------------------

def sample_covariance(x, y):
    if len(x) != len(y):
        raise ValueError("x and y must have the same length")
    n = len(x)
    mean_x = statistics.mean(x)
    mean_y = statistics.mean(y)
    total = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    return total / (n - 1)


def pearson_correlation(x, y):
    cov = sample_covariance(x, y)
    return cov / (statistics.stdev(x) * statistics.stdev(y))


def five_number_summary_simple(data):
    """Replicates the simple 'median of halves' method used in the
    Five-Number-Summary worked example of 1.Statistics.md."""
    sorted_data = sorted(data)
    n = len(sorted_data)
    minimum = sorted_data[0]
    maximum = sorted_data[-1]
    median = statistics.median(sorted_data)
    if n % 2 == 0:
        lower_half = sorted_data[: n // 2]
        upper_half = sorted_data[n // 2:]
    else:
        lower_half = sorted_data[: n // 2]
        upper_half = sorted_data[n // 2 + 1:]
    q1 = statistics.median(lower_half)
    q3 = statistics.median(upper_half)
    return minimum, q1, median, q3, maximum


# ---------------------------------------------------------------------------
# Student heights example (both markdown files use this dataset).
# ---------------------------------------------------------------------------

HEIGHTS = [155, 160, 165, 170, 175, 180]


def test_heights_mean_and_median_are_symmetric():
    assert statistics.mean(HEIGHTS) == pytest.approx(167.5)
    assert statistics.median(HEIGHTS) == pytest.approx(167.5)


def test_heights_population_variance_and_stddev():
    # Documented values: population variance = 72.92, population std ~ 8.54
    assert statistics.pvariance(HEIGHTS) == pytest.approx(72.9166667, rel=1e-6)
    assert statistics.pstdev(HEIGHTS) == pytest.approx(8.54, abs=0.01)


def test_heights_sample_variance_and_stddev():
    # Documented values: sample variance = 87.50, sample std ~ 9.35
    assert statistics.variance(HEIGHTS) == pytest.approx(87.5)
    assert statistics.stdev(HEIGHTS) == pytest.approx(9.35, abs=0.01)


def test_heights_five_number_summary_simple_method():
    minimum, q1, median, q3, maximum = five_number_summary_simple(HEIGHTS)
    assert (minimum, q1, median, q3, maximum) == (155, 160, 167.5, 175, 180)
    iqr = q3 - q1
    assert iqr == 15


def test_heights_no_outliers_via_iqr_fences():
    minimum, q1, median, q3, maximum = five_number_summary_simple(HEIGHTS)
    iqr = q3 - q1
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    assert all(lower_fence <= v <= upper_fence for v in HEIGHTS)


# ---------------------------------------------------------------------------
# 19-value quartile / IQR worked example (Descriptive_Statistics.md), which
# uses the "position = p * (n + 1)" quartile method (equivalent to the
# 'exclusive' quantile estimation method).
# ---------------------------------------------------------------------------

NINETEEN_VALUES = [1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 6, 6, 6, 7, 8, 8, 9, 9]


def test_position_formula_quartiles_match_documented_values():
    q1, median, q3 = statistics.quantiles(
        NINETEEN_VALUES, n=4, method="exclusive"
    )
    assert (q1, median, q3) == pytest.approx((3.0, 5.0, 7.0))


def test_iqr_and_outlier_fences_for_nineteen_values():
    q1, median, q3 = statistics.quantiles(
        NINETEEN_VALUES, n=4, method="exclusive"
    )
    iqr = q3 - q1
    assert iqr == pytest.approx(4.0)

    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    assert lower_fence == pytest.approx(-3.0)
    assert upper_fence == pytest.approx(13.0)

    # All values in the dataset fall within the fences -> no outliers,
    # matching the documented conclusion.
    assert all(lower_fence <= v <= upper_fence for v in NINETEEN_VALUES)


# ---------------------------------------------------------------------------
# Petal length variance/std-dev example (Descriptive_Statistics.md).
# ---------------------------------------------------------------------------

PETAL_LENGTHS = [5, 8, 12, 15, 20]


def test_petal_length_mean_variance_and_stddev():
    assert statistics.mean(PETAL_LENGTHS) == 12
    assert statistics.variance(PETAL_LENGTHS) == pytest.approx(34.5)
    assert statistics.stdev(PETAL_LENGTHS) == pytest.approx(5.87, abs=0.01)


# ---------------------------------------------------------------------------
# Covariance / Pearson correlation example (hours studied vs. exam score).
# ---------------------------------------------------------------------------

HOURS = [2, 3, 4, 5, 6]
SCORES = [50, 60, 70, 80, 90]


def test_covariance_matches_documented_value():
    assert sample_covariance(HOURS, SCORES) == pytest.approx(25.0)


def test_pearson_correlation_is_near_perfect_positive():
    # The documented example reports r ~= 1.00 (a near-perfect positive
    # linear relationship between study hours and exam score).
    r = pearson_correlation(HOURS, SCORES)
    assert r == pytest.approx(1.0, abs=0.01)


# ---------------------------------------------------------------------------
# Edge cases / negative cases not explicitly present in the guide but
# important to guard the helper functions used above against misuse.
# ---------------------------------------------------------------------------

def test_sample_variance_of_constant_data_is_zero():
    constant_data = [10, 10, 10, 10]
    assert statistics.variance(constant_data) == 0


def test_sample_variance_requires_at_least_two_points():
    with pytest.raises(statistics.StatisticsError):
        statistics.variance([42])


def test_covariance_raises_on_mismatched_lengths():
    with pytest.raises(ValueError):
        sample_covariance([1, 2, 3], [1, 2])