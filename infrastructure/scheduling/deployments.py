from datetime import datetime
from prefect.deployments import Deployment

import flows

from zoneinfo import ZoneInfo

berlin_tz = ZoneInfo("Europe/Berlin")
now = datetime.now(berlin_tz)

deployment1 = Deployment.build_from_flow(
    flow=flows.main_flow,
    name="Main Flow",
    version=1,
    description="Runs a long running python task with shell_run_command",
    path="/app/",
)


for deployment in [deployment1]:
    deployment.apply()
