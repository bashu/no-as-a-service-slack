# no-as-a-service-slack

Bot that gives you a reason to say no.

A Slack bot inspired by [No-as-a-Service](https://github.com/hotheadhacker/no-as-a-service).
Mention it in any channel it's been added to, send it a DM, or use the `/no` slash command,
and it replies with a random, creative way to say no.

```
you:  @No Bot can you cover my shift on Saturday?
bot:  In a different season of life, I might say yes—but not right now.
```

## Self-hosting

1. Create an app at [api.slack.com/apps](https://api.slack.com/apps) (**From scratch**).
2. Open **Socket Mode** and enable it. When prompted, create an app-level token with the
   `connections:write` scope and copy it (`xapp-...`).
3. Open **OAuth & Permissions** and add the bot token scopes `app_mentions:read`,
   `chat:write`, `commands` and `im:history` (needed to read DMs).
4. Open **Slash Commands** and create `/no`.
5. Open **Event Subscriptions**, enable events and subscribe to the `app_mention` and
   `message.im` bot events.
6. Open **App Home** and, under **Show Tabs**, enable the **Messages Tab** and check
   **Allow users to send Slash commands and messages from the messages tab**. Without it,
   users can't DM the bot.
7. Install the app to your workspace and copy the **Bot User OAuth Token** (`xoxb-...`).
   If you change scopes later, reinstall the app or the change won't apply.
8. Put both tokens in `.env`, or set them as environment variables:

   ```sh
   cp env.example .env
   # then set SLACK_BOT_TOKEN=xoxb-... and SLACK_APP_TOKEN=xapp-... in .env
   ```

   The bot loads `.env` on startup if it exists. Variables set in the environment take
   precedence over the file.

Invite the bot to a channel (`/invite @No Bot`) before mentioning it there.

## Running

Locally with [uv](https://docs.astral.sh/uv/):

```sh
uv sync
uv run python -m bot
```

The bot connects over Socket Mode, so it needs no public URL.

With Docker:

```sh
docker build -t no-as-a-service-slack .
docker run --rm --env-file .env no-as-a-service-slack
```

On Heroku, the included `Procfile` runs the bot as a `worker` dyno. Set `SLACK_BOT_TOKEN`
and `SLACK_APP_TOKEN` in the app's config vars and scale the worker to one.

## Customizing

Reasons live in `bot/reasons.json`, a plain JSON array of strings. Edit it and restart the bot.

Listeners live in `bot/extensions/`, grouped by type (`commands/`, `events/`, `messages/`),
following the layout of the Slack CLI's Bolt templates. Each type is a package whose
`__init__.py` has a `register(app)` function that wires its callbacks to the app. Every
package there is registered on startup, so adding a new type (say, `actions/`) needs no other
changes. New slash commands also have to be created under **Slash Commands** in the app
settings.

## Credits

Reasons come from [No-as-a-Service](https://github.com/hotheadhacker/no-as-a-service)
by hotheadhacker.

## License

[MIT](LICENSE)
