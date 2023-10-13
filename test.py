from wrapper import call_node

test_rich_text = {
    "data": {},
    "content": [
        {
            "data": {},
            "content": [
                {
                    "data": {},
                    "marks": [],
                    "value": "Level-Up your code with ",
                    "nodeType": "text",
                },
                {
                    "data": {},
                    "marks": [{"type": "bold"}],
                    "value": "Code Quest",
                    "nodeType": "text",
                },
                {"data": {}, "marks": [], "value": "!", "nodeType": "text"},
            ],
            "nodeType": "paragraph",
        }
    ],
    "nodeType": "document",
}

response = call_node(test_rich_text)
print(response)
