import kopf

@kopf.on.create('example.com', 'v1', 'helloworlds')
def hello_world(spec, **kwargs):
    message = spec.get('message', 'No message')
    print(f"Hello World! Message: {message}")