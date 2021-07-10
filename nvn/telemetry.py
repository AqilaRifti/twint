# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import platform

def machine_telemetry() -> dict:
    machine = platform.machine()
    node = platform.node()
    system = platform.system()
    processor = platform.processor()
    arch = platform.architecture()
    return {
        "machine": machine,
        "node": node,
        "system": system,
        "processor": processor,
        "arch": arch
    }
print(machine_telemetry())