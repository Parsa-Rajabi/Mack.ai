# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import sys
from wit import Wit

if len(sys.argv) != 1:
    print('usage: python ' + sys.argv[0])
    exit(1)
access_token = 'CDNAWIU4OA5JUBDQ3JESSC6AVZWRTDVR'

client = Wit(access_token=access_token)
client.interactive()
