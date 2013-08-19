#!/usr/bin/env python

logdata = [line.strip() for line in open("policy.log", 'r')]

ruleset = {}

for line in logdata:
    if line not in ruleset:
        ruleset[line] = 0
    ruleset[line] += 1

print "Source        Dest          Port  Protocol  Hits"
for policy in sorted(ruleset, key=ruleset.get, reverse=True):
    print policy, ruleset[policy]
