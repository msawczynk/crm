from ingestion import embed


def test_embed_deterministic() -> None:
    vec1 = embed(["hello"])[0]
    vec2 = embed(["hello"])[0]
    assert vec1 == vec2
    assert len(vec1) == 8
