from flask import render_template
from . import app
from . import flatpages


def allarticles(flatpages):
    return (p for p in flatpages if "published" in p.meta)


def alltags(flatpages):
    tags = list()
    for p in flatpages:
        if "published" in p.meta:
            for tag in p.meta.get("tags", []):
                tags.append(tag)
    return list(set(tags))


@app.route("/")
def index():
    published = allarticles(flatpages)
    latest = sorted(published, reverse=True,
                    key=lambda p: p.meta["published"])
    tags = alltags(flatpages)
    return render_template("index.html",
                           articles=latest[:10], alltags=tags)


@app.route("/all/")
def all():
    published = allarticles(flatpages)
    latest = sorted(published, reverse=True,
                    key=lambda p: p.meta["published"])
    return render_template("all.html", articles=latest[:])


@app.route("/<path:path>/")
def article(path):
    article = flatpages.get_or_404(path)
    articles = sorted(
        allarticles(flatpages), reverse=True,
        key=lambda p: p.meta["published"])
    now = articles.index(article)
    before = articles[now - 1] if now - 1 >= 0 else False
    after = articles[now + 1] if now + 1 < len(articles) else False
    return render_template("article.html",
                           article=article, before=before, after=after)


@app.route("/tag/<string:tag>/")
def tag(tag):
    tagged = [p for p in flatpages if tag in p.meta.get("tags", [])]
    return render_template("tag.html", articles=tagged, tag=tag)
