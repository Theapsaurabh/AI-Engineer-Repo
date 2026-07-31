"""Tests covering the up-sampling / down-sampling techniques demonstrated in:

3.Data_Preprocessing_&_EDA/2.Feature_Engineering/2.0-Handling+Imbalance+Dataset.ipynb

The notebook builds a synthetic 900 (class 0) vs 100 (class 1) imbalanced
dataset and uses sklearn.utils.resample to both up-sample the minority class
and down-sample the majority class. These tests reproduce that workflow with
a smaller synthetic dataset for speed, while asserting the same invariants
the notebook demonstrates.
"""
import pytest

np = pytest.importorskip("numpy")
pd = pytest.importorskip("pandas")
resample = pytest.importorskip("sklearn.utils").resample


@pytest.fixture
def imbalanced_df():
    np.random.seed(123)
    n_class_0, n_class_1 = 90, 10
    class_0 = pd.DataFrame(
        {
            "feature_1": np.random.normal(loc=0, scale=1, size=n_class_0),
            "feature_2": np.random.normal(loc=0, scale=1, size=n_class_0),
            "target": [0] * n_class_0,
        }
    )
    class_1 = pd.DataFrame(
        {
            "feature_1": np.random.normal(loc=2, scale=1, size=n_class_1),
            "feature_2": np.random.normal(loc=2, scale=1, size=n_class_1),
            "target": [1] * n_class_1,
        }
    )
    return pd.concat([class_0, class_1]).reset_index(drop=True)


def test_fixture_dataset_is_imbalanced(imbalanced_df):
    counts = imbalanced_df["target"].value_counts()
    assert counts[0] == 90
    assert counts[1] == 10


def test_upsampling_minority_class_balances_dataset(imbalanced_df):
    df_majority = imbalanced_df[imbalanced_df["target"] == 0]
    df_minority = imbalanced_df[imbalanced_df["target"] == 1]

    df_minority_upsampled = resample(
        df_minority,
        replace=True,
        n_samples=len(df_majority),
        random_state=42,
    )

    balanced = pd.concat([df_majority, df_minority_upsampled])
    counts = balanced["target"].value_counts()

    assert counts[0] == counts[1] == 90
    assert balanced.shape[0] == 180


def test_upsampling_samples_with_replacement_can_duplicate_rows(imbalanced_df):
    df_minority = imbalanced_df[imbalanced_df["target"] == 1]
    upsampled = resample(
        df_minority, replace=True, n_samples=50, random_state=42
    )
    # Since we asked for more rows (50) than exist in the minority class
    # (10), some original rows must necessarily be duplicated.
    assert upsampled.shape[0] == 50
    assert upsampled.duplicated().sum() > 0


def test_downsampling_majority_class_balances_dataset(imbalanced_df):
    df_majority = imbalanced_df[imbalanced_df["target"] == 0]
    df_minority = imbalanced_df[imbalanced_df["target"] == 1]

    df_majority_downsampled = resample(
        df_majority,
        replace=False,
        n_samples=len(df_minority),
        random_state=42,
    )

    balanced = pd.concat([df_majority_downsampled, df_minority])
    counts = balanced["target"].value_counts()

    assert counts[0] == counts[1] == 10
    assert balanced.shape[0] == 20


def test_downsampling_without_replacement_has_no_duplicate_rows(imbalanced_df):
    df_majority = imbalanced_df[imbalanced_df["target"] == 0]
    downsampled = resample(
        df_majority, replace=False, n_samples=10, random_state=42
    )
    assert downsampled.shape[0] == 10
    assert downsampled.duplicated().sum() == 0


def test_downsampling_without_replacement_cannot_exceed_population_size(imbalanced_df):
    df_minority = imbalanced_df[imbalanced_df["target"] == 1]
    with pytest.raises(ValueError):
        resample(df_minority, replace=False, n_samples=50, random_state=42)