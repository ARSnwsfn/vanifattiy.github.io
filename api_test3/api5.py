import requests

payload = {
  "content": "string1",
  "user_id": "string2",
  "task_id": "string3",
  "is_done": False
}
payload_put = {
  "content": "string7",
  "user_id": "string5",
  "task_id": "string4",
  "is_done": True
}
url="https://todo.pixegami.io/"
path="delete-task/"
path1="get-task/"

def create_task(payload):
    return requests.put("https://todo.pixegami.io/"+"create-task/", json=payload)

task_id=create_task(payload).json()["task"]["task_id"]

def get_task(task_id):
    return requests.get(url+path1+task_id)
def delete_task(path):
    return requests.delete("https://todo.pixegami.io/"+path)
def put_task(payload_put):
    return requests.put("https://todo.pixegami.io/"+"update-task", json=payload_put)

def test_create():
    assert create_task(payload).status_code==200
    assert len(task_id)==37
    assert isinstance(create_task(payload).text, str)

def test_get():
    assert get_task(task_id).status_code==200
    assert (isinstance(get_task(task_id).text, str))
    assert get_task(task_id).text.count('id') == 2
    assert get_task(task_id).json()["is_done"] == False
    assert get_task(task_id).encoding == 'utf-8'
    assert get_task(task_id).headers["Content-Type"] == "application/json"
    assert get_task(task_id).url == f"https://todo.pixegami.io/get-task/{task_id}"

def test_put():
    assert create_task(payload).json()['task']['user_id'] == 'string2'
    assert put_task(payload_put).json()["updated_task_id"] == "string4"
    assert get_task(task_id).json()["task_id"] == task_id
    # assert requests.get("https://todo.pixegami.io/"+"get-task/"+task_id).json()["is_done"] == True
def test_delete():
    assert create_task(payload).status_code==200
    assert delete_task(path+task_id).status_code==200
    assert get_task(task_id).status_code==404
#
