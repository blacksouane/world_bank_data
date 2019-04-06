from world_bank_data import get_lendingtypes, get_incomelevels, get_sources, get_topics
from .tools import assert_numeric_or_string


def test_lending_types():
    df = get_lendingtypes()
    assert df.index.names == ['id']
    assert df.columns.to_list() == ['iso2code', 'value']
    assert_numeric_or_string(df)


def test_income_levels():
    df = get_incomelevels()
    assert df.index.names == ['id']
    assert df.columns.to_list() == ['iso2code', 'value']
    assert_numeric_or_string(df)


def test_topics():
    df = get_topics()
    assert df.index.names == ['id']
    assert df.columns.to_list() == ['value', 'sourceNote']
    assert_numeric_or_string(df)


def test_sources():
    df = get_sources()
    assert df.index.names == ['id']
    assert df.columns.to_list() == ['lastupdated', 'name', 'code', 'description', 'url', 'dataavailability',
                                    'metadataavailability', 'concepts']
    assert_numeric_or_string(df)
