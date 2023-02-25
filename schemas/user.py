from voluptuous import Schema

register_single_user = Schema(
    {
        'id': int,
        'token': str
    }
)

create_single_user = Schema(
    {
        'name': str,
        'job': str,
        'id': str,
        'createdAt': str
    }
)

update_single_user = Schema(
    {
        'name': str,
        'job': str,
        'updatedAt': str,
    }
)
