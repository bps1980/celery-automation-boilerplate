A diagram showing:

[ Celery Beat ]
       |
       v
[ Scheduled Task ]
       |
       v
[ Celery Worker ]
       |
       v
[ Result Backend ]

Parallel branch:
[ Client ] → [ example_task ] → [ Worker ]

Arrows show:
- Beat triggers scheduled tasks
- Workers execute tasks
- Results stored in backend
