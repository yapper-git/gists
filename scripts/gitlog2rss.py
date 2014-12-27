#!/usr/bin/env python
#
# @name gitlog2rss.py
# @author yvand
# @see
#   * http://git-scm.com/book/fr/v2/Customizing-Git-Git-Hooks
#   * http://blog.lost-theory.org/post/how-to-parse-git-log-output/
#   * http://opensource.apple.com/source/Git/Git-19/src/git-htmldocs/pretty-formats.txt

"""
RSS feed generator to follow git workflow (using git log)
"""

import argparse
from datetime import datetime
from jinja2 import Template
import gitlog2rss # for __doc__
import os # for chdir, getcwd, path.basename
import re
from subprocess import Popen, PIPE
import sys

parser = argparse.ArgumentParser(description=gitlog2rss.__doc__)
parser.add_argument("repository", help="path to GIT repository")
parser.add_argument("link", help="URL of the RSS feed")
parser.add_argument("target", help="path to RSS output file (or stdout if missing)", nargs='?', default='-')
args = parser.parse_args()

pwd = os.getcwd()

try:
    os.chdir(args.repository)
except FileNotFoundError as e:
    print(str(e), file=sys.stderr)
    sys.exit(1)

GIT_LIMIT = 10
GIT_COMMIT_FIELDS = ['id', 'author_name', 'author_email', 'date', 'subject', 'body']
GIT_LOG_FORMAT = ['%H', '%an', '%ae', '%ad', '%s', '%B']

DATETIME_RSS = '%a, %d %b %Y %H:%M:%S +0100' # or import email.utils

# git log -n --format="%H %s..."
GIT_LOG_FORMAT = '%x1f'.join(GIT_LOG_FORMAT) + '%x1e'
p = Popen('git log -n %s --format="%s"' % (GIT_LIMIT, GIT_LOG_FORMAT), shell=True, stdout=PIPE)
(log, _) = p.communicate()
if p.returncode != 0:
    sys.exit(2)
log = log.decode('utf-8').strip('\n\x1e').split('\x1e')
log = [row.strip().split("\x1f") for row in log]
log = [dict(zip(GIT_COMMIT_FIELDS, row)) for row in log]

# 'Fri Dec 26 22:13:36 2014 +0100' → 'Fri, 26 Dec 2014 22:13:36 +0100'
pattern = re.compile(r'^(\w+) (\w+) (\d+) (\d{2}:\d{2}:\d{2}) (\d{4}) (.+)$')
for commit in log:
    commit['date'] = pattern.sub(r'\1, \3 \2 \5 \4 \6', commit['date'])

repository = os.path.basename(args.repository)

tmpl = Template('''\
<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{{ title }}</title>
    <link>{{ link }}</link>
    <atom:link href="{{ link }}" rel="self" type="application/rss+xml" />
    <description>{{ description }}</description>
    <lastBuildDate>{{ last_build_date }}</lastBuildDate>
    <ttl>{{ ttl }}</ttl>
    {%- for item in item_list %}
    <item>
      <title>{{ item.subject }}</title>
      <description>{{ item.body }}</description>
      <guid isPermaLink="false">{{ item.id }}</guid>
      <pubDate>{{ item.date }}</pubDate>
      <author>{{ item.author_email }} ({{ item.author_name }})</author>
    </item>
    {%- endfor %}
  </channel>
</rss>
''')

tmpl_render = tmpl.render(
    title=repository,
    description='RSS feed to follow the workflow of %s repository' % repository,
    link=args.link,
    last_build_date=datetime.now().strftime(DATETIME_RSS),
    ttl=60,
    item_list=log
)

if args.target == '-':
    print(tmpl_render)
else:
    os.chdir(pwd)
    with open(args.target, 'w') as output_file:
        output_file.write(tmpl_render)

