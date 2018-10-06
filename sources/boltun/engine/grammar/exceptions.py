from __future__ import absolute_import

import attr


@attr.s
class RecognitionDisabledException(Exception):

    def __init__(self, mode=None, recognizer=None):
        super(RecognitionDisabledException, self) \
            .__init__("Recognition of '{mode}' expressions "
                      "is disabled" % mode.name)

        self.mode = mode
        self.offending_token = recognizer.getCurrentToken()

    def __str__(self):
        return self.message


__all__ = ['RecognitionDisabledException']
