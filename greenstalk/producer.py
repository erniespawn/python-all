import greenstalk

with greenstalk.Client(('127.0.0.1', 11300)) as client:
    client.put('hello')
