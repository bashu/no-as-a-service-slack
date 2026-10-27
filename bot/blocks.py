import json

SEND_ACTION_ID = "no_send"
SHUFFLE_ACTION_ID = "no_shuffle"
CANCEL_ACTION_ID = "no_cancel"


def preview(reason: str, response_url: str) -> list[dict]:
    """A private preview of a reason with Send, Shuffle and Cancel buttons, like /giphy.

    The buttons carry the /no command's response_url: Slack only posts to the channel through
    that one, not through the response_url of a click on this private preview.
    """
    return [
        {"type": "section", "text": {"type": "mrkdwn", "text": reason}},
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "action_id": SEND_ACTION_ID,
                    "text": {"type": "plain_text", "text": "Send"},
                    "style": "primary",
                    "value": json.dumps(
                        {"reason": reason, "response_url": response_url}
                    ),
                },
                {
                    "type": "button",
                    "action_id": SHUFFLE_ACTION_ID,
                    "text": {"type": "plain_text", "text": "Shuffle"},
                    "value": response_url,
                },
                {
                    "type": "button",
                    "action_id": CANCEL_ACTION_ID,
                    "text": {"type": "plain_text", "text": "Cancel"},
                },
            ],
        },
    ]


def sent(reason: str, user_id: str) -> list[dict]:
    """A reason posted to the channel, crediting who sent it since it's posted as the app."""
    return [
        {"type": "section", "text": {"type": "mrkdwn", "text": reason}},
        {
            "type": "context",
            "elements": [{"type": "mrkdwn", "text": f"Sent by <@{user_id}> with /no"}],
        },
    ]
