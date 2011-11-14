import doctest
import unittest
from base import SocialMediaTestCase
from Testing.ZopeTestCase import FunctionalDocFileSuite


OPTIONFLAGS = (doctest.REPORT_ONLY_FIRST_FAILURE |
               doctest.ELLIPSIS |
               doctest.NORMALIZE_WHITESPACE)


def test_suite():
    return unittest.TestSuite((
            FunctionalDocFileSuite('installation.txt',
                  optionflags=OPTIONFLAGS,
                  package='eea.socialmedia.tests',
                  test_class=SocialMediaTestCase),
            ))


if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')

