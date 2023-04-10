import requests

my_site="https://jsonplaceholder.typicode.com/"
my_img = "https://iheartcraftythings.com/wp-content/uploads/2021/04/Computer-DRAWING-%E2%80%93-STEP-10.jpg"
my_img2 = "https://johnlewis.scene7.com/is/image/JohnLewis/desktop-carousel4-280922"
my_obj = {'Content-Length': '16'}
get_post_url="posts"
put_delete_url="/post/1"
class Test:
    def test_api_get(self):
        # def get_response(self,get, add_url)
        #     return requests.get(f"{my_site}{add_url}")
        get_response=requests.get(f"{my_site}{get_post_url}")

        if get_response.status_code != 200:
            raise Exception("Failed:\n Check again")
        assert get_response.status_code==200, print("passed.ok")

        assert (isinstance(get_response.text,str))
        assert get_response.text.count('"id":')==100
        assert get_response.encoding =='utf-8'
        assert get_response.headers["Content-Type"] == "application/json; charset=utf-8"
        assert get_response.url=="https://jsonplaceholder.typicode.com/posts"
        # assert get_response.json()['title']=="quaerat velit veniam amet cupiditate aut numquam ut sequi"


    def test_api_post(self):
        post_response = requests.post(f"{my_site}{get_post_url}", data=my_img, headers=my_obj)
        assert post_response.status_code == 201
        assert post_response.headers['Content-Length']=='15'

    def test_api_put(self):
        put_response = requests.put(f"{my_site}{put_delete_url}", json={'Content-Length': 'value1'})
        assert put_response.json()['json']["Content-Length"]=='value1'



    def test_api_delete(self):
        post_response = requests.post(f"{my_site}{get_post_url}", data=my_img, headers={"HTTP_HOST": "MyVeryOwnHost"})
        delete_response = requests.delete(f"{my_site}{put_delete_url}", headers={"HTTP_HOST": "MyVeryOwnHost"})
        # post_response.text
        assert post_response.headers["HTTP_HOST"] == "MyVeryOwnHost"
        assert delete_response.status_code == 404
        assert delete_response.headers["HTTP_HOST"] is None

