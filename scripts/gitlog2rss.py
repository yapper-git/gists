#!/usr/bin/env python
#
# @name gitlog2rss.py
# @author yvand
# @see
#   * http://git-scm.com/book/fr/v2/Customizing-Git-Git-Hooks
#   * http://blog.lost-theory.org/post/how-to-parse-git-log-output/
#   * http://opensource.apple.com/source/Git/Git-19/src/git-htmldocs/pretty-formats.txt
#   * http://www.rssboard.org/rss-profile#data-types-characterdata (escape &, < and >)

"""
RSS feed generator to follow git workflow (using git log)
"""

import argparse
from datetime import datetime
from jinja2 import Template
import os  # for chdir, getcwd, path.basename
import re
from subprocess import Popen, PIPE
import sys


def escape(string):
    return string.replace('&', '&#x26;').replace('<', '&#x3C;').replace('>', '&#x3E;')


def newline_to_br(string):
    return string.replace('\n', '<br/>')


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("repository",    help="path to GIT repository")
parser.add_argument("link",          help="URL of the RSS feed")
parser.add_argument("target",        help="path to RSS output file. Default: stdout.", nargs='?', default='-')
parser.add_argument("-n", "--limit", help="number of commits to print. Default: 10", default=10)
parser.add_argument("-r", "--reponame",
                    help="name of the GIT repository. Default: the basename of the repository's path")
parser.add_argument("-t", "--ttl",   help="Time to Live of the output RSS. Default: 60", default=60)
parser.add_argument("-v", "--verbose", action='count')
args = parser.parse_args()

pwd = os.getcwd()

try:
    os.chdir(args.repository)
except FileNotFoundError as e:
    print(str(e), file=sys.stderr)
    sys.exit(1)

DATETIME_RSS = '%a, %d %b %Y %H:%M:%S +0100'  # or import email.utils

GIT_LIMIT = args.limit
GIT_COMMIT_FIELDS = ['id', 'author_name', 'author_email', 'date', 'subject', 'body', 'statdiff']
GIT_LOG_FORMAT = ['%H', '%an', '%ae', '%ad', '%s', '%B']
GIT_LOG_FORMAT = '%x1e' + '%x1f'.join(GIT_LOG_FORMAT) + '%x1f'

if args.verbose is None:
    GIT_OPTIONS = ''
elif args.verbose == 1:
    GIT_OPTIONS = '--stat'
elif args.verbose == 2:
    GIT_OPTIONS = '-p'
else:
    GIT_OPTIONS = '--stat -p'


p = Popen('git log -n {} --format="{}" {}'.format(
    GIT_LIMIT,
    GIT_LOG_FORMAT,
    GIT_OPTIONS), shell=True, stdout=PIPE)
(log, _) = p.communicate()
if p.returncode != 0:
    sys.exit(2)
log = log.decode('utf-8').strip('\n\x1e').split('\x1e')
log = [row.strip().split("\x1f") for row in log]
log = [dict(zip(GIT_COMMIT_FIELDS, row)) for row in log]

pattern = re.compile(r'^(\w+) (\w+) (\d+) (\d{2}:\d{2}:\d{2}) (\d{4}) (.+)$')
for commit in log:
    # 'Fri Dec 26 22:13:36 2014 +0100' → 'Fri, 26 Dec 2014 22:13:36 +0100'
    commit['date'] = pattern.sub(r'\1, \3 \2 \5 \4 \6', commit['date'])

    # Escape XML special characters (except quotes)
    commit['author_name'] = escape(commit['author_name'])
    commit['author_email'] = escape(commit['author_email'])
    commit['subject'] = escape(commit['subject'])
    commit['body'] = newline_to_br(escape(commit['body']))
    if args.verbose is not None:
        commit['statdiff'] = escape(commit['statdiff'])

repository = args.reponame if args.reponame is not None else os.path.basename(os.path.realpath(args.repository))

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
      {%- if verbose %}
      <description><![CDATA[
        {{ item.body }}
        <pre>{{ item.statdiff }}</pre>
        ]]></description>
      {%- else %}
      <description><![CDATA[{{ item.body }}]]></description>
      {%- endif %}
      <guid isPermaLink="false">{{ item.id }}</guid>
      <pubDate>{{ item.date }}</pubDate>
      <author>{{ item.author_email }} ({{ item.author_name }})</author>
    </item>
    {%- endfor %}
  </channel>
</rss>
''')

tmpl_render = tmpl.render(
    verbose=args.verbose is not None,
    title=repository,
    description='RSS feed to follow the workflow of %s repository' % repository,
    link=args.link,
    last_build_date=datetime.now().strftime(DATETIME_RSS),
    ttl=args.ttl,
    item_list=log
)

if args.target == '-':
    print(tmpl_render)
else:
    os.chdir(pwd)
    with open(args.target, 'w') as output_file:
        output_file.write(tmpl_render)
