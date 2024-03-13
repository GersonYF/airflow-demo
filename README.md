# airflow

                      +--------------+                  +------------+
                      |              |                  |            |
                      |  Webserver   +------------------>  Scheduler |
                      |              |                  |            |
                      +------+-------+                  +-----+------+
                             |                                |
                             |                                |
                             v                                v
                    +--------+--------+              +-------+-------+
                    |                 |              |               |
                    |  PostgreSQL DB  <--------------+  Worker       |
                    |                 |              |  (Celery)     |
                    +--------+--------+              +-------+-------+
                             ^                                ^
                             |                                |
                             |                                |
                      +------+-------+              +--------+--------+
                      |             |              |                 |
                      |  Redis      |              |  Triggerer      |
                      |             |              |                 |
                      +-------------+              +-----------------+

Webserver: UI for DAGs workspace, it's connected to PostgreSQL to store and retrieve metadata, interacting with the scheduler to run tasks.
Scheduler: Decides when and where to execute the tasks based in the DAGs configuration. Interacts with the DB to keep the state of tasks and Redis to send the tasks to the workers.
Worker: Executes the given tasks by the Redis broker.
Triggerer: To monitor the tasks waiting for external events to complete.
PostgreSQL: Database to store DAGs metadata, tasks configurations and execution states.
Redis: Acts as a message broker between the scheduler and the workers.
Flower: Tasks queues monitoring.
airflow-init: It starts everything we need in order to function and get or UI running.

## Up & running!
Rename the ***_env_template*** to ***.env*** and update with your values.

In the root folder execute the next in order to initialize wour workspace.

docker compose up airflow-init -d

### Start UI

docker compose up -d

## Cleaning-up the environment

docker compose down --volumes --remove-orphans

## Go on!

go to http://localhost:8080 and login with **airflow** - **airflow**


## References

https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

