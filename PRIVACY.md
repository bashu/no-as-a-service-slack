# Privacy Policy

_Last updated: October 27, 2026_

This policy covers the NO! Slack app ("the app"), the open-source
[no-as-a-service-slack](https://github.com/bashu/no-as-a-service-slack) bot installed from
`https://no-as-a-service-slack.duckdns.org/slack/install`. If you run your own copy of the bot,
you are responsible for your own installation and this policy doesn't apply to it.

## What the app does

The app replies to `/no`, to mentions and to direct messages with a random reason to say no,
picked from a fixed list. It doesn't read, analyze or keep the content of your messages.

## What we store

When a workspace installs the app, Slack gives it access credentials for that workspace. We
store them in a database so the app can reply there:

- the workspace's ID and name (and the Enterprise Grid organization's, if any);
- the app's bot token, bot ID, bot user ID and granted scopes;
- the ID of the user who installed the app, and when it was installed.

During installation we also briefly store a random one-time value that protects the install
from forgery. It's only valid for 10 minutes.

## What we don't store

- **Message content.** Messages sent to the app, or containing a mention of it, are processed
  in memory only to send a reply, then discarded.
- **User data.** We don't collect names, emails, profiles or files, and we don't request
  permissions to read them.
- **Channel history.** The app can't read channels. It only receives messages that mention it
  and direct messages sent to it.

Server logs record technical details of each request (time, path, response status) for
troubleshooting, and are rotated regularly.

## How data is used and shared

Stored credentials are used only to send the app's replies through Slack's API. We don't sell,
rent or share any data with third parties, and we don't use it for analytics or advertising.

## Where data is kept

Data is stored on a server operated by the app's maintainer, in a database that isn't publicly
accessible. All traffic between Slack and the app is encrypted with HTTPS.

## Deleting your data

Uninstall the app from your workspace (**Tools → Apps → NO! → Configuration → Remove App**).
Slack notifies the app, which immediately deletes everything stored for that workspace. You can
also ask for deletion through the contact below.

## Changes

If this policy changes, the updated version will be published here with a new date.

## Contact

Questions about privacy: open an issue at
[github.com/bashu/no-as-a-service-slack/issues](https://github.com/bashu/no-as-a-service-slack/issues).
