# TG distilled data dictionary

## Prelude

Unless specified, the field is directly sourced from Telegram.
Non-boolean fields may be `NULL` if the message package doesn't contain that data. Boolean fields will only be 1 or 0.
All messages present in the distilled dataset were produced by users or bots. System messages and similar were purged.
Posts are messages that are are one-to-many (from channel administrators to users) and are exclusive to broadcast channels.
A forward is an immutable copy-paste of another message.
A reply is a forward that must include new elements (text, media, etc.). Unlike a forward, a reply only shows a short snippet, which may be cropped if too long, of the original message.
Forwards will not reveal the chat they come from, but replies will. However, this is not extracted due to a conflict: Telegram states that the type and ID of these chats will be revealed if the user (the scraper) is not a member.
Both forwards and replies reveal the user or chat which sent the message being forwarded or replied to (see the `chain_from_id` column).
Messages may be sent by channels or users.
Message senders may have more than one identifier associated with them:

* Type and ID: Defined by Telegram and unique to each chat and user. See the `from_id` and `chain_from_id` columns.
* Post author signature: Optional setting which allows broadcast channel administrators to add a signature to their posts. If signatures were not set up, it would be impossible tell which administrator sent which post. See the `post_author` and `chain_post_author` columns.
* Name: Optional setting which allows a Telegram account to hide any account information under a user-defined name whenever their messages are forwarded or replied to. See the `chain_from_name` column.

### message_id | INTEGER

A message's index; 1-based, relative to other messages in the same chat, and determined by the sending order.
If a message is deleted, its corresponding ID gets deleted without replacement.

### content | TEXT

The text resulting from concatenating the text in:

1. `"message"` (the main text).
2. `"media"` (text related to attachments).
3. `"reply_markup"` (text related to buttons and reply interfaces).

**If in English, `content` was normalized by attempting to map non-ASCII characters to ASCII characters (å to a) with the `unidecode` library, lowercasing, expanding contractions with the `contractions` library, and removing unnecessary whitespaces.**
`content` does not include the text in the `"quote"` field of `"MessageReplyHeader"` objects, as this text may be very long in the package, but in practice users can only see a limited number of `"quote"` characters in the Telegram interface. Moreover, trying to extract the exact character window of `"quote"` text available to the users may be counterproductive, as cropped documents may add confusing context.
If `content` is `NULL`, the message exclusively consisted of `"media"` (attachments) or similar (polls, etc.).

### language | TEXT

The ISO 639-1 language code associated with the `content`, as determined by the `langdetect` library.
If `content` is `NULL`, `language` will be `NULL`, and if `langdetect` couldn't determine a language, `language` will be `"?"`.

### from_id | TEXT

The sender's type and ID.
If `NULL`, the sender is a channel administrator.

### post_author | TEXT

A post is a broadcast message exclusive to broadcast channels.
 `post_author` is a string identifying the channel administrator who created the post.
May be `NULL` even if the message is a broadcast.

### edit_hide | BOOLEAN

If `True`, edit times will not be shown.

### noforwards | BOOLEAN

If `True`, the message can't be forwarded.

### scheduled | BOOLEAN

If `True`, the delivery of the message was scheduled.

### pinned | BOOLEAN

If `True`, the message is pinned.

### views | INTEGER

The number of views.

### forwards | INTEGER

The number of forwards.

### replies | INTEGER

The number of replies.
If `NULL`, the message is not one that can can be replied to.

### date | TEXT

The time and date of sending.

### edit_date | TEXT

The time and date of editing.

### ttl | INTEGER

Time-to-live (time before the message self-destructs).

### forward | BOOLEAN

If `True`, the message is a forward of another message, which could be imported from a different platform (not Telegram).

### reply | BOOLEAN

If `True`, the message is a reply to another message, which could be imported from a different platform (not Telegram).

### reply_source | TEXT

The chat that contains the message being replied to.

### reply_scheduled | BOOLEAN

If `True`, the message is a reply to a message whose delivery was scheduled.

### chain_from_id | TEXT

The type and ID of the sender of the message being forwarded or replied to.
If `NULL`, the source messages' sender is a channel administrator.

### chain_from_name | TEXT

The name (masking any account information) of the sender of the message being forwarded or replied to.

### chain_post_author | TEXT

A post is a broadcast message exclusive to broadcast channels.
 `chain_post_author`, is a string identifying the channel administrator who created the the source post (the one forwarded from or replied to).
May be `NULL` even if the source message is a broadcast.

### chain_imported | BOOLEAN

If `True`, the source message (the one forwarded from or replied to) was imported from a different platform (not Telegram).

### chain_date | TEXT

The time and date the source message (the one forwarded from or replied to) was sent.

### invoice | TEXT

In Telegram, messages may carry payment interfaces (users may ask for donations or sell services).
If not `NULL`, this field indicates the price and currency being asked for. XTR means Telegram Stars.

### media_price | INTEGER

In Telegram, messages may carry paid media attachments, which are shown as blurry snippets and may be unlocked by paying a fee in the Telegram Stars currency to the sender of the message.
If not `NULL`, this field indicates the price for a paid media attachment on the message.

### contact | TEXT

A JSON document with contact details provided on the message:

* `phone`: Phone number.
* `first_name`: First name.
* `last_name`: Last name.
* `vcard`: A JSON document of a vCard.
* `user_id`: User ID.

Not all fields may be present.

### location | TEXT

A JSON document with location details provided on the message:

* `long`: Longitude.
* `lat`: Latitude.
* `accuracy_radius`: Accuracy radius.
* `period`: For live location sharing, the validity period of the geolication object on Telegram.
* `notification_radius`: For live location sharing, the distance (in meters) to another chat member for proximity alerts.
* `title`: The name of a venue.
* `address`: The address of a venue.
* `venue_type`: The type of venue, as determined by a venue provider (like Google Places).

Not all fields may be present.

### web_preview | BOOLEAN

If `True`, the message contains a webpage snippet.

### story | BOOLEAN

If `True`, the message contains a Telegram story.

### photo | BOOLEAN

If `True`, the message contains a photo.

### video | BOOLEAN

If `True`, the message contains a video.

### round | BOOLEAN

If `True`, the message contains a round video (a video with a circle mask).
In Telegram, round videos are associated with phone recordings (indicating potentially authentic content), but may be faked (there are ways to send other videos as round videos).

### voice | BOOLEAN

If `True`, the message contains a voice message.

### other_media | BOOLEAN

If `True`, the message contains a document (may be a video, pdf, gif, etc.).

### media_ttl | INTEGER

Media time-to-live (time before the attachment self-destructs).

### buttons | BOOLEAN

If `True`, the message contains a reply interface with buttons.

### emails | TEXT

The set of emails in the message.

### phones | TEXT

The set of phone numbers in the message.

### hashtags | TEXT

The set of hashtags in the message.

### cashtags | TEXT

The set of cashtags in the message (to be used in CashApp, like $spongebob).
It's unclear if non-US cashtags are recognized by Telegram (like £spongebob).

### cards | TEXT

The set of credit card numbers in the message.

### urls | TEXT

The unique URLs in `content`, prior to any normalization, as determined by the `urlextract` library.
Due to encoding and offset inconsistencies, these were not directly extracted using Telegram's message entities data.

### cleaner_urls | TEXT

Deduplicated, normalized `urls`, with lowercased domains.

### domains | TEXT

The unique fully-qualified domain names (FQDNs) in `urls`, as determined by the `tldextract` library.
**Normalized by lowercasing.**

### identifiers | TEXT

The unique identifiers (usernames, invite codes, folder codes, type and ids, etc.) in `content`, prior to any normalization and as determined by `re` patterns.
**Usernames were normalized by lowercasing.**
Due to encoding and offset inconsistencies, these were not directly extracted using Telegram's message entities data.

### restriction_reasons | TEXT

The list of reasons that restrict the content from displaying in the Telegram app.

### political | BOOLEAN

If `True`, the message was classified as political, using a classification process as described in www.nature.com/articles/s44260-025-00056-w.
This applies only to messages in English and Russian.

### toxicity | REAL

A 0-1 score acquired from the Perspective API. Here, toxicity is defined as "A rude, disrespectful, or unreasonable comment that is likely to make people leave a discussion."
This applies only to messages in English.

### severe_toxicity | REAL

A 0-1 score acquired from the Perspective API. Here, severe toxicity is defined as "A very hateful, aggressive, disrespectful comment or otherwise very likely to make a user leave a discussion or give up on sharing their perspective. This attribute is much less sensitive to more mild forms of toxicity, such as comments that include positive uses of curse words."
This applies only to messages in English.

### identity_attack | REAL

A 0-1 score acquired from the Perspective API. Here, an identity attack is defined as "Negative or hateful comments targeting someone because of their identity."
This applies only to messages in English.

### insult | REAL

A 0-1 score acquired from the Perspective API. Here, an insult is defined as "Insulting, inflammatory, or negative comment towards a person or a group of people."
This applies only to messages in English.

### profanity | REAL

A 0-1 score acquired from the Perspective API. Here, a profanity is defined as "Swear words, curse words, or other obscene or profane language."
This applies only to messages in English.

### threat | REAL

A 0-1 score acquired from the Perspective API. Here, a threat is defined as "Describes an intention to inflict pain, injury, or violence against an individual or group."
This applies only to messages in English.
