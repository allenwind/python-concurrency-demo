#分布式任务队列Celery

#架构组成

#消息中间人 Broker 任务调度队列
#是一个生产者消费者模式，即主程序将任务放入队列中，而后台职程则会从队列中取出任务并执行
#Redis、RabbitMQ

#任务执行单元 Worker

#执行结果存储 Backend


from celery import Celery

app = Celery('tasks',
             broker='amqp://guest@localhost//', #Broker 任务调度队列
             backend='redis://localhost:6379/0')

@app.task
def add(x, y):
    return x + y
