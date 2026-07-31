"""Tests covering the IQR-based outlier detection demonstrated in:

3.Data_Preprocessing_&_EDA/2.Feature_Engineering/4.0-Handling+Outliers.ipynb

The notebook computes the five-number summary with `np.quantile`, derives
the IQR, and flags values outside `[Q1 - 1.5*IQR, Q3 + 1.5*IQR]` as outliers.
It uses two example datasets: one without outliers and one with several
extreme values added.
"""
import pytest

np = pytest.importorskip("numpy")


NO_OUTLIER_MARKS = [45, 32, 56, 75, 89, 54, 32, 89, 90, 87, 67, 54, 45, 98, 99, 67, 74]
WITH_OUTLIER_MARKS = NO_OUTLIER_MARKS + [-100, -200, 150, 170, 180]


def _five_number_summary(data):
    return np.quantile(data, [0, 0.25, 0.50, 0.75, 1.0])


def test_five_number_summary_matches_documented_values():
    minimum, q1, median, q3, maximum = _five_number_summary(NO_OUTLIER_MARKS)
    assert minimum == pytest.approx(32.0)
    assert q1 == pytest.approx(54.0)
    assert median == pytest.approx(67.0)
    assert q3 == pytest.approx(89.0)
    assert maximum == pytest.approx(99.0)


def test_iqr_and_fences_match_documented_values():
    _, q1, _, q3, _ = _five_number_summary(NO_OUTLIER_MARKS)
    iqr = q3 - q1
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr

    assert iqr == pytest.approx(35.0)
    assert lower_fence == pytest.approx(1.5)
    assert upper_fence == pytest.approx(141.5)


def test_no_outliers_detected_in_clean_dataset():
    _, q1, _, q3, _ = _five_number_summary(NO_OUTLIER_MARKS)
    iqr = q3 - q1
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr

    outliers = [v for v in NO_OUTLIER_MARKS if v < lower_fence or v > upper_fence]
    assert outliers == []


def test_outliers_detected_when_extreme_values_are_present():
    _, q1, _, q3, _ = _five_number_summary(WITH_OUTLIER_MARKS)
    iqr = q3 - q1
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr

    outliers = sorted(
        v for v in WITH_OUTLIER_MARKS if v < lower_fence or v > upper_fence
    )

    # The extreme values added on top of the clean dataset should all be
    # flagged, while the original, non-extreme values should not be.
    for extreme_value in (-100, -200, 150, 170, 180):
        assert extreme_value in outliers

    for original_value in NO_OUTLIER_MARKS:
        assert original_value not in outliers


def test_outlier_fence_ordering_is_lower_less_than_upper():
    _, q1, _, q3, _ = _five_number_summary(WITH_OUTLIER_MARKS)
    iqr = q3 - q1
    lower_fence = q1 - 1.5 * iqr
    upper_fence = q3 + 1.5 * iqr
    assert lower_fence < upper_fence


def test_iqr_is_zero_for_constant_dataset():
    constant_data = [10] * 20
    _, q1, _, q3, _ = _five_number_summary(constant_data)
    assert q3 - q1 == 0