# def greet(name: str, age: int) -> str :
#     return f"Hello, {name} {age}"
# abc = greet("Hamza", 22)
# print (abc)

# studentDetails = {
#     "Name": "Hamza",
#     "Age": 21,
#     "Roll No": 123
# }

# print(f"""
#       Name = {studentDetails['Name']}
#       Age = {studentDetails['Age']}
#       Roll No = {studentDetails['Roll No']}
# """)


def llm (prompt: str):
    return {
        "content": "Hello, How can I help you",
        "role": "assistant"

    }
response_dict = llm(prompt="Hi")

print(response_dict["content"])
