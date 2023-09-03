from typing import Iterator
from datetime import datetime
from itertools import groupby
from enum import Enum
from typer import Typer
from pydantic import BaseModel
import glob


class PostStatus(str, Enum):
    draft = 'draft'
    published = 'published'


class MetaPost(BaseModel):
    title: str
    date: datetime
    category: str
    status: PostStatus
    filename: str
    tags: list[str] = []


app = Typer()


@app.command()
def list_unpublished():
    blog_meta = read_blog_meta()
    for post in blog_meta:
        if post.status == PostStatus.draft:
            print(post.title, post.filename)


@app.command()
def list_categories():
    blog_meta = sorted(read_blog_meta(), key=lambda p: p.category)
    for category, posts in groupby(blog_meta, key=lambda p: p.category):
        print(category)
        for p in posts:
            print(f'- {p.title} ({p.filename})')
        print('')


def read_blog_meta() -> Iterator[MetaPost]:
    for filename in glob.glob('content/*.md'):
        content =  {'filename': filename}
        with open(filename) as f:
            for line in f:
                if len(line.strip()):
                    key, value = line.split(':', 1)
                    content[key.lower()] = value.strip()
                else:
                    break
        if 'tags' in content:
            content['tags'] = [tag.strip() for tag in content['tags'].split(',')]
        yield MetaPost(**content)

if __name__ == '__main__':
    app()
