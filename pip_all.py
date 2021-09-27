import pip
import sys, os
from subprocess import check_call

for p in os.listdir('D:\letcode\IdeaProjects'):
    os.chdir('D:\letcode\IdeaProjects\\'+p)
    check_call('git pull')

