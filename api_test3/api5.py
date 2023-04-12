import requests
import json
payload = {
  "content": "string1",
  "user_id": "string2",
  "task_id": "string3",
  "is_done": False
}
url="https://todo.pixegami.io/"
path1="get-task/"
path="delete-task/"
def create_task(payload):
    return requests.put("https://todo.pixegami.io/"+"create-task/", json=payload)
# print(create_task(payload).json()["task"]["task_id"])
task_id=create_task(payload).json()["task"]["task_id"]
def get_task(task_id):
    return requests.get(f"{url}{path1}{task_id}")
def delete_task(path):
    return requests.delete("https://todo.pixegami.io/"+path)

# def test_create():
#     assert create_task(payload).status_code==200
print(requests.get("https://todo.pixegami.io/get-task/").json())
# def test_get():
#     assert get_task(task_id).status_code==200
#     assert (isinstance(get_task(None).text, str))
#     assert get_task(None).text.count('task') == 100
#     assert get_task(None).encoding == 'utf-8'
#     assert get_task(None).headers["Content-Type"] == "application/json; charset=utf-8"
#     assert get_task(None).url == "https://todo.pixegami.io/get-task/"
# def test_delete():
#     assert create_task(payload).status_code==200
#     assert delete_task(path+task_id).status_code==200
#     assert get_task(task_id).status_code==404

