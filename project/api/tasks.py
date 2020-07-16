from background_task import background
from logging import getLogger

logger = getLogger(__name__)


@background(schedule=60)
def demo_task():
    print('This sentence should be printed per 10 seconds')
