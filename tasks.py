from invoke import task

@task
def crawler(ctx):
    ctx.run("python3 crawler/crawler.py")