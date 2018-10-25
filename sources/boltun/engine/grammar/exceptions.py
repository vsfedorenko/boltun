from __future__ import absolute_import, division, print_function

import attr


@attr.s
class RecognitionDisabledException(Exception):
    mode = attr.ib()
    recognizer = attr.ib()

    offending_token = attr.ib()

    def __attrs_post_init__(self):
        self.message = "Recognition of '%s' " \
                       "expressions is disabled" % self.mode.name
        self.offending_token = self.recognizer.getCurrentToken()

    def __str__(self):
        return self.message


__all__ = ['RecognitionDisabledException']
