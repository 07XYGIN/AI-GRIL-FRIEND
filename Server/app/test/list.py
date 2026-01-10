arr = [{'type': 'human', 'data': {'content': '你好，我叫小明。', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': None}}, {'type': 'ai', 'data': {'content': '你好，小明！很高兴认识你～ 今天过得怎么样呀？ 🌟', 'additional_kwargs': {'refusal': None}, 'response_metadata': {'id': 'chatcmpl-db275e43-cf64-9a1d-be59-ef7db19daf60', 'logprobs': None, 'model_name': 'qwen-plus', 'token_usage': {'total_tokens': 44, 'prompt_tokens': 26, 'completion_tokens': 18, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 0}, 'completion_tokens_details': None}, 'finish_reason': 'stop', 'model_provider': 'openai', 'system_fingerprint': None}, 'type': 'ai', 'name': None, 'id': 'lc_run--019ba6ad-e2af-7983-a8d2-bbc8689be55c-0', 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 26, 'output_tokens': 18, 'total_tokens': 44, 'input_token_details': {'cache_read': 0}, 'output_token_details': {}}}}, {'type': 'human', 'data': {'content': '我刚才说我叫什么？', 'additional_kwargs': {}, 'response_metadata': {}, 'type': 'human', 'name': None, 'id': None}}, {'type': 'ai', 'data': {'content': '你刚才说你叫小明呀～ 要我再帮你记住一遍的话：你好，我是小明！ 😊（还特意加了波浪号让自己显得更友好些呢）', 'additional_kwargs': {'refusal': None}, 'response_metadata': {'id': 'chatcmpl-70cd5a0d-a79f-92da-872c-23529de1b0de', 'logprobs': None, 'model_name': 'qwen-plus', 'token_usage': {'total_tokens': 102, 'prompt_tokens': 60, 'completion_tokens': 42, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 0}, 'completion_tokens_details': None}, 'finish_reason': 'stop', 'model_provider': 'openai', 'system_fingerprint': None}, 'type': 'ai', 'name': None, 'id': 'lc_run--019ba6ad-ea19-71a3-bde0-527192eb7049-0', 'tool_calls': [], 'invalid_tool_calls': [], 'usage_metadata': {'input_tokens': 60, 'output_tokens': 42, 'total_tokens': 102, 'input_token_details': {'cache_read': 0}, 'output_token_details': {}}}}]

from rich.console import Console

console = Console()
arr1 = []

obj = {
    "ai": [],
    "human": []
}




