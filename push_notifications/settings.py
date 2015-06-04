from django.conf import settings

PUSH_NOTIFICATIONS_SETTINGS = getattr(settings, "PUSH_NOTIFICATIONS_SETTINGS", {})


# GCM
default_item = {
    "GCM_POST_URL" : "https://android.googleapis.com/gcm/send",
    "GCM_MAX_RECIPIENTS" : 1000,
    "APNS_PORT" : 2195,
    "APNS_FEEDBACK_PORT" : 2196,
    "APNS_ERROR_TIMEOUT" : None,
    "APNS_MAX_NOTIFICATION_SIZE" : 2048,

}

if settings.DEBUG:
    default_item["APNS_HOST"] = "gateway.sandbox.push.apple.com"
    default_item["APNS_FEEDBACK_HOST"] = "feedback.sandbox.push.apple.com"
else:
    default_item["APNS_HOST"] = "gateway.push.apple.com"
    default_item["APNS_FEEDBACK_HOST"] = "feedback.push.apple.com"

for s in PUSH_NOTIFICATIONS_SETTINGS.keys():
    for df in default_item.keys():
        PUSH_NOTIFICATIONS_SETTINGS[s].setdefault(df,default_item[df])
