from contentful_rich_text_to_markdown_converter import convert_rich_text_to_markdown

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

response = convert_rich_text_to_markdown(test_rich_text)
print(response)
