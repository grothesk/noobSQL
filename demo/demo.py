import os
import time
import docker

from noobSQL.utils.db import Connection, Naming
from noobSQL.bi.bio import BIResponder


HERE = os.path.dirname(__file__)


if __name__ == '__main__':
    # Initialize docker client
    cli = docker.from_env()

    # Build a docker image
    cli.images.build(path=HERE, tag='docker_pg')

    # Create and run a container
    container = cli.containers.run(
        image='docker_pg',
        detach=True,
        ports={5432: 5432}
    )

    # Wait to make sure that the container is up and running
    time.sleep(5) # todo: There must be a better way...

    # Run noobSQL demo
    file = 'demo.yml'
    connection = Connection.from_yaml(file)
    naming = Naming.from_yaml(file)

    bir = BIResponder(connection, naming)
    dau, query = bir.daily_active_user()

    print(query)
    print(dau)

    # Kill the container
    container.kill()
