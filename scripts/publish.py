#!/usr/bin/env python3
from __future__ import annotations
import re, shutil, sys, unicodedata
from datetime import date
from pathlib import Path

def slugify(value):
    value=unicodedata.normalize('NFKD',value).encode('ascii','ignore').decode('ascii').lower()
    return re.sub(r'[^a-z0-9]+','-',value).strip('-') or 'untitled'

def parse_frontmatter(text):
    if not text.startswith('---'): return {},text
    m=re.match(r'^---\s*\n(.*?)\n---\s*\n?(.*)$',text,re.S)
    if not m: return {},text
    data={}
    for line in m.group(1).splitlines():
        if ':' in line:
            k,v=line.split(':',1); data[k.strip()]=v.strip().strip('"').strip("'")
    return data,m.group(2)

def make_fm(data,title,dt=None,page=False):
    lines=['---',f'title: {data.get("title",title)}']
    if page: lines.append(f'permalink: {data.get("permalink", "/"+slugify(title)+"/")}')
    else: lines.append(f'date: {data.get("date",dt)}')
    for k in ('description','math','categories','tags'):
        if k in data: lines.append(f'{k}: {data[k]}')
    return '\n'.join(lines+['---'])

def find_asset(name,asset_root,note_dir):
    name=name.strip().strip('/')
    for c in (note_dir/name,asset_root/name,asset_root/Path(name).name):
        if c.is_file(): return c
    if asset_root.exists():
        ms=list(asset_root.rglob(Path(name).name));
        if ms: return ms[0]
    return None

def convert_images(body,note,writing,slug):
    asset_root=writing/'assets'; dest=Path('assets/images')/slug; dest.mkdir(parents=True,exist_ok=True)
    pat=re.compile(r'!\[\[([^\]|#]+)(?:\|[^\]]+)?\]\]')
    def sub(m):
        src=find_asset(m.group(1),asset_root,note.parent)
        if not src:
            print(f'WARNING: image not found: {m.group(1)}'); return m.group(0)
        target=dest/src.name; shutil.copy2(src,target)
        return f'![{src.stem}]({{{{ site.baseurl }}}}/assets/images/{slug}/{target.name})'
    return pat.sub(sub,body)

def convert_wikilinks(body):
    pat=re.compile(r'(?<!!)\[\[([^\]|#]+)(?:\|([^\]]+))?\]\]')
    def sub(m):
        target=m.group(1).strip(); label=(m.group(2) or target).strip()
        return f'[{label}]({{{{ site.baseurl }}}}/posts/{slugify(Path(target).stem)}/)'
    return pat.sub(sub,body)

def publish(writing):
    pub=writing/'3-published'
    if not pub.is_dir(): raise SystemExit(f'Could not find published folder: {pub}')
    posts=pages=0
    for src in sorted(pub.rglob('*.md')):
        meta,body=parse_frontmatter(src.read_text(encoding='utf-8'))
        title=meta.get('title',src.stem); typ=meta.get('type','post').lower(); slug=slugify(title)
        body=convert_wikilinks(convert_images(body,src,writing,slug))
        if typ=='page':
            permalink=meta.get('permalink',f'/{slug}/')
            out=Path(f'{slug}.md') if permalink in ('/about/','/bookshelf/') else Path(permalink.strip('/'))/'index.md'
            out.parent.mkdir(parents=True,exist_ok=True)
            out.write_text(make_fm(meta,title,page=True)+'\n\n'+body.lstrip()+'\n',encoding='utf-8')
            pages+=1; print(f'Published page: {src.relative_to(pub)} -> {out}')
        else:
            dt=meta.get('date',date.fromtimestamp(src.stat().st_mtime).isoformat()); out=Path('_posts')/f'{dt[:10]}-{slug}.md'
            out.write_text(make_fm(meta,title,dt)+'\n\n'+body.lstrip()+'\n',encoding='utf-8')
            posts+=1; print(f'Published post: {src.relative_to(pub)} -> {out}')
    print(f'\nDone. Published {posts} post(s) and {pages} page(s).')

if __name__=='__main__':
    if len(sys.argv)!=2: raise SystemExit("Usage: python3 scripts/publish.py '/path/to/vault/writing'")
    publish(Path(sys.argv[1]).expanduser().resolve())
