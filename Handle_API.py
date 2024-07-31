import requests

def fetch_data_from_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    user_info = response.json()
    if(user_info["success"] and "data" in user_info):
        user_data = user_info["data"]
        first = user_data["name"]["first"]
        last = user_data["name"]["last"]
        full_name = first+" "+last
        user_name = user_data["login"]["username"]
        password = user_data["login"]["password"]
        return [full_name,user_name, password]
    else:
        raise Exception("Failed to fetch user data")

def main():
    try:
        list = fetch_data_from_api()
        print(f"full name : {list[0]} \n Username : {list[1]} \n password : {list[2]}")
    
    except Exception as e:
        print(str(e))



if __name__ == "__main__":
    main()