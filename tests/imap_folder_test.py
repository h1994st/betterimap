# coding: utf-8

import unittest
import betterimap


class IMAPFolderTest(unittest.TestCase):
    def test_parse_flags(self):
        fld = betterimap.IMAPFolder(
            ur'(\\HasNoChildren \\Sent \\Sent) "." "Sent Folder"')
        self.assertEqual(fld.name, u'Sent Folder')
        self.assertSetEqual(fld.flags, set(['HasNoChildren', 'Sent']))

    def test_parse_no_flags(self):
        fld = betterimap.IMAPFolder(
            u'() "." "Sent Folder"')
        self.assertSetEqual(fld.flags, set())

    def test_parse_utf7(self):
        fld = betterimap.IMAPFolder(
            r'(\\Unmarked \\HasNoChildren \\Sent) "|" '
            '"&BB4EQgQ,BEAEMAQyBDsENQQ9BD0ESwQ1-"'
        )
        self.assertEqual(fld.name, u'Отправленные')
        self.assertSetEqual(
            fld.flags, set(['Unmarked', 'HasNoChildren', 'Sent']))
