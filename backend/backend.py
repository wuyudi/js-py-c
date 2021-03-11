import ctypes as ct

from bottle import get, response, run

# https://stackoverflow.com/a/27781231/13040423


global_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
dll = ct.CDLL("./main.dll")

return_char_p = dll.return_char_p
return_char_p.restype = ct.c_char_p

return_int = dll.return_int
return_int.restype = ct.c_int

return_int_add = dll.return_int_add
return_int_add.restype = ct.c_int
return_int_add.argtypes = [ct.c_int]


@get("/get/<key:int>/")
def _main(key):
    # https://www.cnblogs.com/aknife/p/11941915.html
    # https://bottlepy.org/docs/dev/api.html?highlight=set_#bottle.BaseResponse.set_header
    # https://bottlepy.org/docs/dev/tutorial.html?highlight=header#the-response-object
    response.set_header("Access-Control-Allow-Origin", "*")
    return (
        {"key": global_dict[key]}
        | {"str": return_char_p().decode("utf-8")}
        | {"int": return_int(), "int_add": return_int_add(4)}
    )


run(port=4000, reloader=True, debug=True)
