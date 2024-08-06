# clickstream
Clickstream API


### Examples


POST new event

```bash
curl --request POST \
  --url http://127.0.0.1:8000/collect/ \
  --header 'Content-Type: application/json' \
  --data '{
    "user_id": "user123",
    "page_url": "http://example.com/page",
    "referrer_url": "http://example.com/referrer",
    "user_agent": "Mozilla/5.0",
    "event_type": "click",
    "object_id": "button123",
    "details": {"additional_info": "some details"}
}'
```

GET all events

```bash
curl --request GET \
  --url http://127.0.0.1:8000/clicks/
```
