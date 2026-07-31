"""Tests covering Target Guided Ordinal Encoding demonstrated in:

3.Data_Preprocessing_&_EDA/2.Feature_Engineering/8.0-Target+Guided+Ordinal+Encoding.ipynb

The notebook encodes a categorical 'city' column by mapping each category to
the mean of the target ('price') variable for that category:

    mean_price = df.groupby('city')['price'].mean().to_dict()
    df['city_encoded'] = df['city'].map(mean_price)
"""
import pytest

pd = pytest.importorskip("pandas")


@pytest.fixture
def city_price_df():
    return pd.DataFrame(
        {
            "city": ["New York", "London", "Paris", "Tokyo", "New York", "Paris"],
            "price": [200, 150, 300, 250, 180, 320],
        }
    )


def test_groupby_mean_matches_documented_values(city_price_df):
    mean_price = city_price_df.groupby("city")["price"].mean()

    assert mean_price["London"] == pytest.approx(150.0)
    assert mean_price["New York"] == pytest.approx(190.0)
    assert mean_price["Paris"] == pytest.approx(310.0)
    assert mean_price["Tokyo"] == pytest.approx(250.0)


def test_target_guided_encoding_maps_each_row_to_its_city_mean(city_price_df):
    mean_price = city_price_df.groupby("city")["price"].mean().to_dict()
    city_price_df["city_encoded"] = city_price_df["city"].map(mean_price)

    expected = [190.0, 150.0, 310.0, 250.0, 190.0, 310.0]
    assert city_price_df["city_encoded"].tolist() == pytest.approx(expected)


def test_target_guided_encoding_preserves_row_count_and_no_missing_values(city_price_df):
    mean_price = city_price_df.groupby("city")["price"].mean().to_dict()
    city_price_df["city_encoded"] = city_price_df["city"].map(mean_price)

    assert city_price_df["city_encoded"].shape[0] == city_price_df.shape[0]
    assert city_price_df["city_encoded"].isnull().sum() == 0


def test_target_guided_encoding_ordering_reflects_target_ranking(city_price_df):
    # The documented ordering is: London < New York < Tokyo < Paris.
    mean_price = city_price_df.groupby("city")["price"].mean().to_dict()
    assert mean_price["London"] < mean_price["New York"] < mean_price["Tokyo"] < mean_price["Paris"]


def test_target_guided_encoding_gives_same_code_to_same_category(city_price_df):
    mean_price = city_price_df.groupby("city")["price"].mean().to_dict()
    city_price_df["city_encoded"] = city_price_df["city"].map(mean_price)

    new_york_rows = city_price_df[city_price_df["city"] == "New York"]
    assert new_york_rows["city_encoded"].nunique() == 1

    paris_rows = city_price_df[city_price_df["city"] == "Paris"]
    assert paris_rows["city_encoded"].nunique() == 1


def test_target_guided_encoding_maps_unseen_category_to_nan(city_price_df):
    # If a category wasn't present in the training mapping, map() should
    # produce NaN for it - an important edge case not explicitly covered by
    # the notebook, but implied by pandas' Series.map() semantics.
    mean_price = city_price_df.groupby("city")["price"].mean().to_dict()
    unseen = pd.Series(["Berlin"])
    encoded_unseen = unseen.map(mean_price)
    assert encoded_unseen.isnull().all()