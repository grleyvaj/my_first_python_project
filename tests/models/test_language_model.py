import unittest

from examples.src.language_model import LanguageModel


class MyTestCase(unittest.TestCase):

    def test_when_get_languages_not_none(self) -> None:
        assert LanguageModel.get_languages() is not None

    def test_when_get_languages_has_elements(self) -> None:
        assert len(LanguageModel.get_languages()) > 0

    def test_when_get_languages_check_len_elements(self) -> None:
        for language in LanguageModel.get_languages():
            assert len(language) > 0


if __name__ == "__main__":
    unittest.main()
