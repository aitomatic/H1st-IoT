from __future__ import print_function

import datetime
import os
import subprocess

from h1st_pw.runtime import params

from h1st.util.date_time import month_str
from h1st.IoT.PredMaint import __path__


today = str(datetime.date.today())

cmd_args = [
    os.path.join(__path__[0], 'bin', 'h1st-iot-pm'),
    params.PROJECT,
    'ppp-anom-alert',
    params.EQUIPMENT_GENERAL_TYPE, params.EQUIPMENT_UNIQUE_TYPE_GROUP,
    month_str(today, n_months_offset=-3), '--to', str(today)
]


cmd = ' '.join(cmd_args)

print('\n*** RUNNING {}... ***\n'.format(cmd))

subprocess.check_call(cmd_args)

print('\n*** {} DONE! ***\n'.format(cmd))
