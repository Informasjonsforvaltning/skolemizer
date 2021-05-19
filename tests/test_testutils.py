"""Test cases for the testutils module."""
from skolemizer.testutils import SkolemUtils


def test_skolemutils() -> None:
    """Test the SkolemUtils class."""
    skolemutils = SkolemUtils()
    assert (
        "http://example.com/.well-known/skolem/284db4d2-80c2-11eb-82c3-83e80baa2f94"
        == skolemutils.get_skolemization()
    )
    assert (
        "http://example.com/.well-known/skolem/21043186-80ce-11eb-9829-cf7c8fc855ce"
        == skolemutils.get_skolemization()
    )
    assert (
        "http://example.com/.well-known/skolem/279b7540-80ce-11eb-ba1a-7fa81b1658fe"
        == skolemutils.get_skolemization()
    )
    assert skolemutils.get_skolemization() is None
