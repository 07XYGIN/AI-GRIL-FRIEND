frontend_messages = []
def get_ai_response(arr:list):
    for i in arr:
        frontend_messages.append({
            "role": i["type"],
            "content": i["data"]["content"]
        })
    return frontend_messages