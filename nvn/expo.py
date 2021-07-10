# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
defined = []

def define(var):
    global defined
    defined = set(defined)
    defined = list(defined)
    defined.append(var)
    defined = set(defined)

def undef(var):
    global defined
    defined = set(defined)
    defined = list(defined)
    for i in range(len(defined)):
        if var == defined[i]:
            del defined[i]
    defined = set(defined)

