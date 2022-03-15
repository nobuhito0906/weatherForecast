def create_single_text_message(message):
    if message == 'やあ':
        message = 'なんすか'
    test_message = [
        {
            'type': 'text',
            'text': message
        }
    ]
    return test_message