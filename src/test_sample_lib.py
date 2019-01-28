import pytest
from . import sample_lib

########################################################
## This Function will fail
## We know it will fail. What do we do? We may still want it in our tests!
########################################################
## @wtf.are.these(?) - they're called "decorators"
## they inform pytest that we want to wrap this function in another function
## it's invisible to us, but we've marked the following function to `xfail` or
## "expected failure" because in this case, Line 16 is incorrect syntax.
@pytest.mark.xfail(reason="""
    Example Failure; Headers is incorrect.
""")
def test_get_url_explicit_args_failure():
    r = sample_lib.get_url_explicit_args(
        url = "https://google.com",
        headers = {
            'Content-Type: application/json'
        }
    )
    assert(r.status_code == 200)

#########################################################
## These will succeed
#########################################################
def test_get_url_explicit_args():
    r = sample_lib.get_url_explicit_args(
        url = "https://google.com",
        headers = {
            'Content-Type': 'application/json'
        }
    )
    assert r.status_code == 200

def test_get_url_keyword_args():
    arguments = {
        "url": "http://www.json.org/example.html?",
        "headers": {
            'Content-Type': 'application/json'
        }
    }
    r = sample_lib.get_url_kwargs(**arguments)
    assert r.status_code == 200

############################################################
## This one will be skipped
############################################################
## Down here, we can "decorate" our test with a `skip()` function
## We may not know what this function does, exactly, but we know we'll
## need it at some point in the future, so why not write something around it?
@pytest.mark.skip(reason="It should do some future thing")
def test_some_future_function():
    what_it_does = "i don't really know yet, but that's okay"
    vague_idea = 1
    assert vague_idea == 1
