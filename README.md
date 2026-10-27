# no-as-a-service-slack

Bot that gives you a reason to say no.

A Slack bot inspired by [No-as-a-Service](https://github.com/hotheadhacker/no-as-a-service).
Mention it in any channel it's been added to or send it a DM, and it replies with a random,
creative way to say no. Or type `/no` to preview a reason only you can see, then **Send** it
to the channel, **Shuffle** for another one, or **Cancel**, like `/giphy`.

```
you:  @No Bot can you cover my shift on Saturday?
bot:  In a different season of life, I might say yes—but not right now.
```

## Self-hosting

The bot is a small web server. Slack sends it events, and each workspace installs it
through OAuth, so its token is stored in a database (SQLite locally, Postgres in production).
It needs a public HTTPS URL, `https://<host>` below. For local development, use
[ngrok](https://ngrok.com/) with your free static domain:
`ngrok http --url=<your-domain> 3000`.

1. Create an app at [api.slack.com/apps](https://api.slack.com/apps) (**From scratch**).
2. Open **Basic Information** and copy the **Client ID**, **Client Secret** and
   **Signing Secret** into `.env`:

   ```sh
   cp env.example .env
   # then set SLACK_SIGNING_SECRET, SLACK_CLIENT_ID and SLACK_CLIENT_SECRET in .env
   ```

   `DATABASE_URL` defaults to a local SQLite file. In production, point it at Postgres:
   `postgresql+asyncpg://user:password@host/dbname`. The bot loads `.env` on startup if it
   exists. Variables set in the environment take precedence over the file.
3. Open **OAuth & Permissions**, add the redirect URL `https://<host>/slack/oauth_redirect`
   and the bot token scopes `app_mentions:read`, `chat:write`, `commands` and `im:history`
   (needed to read DMs).
4. Start the bot (see [Running](#running)). The next steps need it running, because Slack
   checks each Request URL by calling it.
5. Make sure **Socket Mode** is off. Then use `https://<host>/slack/events` as the Request URL in:
   - **Event Subscriptions**: enable events and subscribe to the `app_mention`, `message.im`,
     `app_uninstalled` and `tokens_revoked` bot events;
   - **Slash Commands**: create `/no`;
   - **Interactivity & Shortcuts**: turn **Interactivity** on (needed for the Send, Shuffle
     and Cancel buttons).
6. Open **App Home** and, under **Show Tabs**, enable the **Messages Tab** and check
   **Allow users to send Slash commands and messages from the messages tab**. Without it,
   users can't DM the bot.
7. Install the app by opening `https://<host>/slack/install` and clicking **Add to Slack**.
   Don't use **Install to Workspace** in the app settings. It shows a token there but doesn't
   store it in the bot's database. If you change scopes later, install again the same way.

To let anyone install the bot, open **Manage Distribution** and activate public
distribution, then share the `https://<host>/slack/install` link.

Invite the bot to a channel (`/invite @No Bot`) before mentioning it there.

## Running

Locally with [uv](https://docs.astral.sh/uv/):

```sh
uv sync
uv run python -m bot
```

The bot listens on port 3000, or on `PORT` if it's set. On first start, it creates its tables
in the database.

With Docker, use Postgres for `DATABASE_URL`, since a SQLite file inside the container is lost
when the container is removed:

```sh
docker build -t no-as-a-service-slack .
docker run --rm --env-file .env -p 3000:3000 no-as-a-service-slack
```

On Heroku, the included `Procfile` runs the bot as a `web` dyno. Set `SLACK_SIGNING_SECRET`,
`SLACK_CLIENT_ID`, `SLACK_CLIENT_SECRET` and `DATABASE_URL` in the app's config vars.

## Customizing

Reasons live in `bot/reasons.json`, a plain JSON array of strings. Edit it and restart the bot.

Listeners live in `bot/extensions/`, grouped by type (`actions/`, `commands/`, `events/`, `messages/`),
following the layout of the Slack CLI's Bolt templates. Each type is a package whose
`__init__.py` has a `register(app)` function that wires its callbacks to the app. Every
package there is registered on startup, so adding a new type (say, `views/`) needs no other
changes. New slash commands also have to be created under **Slash Commands** in the app
settings.

## Credits

Reasons come from [No-as-a-Service](https://github.com/hotheadhacker/no-as-a-service)
by hotheadhacker.

## License

[MIT](LICENSE)
