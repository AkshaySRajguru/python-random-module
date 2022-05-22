import random
import uuid
import string

def generate_unique_id():
    return 'PTR-' + str(uuid.uuid4().hex[:8])

print(generate_unique_id()) # PTR-05592619

def generate_client_secret():
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(32))

print(generate_client_secret()) # V6YRZUYGLRJNM5W9FJ1XGA5CZVS6AA61

