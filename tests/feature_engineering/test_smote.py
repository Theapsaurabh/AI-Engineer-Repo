"""Tests covering the SMOTE over-sampling workflow demonstrated in:

3.Data_Preprocessing_&_EDA/2.Feature_Engineering/3.0-SMOTE.ipynb

The notebook creates an imbalanced binary classification dataset with
`sklearn.datasets.make_classification` and rebalances it using
`imblearn.over_sampling.SMOTE`. `imbalanced-learn` is an optional/extra
dependency, so these tests are skipped automatically if it is not installed.
"""
import pytest

np = pytest.importorskip("numpy")
make_classification = pytest.importorskip("sklearn.datasets").make_classification
imblearn_over_sampling = pytest.importorskip("imblearn.over_sampling")
SMOTE = imblearn_over_sampling.SMOTE


@pytest.fixture
def imbalanced_classification_data():
    X, y = make_classification(
        n_samples=300,
        n_redundant=0,
        n_features=2,
        n_clusters_per_class=1,
        weights=[0.90],
        random_state=12,
    )
    return X, y


def test_synthetic_dataset_is_imbalanced_as_expected(imbalanced_classification_data):
    _, y = imbalanced_classification_data
    n_class_0 = (y == 0).sum()
    n_class_1 = (y == 1).sum()
    assert n_class_0 > n_class_1
    # weights=[0.90] -> approximately 90% class 0 / 10% class 1
    assert n_class_0 == pytest.approx(300 * 0.90, abs=5)


def test_smote_balances_class_distribution(imbalanced_classification_data):
    X, y = imbalanced_classification_data
    oversample = SMOTE(random_state=42)
    X_resampled, y_resampled = oversample.fit_resample(X, y)

    n_class_0 = (y_resampled == 0).sum()
    n_class_1 = (y_resampled == 1).sum()

    assert n_class_0 == n_class_1
    assert X_resampled.shape[0] == y_resampled.shape[0]
    assert X_resampled.shape[0] == 2 * n_class_0


def test_smote_preserves_original_majority_class_samples(imbalanced_classification_data):
    X, y = imbalanced_classification_data
    oversample = SMOTE(random_state=42)
    X_resampled, y_resampled = oversample.fit_resample(X, y)

    # The majority class count should not shrink - SMOTE only synthesizes
    # new minority-class samples, it never removes majority samples.
    original_majority_count = (y == 0).sum()
    resampled_majority_count = (y_resampled == 0).sum()
    assert resampled_majority_count == original_majority_count


def test_smote_generates_new_synthetic_minority_samples(imbalanced_classification_data):
    X, y = imbalanced_classification_data
    original_minority_points = {tuple(row) for row in X[y == 1]}

    oversample = SMOTE(random_state=42)
    X_resampled, y_resampled = oversample.fit_resample(X, y)
    resampled_minority_points = X_resampled[y_resampled == 1]

    # There should be more minority samples after resampling than there
    # were original minority samples, and at least some of them must be
    # genuinely new (synthetic) points rather than exact duplicates.
    assert len(resampled_minority_points) > len(original_minority_points)
    synthetic_points = [
        row for row in resampled_minority_points
        if tuple(row) not in original_minority_points
    ]
    assert len(synthetic_points) > 0


def test_smote_raises_on_single_class_target(imbalanced_classification_data):
    X, _ = imbalanced_classification_data
    y_single_class = np.zeros(len(X), dtype=int)
    oversample = SMOTE(random_state=42)
    with pytest.raises(ValueError):
        oversample.fit_resample(X, y_single_class)