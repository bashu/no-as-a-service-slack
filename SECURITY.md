# Security Policy

## Supported versions

Security fixes go into the `main` branch and are deployed to the hosted NO! app at
`https://no-as-a-service-slack.duckdns.org`. Older commits aren't supported. If you run your
own copy, update to the latest `main`.

## Reporting a vulnerability

Please report security issues privately. **Don't open a public GitHub issue.**

- Email [basil.shubin@gmail.com](mailto:basil.shubin@gmail.com) with "Security" in the
  subject, or
- use GitHub's [private vulnerability reporting](https://github.com/bashu/no-as-a-service-slack/security/advisories/new).

Include what you found, how to reproduce it, and what an attacker could do with it. Don't
include real Slack tokens or other people's data. If you need to show access, show that it's
possible without using it.

## What to expect

- An acknowledgment within 7 days.
- An assessment and, if the issue is confirmed, a fix plan within 30 days. Critical issues,
  such as exposure of stored workspace tokens, are fixed as soon as possible.
- Credit in the fix's release notes, if you'd like it.

This is a free project maintained by one person in their spare time, so there's no bug bounty.

## Scope

In scope:

- the hosted app's endpoints: `/slack/events`, `/slack/install` and `/slack/oauth_redirect`;
- the source code in this repository, including how it verifies Slack's requests, handles
  OAuth and stores workspace tokens.

Out of scope:

- Slack itself (report those to [Slack](https://hackerone.com/slack));
- the hosting provider, DNS and certificate services (DigitalOcean, DuckDNS, Let's Encrypt);
- denial-of-service or load testing, spam, and social engineering.

## Testing safely

Test only against a workspace you own, and stop as soon as you've confirmed an issue. Don't
access, change or delete other workspaces' data, and don't degrade the service for others.
Good-faith research that follows these rules won't be pursued legally.
