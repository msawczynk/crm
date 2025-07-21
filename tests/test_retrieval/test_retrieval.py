from retrieval import index, search


def test_index_and_search() -> None:
    pages = {"http://a": "hello world", "http://b": "other"}
    index(pages)
    results = search("hello", top_k=1)
    assert results[0][0] == "http://a"
