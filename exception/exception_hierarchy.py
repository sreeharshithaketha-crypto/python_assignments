try:
    raise ValueError("example")
except Exception as e:
    print(type(e).__name__)
