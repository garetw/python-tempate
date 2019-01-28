import src.sample_lib as sample

if __name__ == "__main__":
    arguments = {
        "url": "https://google.com",
    }
    result = sample.get_url_kwargs(**arguments)
    print(result)