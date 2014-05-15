from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def event_choices(events):
    """ Get the possible events from settings """
    if events is None:
        msg = "Please add some events in settings.WEBHOOK_EVENTS."
        raise ImproperlyConfigured(msg)
    try:
        choices = [(x, x) for x in events]
    except TypeError:
        """ Not a valid iterator, so we raise an exception """
        msg = "settings.WEBHOOK_EVENTS must be an iterable object."
        raise ImproperlyConfigured(msg)

    return choices


WEBHOOKS_SENDER = getattr(settings, "WEBHOOKS_SENDER", "djwebhooks.senders")
WEBHOOK_OWNER_FIELD = getattr(settings, "WEBHOOK_OWNER_FIELD", "username")
WEBHOOK_ATTEMPTS = getattr(settings, "WEBHOOK_EVENTS", (0, 15, 30, 60))
WEBHOOK_EVENTS = getattr(settings, "WEBHOOK_EVENTS", None)
WEBHOOK_EVENTS_CHOICES = event_choices(WEBHOOK_EVENTS)

