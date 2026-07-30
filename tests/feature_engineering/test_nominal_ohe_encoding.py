"""Tests covering One-Hot Encoding (nominal encoding) demonstrated in:

3.Data_Preprocessing_&_EDA/2.Feature_Engineering/5.0-Nominal+or+OHE.ipynb

The notebook builds a small categorical DataFrame (a 'color' column with
'red' / 'blue' / 'green' values) and encodes it with
`sklearn.preprocessing.OneHotEncoder`.
"""
import pytest

pd = pytest.importorskip("pandas")
OneHotEncoder = pytest.importorskip("sklearn.preprocessing").OneHotEncoder


@pytest.fixture
def color_df():
    return pd.DataFrame(
        {"color": ["red", "blue", "green", "green", "red", "blue"]}
    )


def test_one_hot_encoder_creates_one_column_per_category(color_df):
    encoder = OneHotEncoder()
    encoded = encoder.fit_transform(color_df[["color"]]).toarray()

    assert encoded.shape == (6, 3)
    assert list(encoder.get_feature_names_out()) == [
        "color_blue",
        "color_green",
        "color_red",
    ]


def test_one_hot_encoder_rows_are_mutually_exclusive_indicators(color_df):
    encoder = OneHotEncoder()
    encoded = encoder.fit_transform(color_df[["color"]]).toarray()

    # Every row should have exactly one "hot" (1.0) entry and the rest 0.0.
    for row in encoded:
        assert row.sum() == pytest.approx(1.0)
        assert set(row.tolist()) <= {0.0, 1.0}


def test_one_hot_encoder_maps_known_category_correctly(color_df):
    encoder = OneHotEncoder()
    encoder.fit(color_df[["color"]])
    feature_names = list(encoder.get_feature_names_out())

    encoded_red = encoder.transform([["red"]]).toarray()[0]
    encoded_blue = encoder.transform([["blue"]]).toarray()[0]
    encoded_green = encoder.transform([["green"]]).toarray()[0]

    assert encoded_red[feature_names.index("color_red")] == 1.0
    assert encoded_blue[feature_names.index("color_blue")] == 1.0
    assert encoded_green[feature_names.index("color_green")] == 1.0

    # And the non-matching columns for a given category must all be 0.
    assert encoded_red.sum() == 1.0
    assert encoded_blue.sum() == 1.0
    assert encoded_green.sum() == 1.0


def test_one_hot_encoder_result_can_be_reassembled_as_dataframe(color_df):
    encoder = OneHotEncoder()
    encoded = encoder.fit_transform(color_df[["color"]]).toarray()
    encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out())

    assert encoded_df.shape == (6, 3)
    # Row 0 is 'red' -> color_red should be 1, others 0.
    assert encoded_df.loc[0, "color_red"] == 1.0
    assert encoded_df.loc[0, "color_blue"] == 0.0
    assert encoded_df.loc[0, "color_green"] == 0.0


def test_one_hot_encoder_raises_on_unknown_category_by_default(color_df):
    # By default handle_unknown='error', so transforming a category that
    # was never seen during fit() should raise a ValueError.
    encoder = OneHotEncoder()
    encoder.fit(color_df[["color"]])
    with pytest.raises(ValueError):
        encoder.transform([["purple"]])


def test_one_hot_encoder_can_ignore_unknown_category_when_configured(color_df):
    encoder = OneHotEncoder(handle_unknown="ignore")
    encoder.fit(color_df[["color"]])
    encoded_unknown = encoder.transform([["purple"]]).toarray()[0]
    # An unknown category, when ignored, produces an all-zero row.
    assert encoded_unknown.sum() == 0.0