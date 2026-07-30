"""Tests covering Label Encoding and Ordinal Encoding demonstrated in:

3.Data_Preprocessing_&_EDA/2.Feature_Engineering/7.0-Label+and+Ordinal.ipynb

The notebook contrasts:
- `sklearn.preprocessing.LabelEncoder`, which assigns arbitrary
  (alphabetically-ordered) integer labels to a nominal categorical column.
- `sklearn.preprocessing.OrdinalEncoder`, which maps categories to integers
  according to an explicitly supplied, meaningful order.
"""
import pytest

pd = pytest.importorskip("pandas")
sklearn_preprocessing = pytest.importorskip("sklearn.preprocessing")
LabelEncoder = sklearn_preprocessing.LabelEncoder
OrdinalEncoder = sklearn_preprocessing.OrdinalEncoder


@pytest.fixture
def color_df():
    return pd.DataFrame({"color": ["red", "blue", "green", "green", "red", "blue"]})


@pytest.fixture
def size_df():
    return pd.DataFrame(
        {"size": ["small", "medium", "large", "medium", "small", "large"]}
    )


def test_label_encoder_assigns_labels_in_alphabetical_order(color_df):
    encoder = LabelEncoder()
    encoded = encoder.fit_transform(color_df["color"])

    # Alphabetical order: blue -> 0, green -> 1, red -> 2
    assert list(encoder.classes_) == ["blue", "green", "red"]
    assert list(encoded) == [2, 0, 1, 1, 2, 0]


def test_label_encoder_transform_is_consistent_with_fit(color_df):
    encoder = LabelEncoder()
    encoder.fit(color_df["color"])
    assert encoder.transform(["red"])[0] == 2
    assert encoder.transform(["blue"])[0] == 0
    assert encoder.transform(["green"])[0] == 1


def test_label_encoder_inverse_transform_recovers_original_labels(color_df):
    encoder = LabelEncoder()
    encoded = encoder.fit_transform(color_df["color"])
    decoded = encoder.inverse_transform(encoded)
    assert list(decoded) == list(color_df["color"])


def test_label_encoder_raises_on_unseen_label(color_df):
    encoder = LabelEncoder()
    encoder.fit(color_df["color"])
    with pytest.raises(ValueError):
        encoder.transform(["purple"])


def test_ordinal_encoder_respects_explicit_category_order(size_df):
    encoder = OrdinalEncoder(categories=[["small", "medium", "large"]])
    encoded = encoder.fit_transform(size_df[["size"]])

    expected = [[0.0], [1.0], [2.0], [1.0], [0.0], [2.0]]
    assert encoded.tolist() == expected


def test_ordinal_encoder_transform_of_new_data_uses_fitted_order(size_df):
    encoder = OrdinalEncoder(categories=[["small", "medium", "large"]])
    encoder.fit(size_df[["size"]])

    assert encoder.transform([["small"]])[0][0] == 0.0
    assert encoder.transform([["medium"]])[0][0] == 1.0
    assert encoder.transform([["large"]])[0][0] == 2.0


def test_ordinal_encoder_ordering_reflects_intrinsic_rank(size_df):
    encoder = OrdinalEncoder(categories=[["small", "medium", "large"]])
    encoded = encoder.fit_transform(size_df[["size"]]).flatten()

    small_code = encoded[size_df["size"] == "small"][0]
    medium_code = encoded[size_df["size"] == "medium"][0]
    large_code = encoded[size_df["size"] == "large"][0]

    assert small_code < medium_code < large_code


def test_ordinal_encoder_raises_on_unknown_category_by_default(size_df):
    encoder = OrdinalEncoder(categories=[["small", "medium", "large"]])
    encoder.fit(size_df[["size"]])
    with pytest.raises(ValueError):
        encoder.transform([["extra_large"]])