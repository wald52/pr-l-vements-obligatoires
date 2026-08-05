from po_pipeline.schema import normalize_label, slugify, strip_accents


def test_strip_accents():
    assert strip_accents("Prélèvement") == "Prelevement"


def test_normalize_label():
    assert normalize_label("  Taxe   sur la  VALEUR ajoutée ") == "taxe sur la valeur ajoutee"
    assert normalize_label(None) == ""


def test_slugify_stable():
    assert slugify("Taxe sur la valeur ajoutée (TVA)") == "taxe-sur-la-valeur-ajoutee-tva"
    assert slugify("") == "sans-nom"
