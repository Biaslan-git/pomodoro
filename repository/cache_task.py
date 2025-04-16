from redis import Redis
import json

from schema import TaskSchema

class TaskCache:
    def __init__(self, redis: Redis):
        self.redis = redis

    def get_tasks(self) -> list[TaskSchema]:
        with self.redis as redis:
            tasks_json = redis.lrange('tasks', 0, -1)
            res = []
            for task in tasks_json:
                print(task)
                res.append(TaskSchema.model_validate(json.loads(task)))
            return res


    def set_tasks(self, tasks: list[TaskSchema]):
        tasks_json = [task.json() for task in tasks]
        with self.redis as redis:
            redis.lpush('tasks', *tasks_json)


