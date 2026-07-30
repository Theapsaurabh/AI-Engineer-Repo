"""Tests covering the missing-value handling techniques demonstrated in:

3.Data_Preprocessing_&_EDA/2.Feature_Engineering/1.0-+Handling+Missing+values+(1).ipynb

The notebook works against the seaborn 'titanic' dataset (fetched from the
network), which is not suitable for unit tests. Instead, these tests use a
small, deterministic synthetic DataFrame that reproduces the same shape of
problem (numeric column with missing values, categorical column with a
missing value) and exercises exactly the same pandas operations shown in the
notebook:

- df.isnull().sum() / df.dropna() / df.dropna(axis=1)
- Series.fillna(mean) / Series.fillna(median)
- mode-based imputation for categorical columns
"""
import pytest

pd = pytest.importorskip("pandas")


@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {
            "age": [22.0, 38.0, 26.0, None, 35.0, None, 40.0],
            "embarked": ["S", "C", None, "S", "Q", "S", None],
            "fare": [7.25, 71.28, 7.92, 53.10, 8.05, 13.0, 30.0],
        }
    )


def test_isnull_sum_reports_missing_counts_per_column(sample_df):
    missing_counts = sample_df.isnull().sum()
    assert missing_counts["age"] == 2
    assert missing_counts["embarked"] == 2
    assert missing_counts["fare"] == 0


def test_dropna_removes_rows_with_any_missing_value(sample_df):
    dropped = sample_df.dropna()
    assert dropped.shape[0] == 4
    assert dropped.isnull().sum().sum() == 0


def test_dropna_axis_1_removes_columns_with_any_missing_value(sample_df):
    dropped = sample_df.dropna(axis=1)
    assert list(dropped.columns) == ["fare"]
    assert dropped.shape[0] == sample_df.shape[0]


def test_mean_imputation_fills_all_missing_values(sample_df):
    mean_value = sample_df["age"].mean()
    imputed = sample_df["age"].fillna(mean_value)
    assert imputed.isnull().sum() == 0
    # Original non-missing entries must remain unchanged.
    assert imputed.iloc[0] == 22.0
    assert imputed.iloc[1] == 38.0
    # Missing entries are replaced with the column mean.
    assert imputed.iloc[3] == pytest.approx(mean_value)
    assert imputed.iloc[5] == pytest.approx(mean_value)


def test_median_imputation_fills_all_missing_values(sample_df):
    median_value = sample_df["age"].median()
    imputed = sample_df["age"].fillna(median_value)
    assert imputed.isnull().sum() == 0
    assert imputed.iloc[3] == pytest.approx(median_value)


def test_median_imputation_is_robust_to_outliers():
    # Median imputation should be far less affected by an extreme outlier
    # than mean imputation, matching the rationale documented in the
    # notebook/markdown guides.
    s = pd.Series([155.0, 160.0, 165.0, 170.0, 175.0, 300.0, None])
    mean_imputed_value = s.fillna(s.mean()).iloc[-1]
    median_imputed_value = s.fillna(s.median()).iloc[-1]
    assert mean_imputed_value > median_imputed_value
    assert median_imputed_value == pytest.approx(167.5)


def test_mode_imputation_for_categorical_column_uses_most_frequent_value(sample_df):
    mode_value = sample_df[sample_df["embarked"].notna()]["embarked"].mode()[0]
    assert mode_value == "S"

    imputed = sample_df["embarked"].fillna(mode_value)
    assert imputed.isnull().sum() == 0
    assert imputed.iloc[2] == "S"
    assert imputed.iloc[6] == "S"
    # Non-missing values must be preserved.
    assert imputed.iloc[1] == "C"
    assert imputed.iloc[4] == "Q"


def test_notna_filter_excludes_missing_rows_before_mode_calculation(sample_df):
    non_missing = sample_df[sample_df["embarked"].notna()]
    assert non_missing.shape[0] == 5
    assert non_missing["embarked"].isnull().sum() == 0


def test_dropna_on_dataframe_with_no_missing_values_is_a_no_op():
    df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    result = df.dropna()
    pd.testing.assert_frame_equal(result, df)


def test_fillna_on_column_with_all_missing_values_uses_nan_mean():
    # Edge case: mean of an all-missing column is NaN, so fillna should
    # leave the column unchanged (still all missing) rather than raising.
    s = pd.Series([None, None, None], dtype="float64")
    result = s.fillna(s.mean())
    assert result.isnull().all()