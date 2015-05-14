#!/usr/bin/env python
# -*- coding: utf-8 -*-
#repo_info.py

from github import Github
import getpass
import time

#input own account info
gusername = raw_input("Github_ID>")
gpassword = getpass.getpass()

g = Github(gusername,gpassword)

#show repositoory from repository fullname
repo_name = raw_input("Repository_Name>")

#take repository info
repo = g.get_repo(repo_name)

f = open('repo_comments','a')
start_time = time.clock()
revision = repo.get_commits()
n=0
for rev in revision:
    rev_sha = rev.sha
    cmt = repo.get_commit(rev_sha)
    commit_comment = cmt.commit.message.encode('utf_8')
    f.write(commit_comment)
    print n
    n=n+1
print "Owner:",
print repo.owner.name
print "Repositoty ID:",
print repo.id
end_time = time.clock()
print "time = %f" %(end_time-start_time)
f.close()
