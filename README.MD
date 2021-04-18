# Description

Simple API for learning Python

bin/kafka-console-producer.sh --topic dashboard --bootstrap-server PLAINTEXT://127.0.0.1:9094

bin/kafka-console-consumer.sh --topic dashboard --from-beginning --bootstrap-server PLAINTEXT://127.0.0.1:9094

### Example message

```json
{ "url": "https://www.lambdatest.com", "html_element_id": "testing_form", "output_file": "element1.png" }
```
