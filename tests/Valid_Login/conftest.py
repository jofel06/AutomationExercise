import pytest

#list of valid credentials
@pytest.fixture(params=[("sampleuser01@yahoo.com", "thisispass01"),
                        ("sampleuser02@yahoo.com", "thisispass02"),
                        ("sampleuser03@yahoo.com", "thisispass03")])
def valid_login_credentials(request): #this fixture will provide the valid login credentials.
    return request.param

